import numpy as np
from lenstronomy.LensModel.lens_model import LensModel
from pyHalo.Rendering.rendering_class_base import RenderingClassBase
from pyHalo.Rendering.SpatialDistributions.correlated import Correlated2D
from pyHalo.Rendering.MassFunctions.delta import DeltaFunction
from pyHalo.Cosmology.geometry import Geometry
from pyHalo.single_realization import realization_at_z

class CorrelatedStructure(RenderingClassBase):

    """
    This class generates a population of halos with a spatial distribution that tracks the dark matter density in halos
    at each lens plane
    """

    def __init__(self, kwargs_rendering, realization, r_max_arcsec):

        """

        :param kwargs_rendering: keyword arguments that specify the mass function model
        :param realization: an instance of Realization used to compute the convergence at each lens plane
        :param r_max_arcsec: the radius of area at which the halos are rendered
        """

        self.kwargs_rendering = kwargs_rendering
        self._realization = realization
        self.cylinder_geometry = Geometry(self._realization.lens_cosmo.cosmo,
                                                     self._realization.lens_cosmo.z_lens,
                                                     self._realization.lens_cosmo.z_source,
                                                     2 * r_max_arcsec,
                                                     'DOUBLE_CONE')

        self.spatial_distribution_model = Correlated2D(self.cylinder_geometry)
        self._rmax = r_max_arcsec

    def render(self, x_center_interp_list, y_center_interp_list, arcsec_per_pixel):

        """
        Generates halo masses and positions for correlated structure along the line of sight around
        the angular coordinate of each light ray

        :param x_center_interp_list: a list of interp1d functions that return the x angular position of a
        ray given a comoving distance
        :param y_center_interp_list: a list of interp1d functions that return the y angular position of a
        ray given a comoving distance
        :param arcsec_per_pixel: sets the spatial resolution for the rendering of correlated structure
        :return: mass (in Msun), x (arcsec), y (arcsec), r3d (kpc), redshift
        """

        masses = np.array([])
        x = np.array([])
        y = np.array([])
        redshifts = np.array([])

        plane_redshifts = self._realization.unique_redshifts
        delta_z = []
        for i, zi in enumerate(plane_redshifts[0:-1]):
            delta_z.append(plane_redshifts[i+1] - plane_redshifts[i])

        for x_image_interp, y_image_interp in zip(x_center_interp_list, y_center_interp_list):

            for z, dz in zip(plane_redshifts, delta_z):

                if dz > 0.2:
                    print('WARNING: redshift spacing is possibly too large due to the few number of halos '
                          'in the lens model!')

                m = self.render_masses_at_z(z, dz)
                nhalos = len(m)

                if nhalos == 0:
                    continue

                rendering_radius = self._rmax * self.cylinder_geometry.rendering_scale(z)

                d = self.cylinder_geometry._cosmo.D_C_transverse(z)

                x_angle = x_image_interp(d)
                y_angle = y_image_interp(d)

                _x, _y = self.render_positions_at_z(nhalos, z, x_angle, y_angle,
                                                    rendering_radius, arcsec_per_pixel)

                if len(_x) > 0:
                    _z = np.array([z] * len(_x))
                    masses = np.append(masses, m)
                    x = np.append(x, _x)
                    y = np.append(y, _y)
                    redshifts = np.append(redshifts, _z)

        subhalo_flag = [False] * len(masses)
        r3d = np.array([None] * len(masses))

        return masses, x, y, r3d, redshifts, subhalo_flag

    def render_positions_at_z(self, n, z, angular_coordinate_x, angular_coordinate_y, rendering_radius, arcsec_per_pixel):

        """

        :param n: number of objects to render
        :param z: redshift
        :param angular_coordinate_x: the angular coordinate in arcsec of a light ray at redshift z
        :param angular_coordinate_y: the angular coordinate in arcsec of a light ray at redshift z
        :param rendering_radius: the angular radius inside which to render objects
        :param arcsec_per_pixel: sets the spatial resolution for the rendering of correlated structure
        :return: the positions in arcsec of the rendered objects
        """
        realization_at_plane, _ = realization_at_z(self._realization,
                                                   z,
                                                   angular_coordinate_x,
                                                   angular_coordinate_y,
                                                   rendering_radius)

        lens_model_list, _, kwargs_lens, numerical_interp = realization_at_plane.lensing_quantities(
            add_mass_sheet_correction=False)

        if len(lens_model_list) == 0:
            return np.array([]), np.array([])

        lens_model = LensModel(lens_model_list, numerical_alpha_class=numerical_interp)
        npix = int(2 * rendering_radius / arcsec_per_pixel)
        _r = np.linspace(-rendering_radius, rendering_radius, 2 * npix)
        xx, yy = np.meshgrid(_r, _r)
        shape0 = xx.shape
        xx, yy = xx.ravel(), yy.ravel()
        rr = np.sqrt(xx ** 2 + yy ** 2)
        inds_zero = np.where(rr > rendering_radius)[0].ravel()
        kpc_per_asec = self.cylinder_geometry.kpc_per_arcsec(z)

        pdf = lens_model.kappa(xx + angular_coordinate_x, yy + angular_coordinate_y, kwargs_lens)

        if np.sum(pdf) == 0:
            return np.array([]), np.array([])

        pdf[inds_zero] = 0.
        inds_nan = np.where(np.isnan(pdf))
        pdf[inds_nan] = 0.

        x_kpc, y_kpc = self.spatial_distribution_model.draw(n, rendering_radius, pdf.reshape(shape0), z,
                                                            angular_coordinate_x, angular_coordinate_y)


        x_arcsec = x_kpc / kpc_per_asec
        y_arcsec = y_kpc / kpc_per_asec
        return x_arcsec, y_arcsec

    def render_masses_at_z(self, z, delta_z):

        """
        :param z: redshift at which to render masses
        :param delta_z: thickness of the redshift slice
        :return: halo masses at the desired redshift in units Msun
        """

        if self.kwargs_rendering['mass_function_type'] == 'DELTA':
            rho = self.kwargs_rendering['mass_fraction'] * self._realization.lens_cosmo.cosmo.rho_dark_matter_crit
            volume = self.cylinder_geometry.volume_element_comoving(z, delta_z)
            mass_function = DeltaFunction(10 ** self.kwargs_rendering['logM'],
                                          volume, rho)
        else:
            raise Exception('no other mass function for correlated structure currently implemented')

        return mass_function.draw()

    @staticmethod
    def keys_convergence_sheets(keywords_master):
        return {}

    def convergence_sheet_correction(self, kwargs_mass_sheets=None):

        return [{}], [], []

    @staticmethod
    def keyword_parse_render(keywords_master):

        return {}
