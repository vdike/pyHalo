import numpy as np
norm_z_dV = [6.1335e-08, 6.165e-08, 6.1969e-08, 6.2289e-08, 6.2612e-08, 6.2936e-08, 6.3262e-08, 6.3591e-08, 6.392e-08, 6.4252e-08, 6.4584e-08, 6.4918e-08, 6.5252e-08, 6.5588e-08, 6.5924e-08, 6.6261e-08, 6.6598e-08, 6.6936e-08, 6.7274e-08, 6.7612e-08, 6.795e-08, 6.8287e-08, 6.8625e-08, 6.8962e-08, 6.9299e-08, 6.9636e-08, 6.9972e-08, 7.0307e-08, 7.0641e-08, 7.0975e-08, 7.1308e-08, 7.164e-08, 7.1971e-08, 7.23e-08, 7.2629e-08, 7.2956e-08, 7.3282e-08, 7.3606e-08, 7.3929e-08, 7.4251e-08, 7.4571e-08, 7.4889e-08, 7.5205e-08, 7.552e-08, 7.5833e-08, 7.6144e-08, 7.6453e-08, 7.676e-08, 7.7065e-08, 7.7367e-08, 7.7668e-08, 7.7967e-08, 7.8263e-08, 7.8558e-08, 7.885e-08, 7.914e-08, 7.9428e-08, 7.9713e-08, 7.9996e-08, 8.0277e-08, 8.0555e-08, 8.0831e-08, 8.1105e-08, 8.1376e-08, 8.1644e-08, 8.191e-08, 8.2174e-08, 8.2435e-08, 8.2693e-08, 8.2949e-08, 8.3202e-08, 8.3452e-08, 8.37e-08, 8.3945e-08, 8.4188e-08, 8.4427e-08, 8.4664e-08, 8.4898e-08, 8.513e-08, 8.5358e-08, 8.5584e-08, 8.5808e-08, 8.6028e-08, 8.6246e-08, 8.646e-08, 8.6672e-08, 8.6882e-08, 8.7088e-08, 8.7292e-08, 8.7492e-08, 8.769e-08, 8.7885e-08, 8.8078e-08, 8.8267e-08, 8.8454e-08, 8.8637e-08, 8.8818e-08, 8.8996e-08, 8.9171e-08, 8.9343e-08, 8.9512e-08, 8.9679e-08, 8.9842e-08, 9.0003e-08, 9.0161e-08, 9.0316e-08, 9.0468e-08, 9.0617e-08, 9.0763e-08, 9.0906e-08, 9.1046e-08, 9.1184e-08, 9.1318e-08, 9.145e-08, 9.1579e-08, 9.1704e-08, 9.1827e-08, 9.1947e-08, 9.2065e-08, 9.2179e-08, 9.229e-08, 9.2399e-08, 9.2505e-08, 9.2607e-08, 9.2707e-08, 9.2804e-08, 9.2899e-08, 9.299e-08, 9.3079e-08, 9.3164e-08, 9.3247e-08, 9.3327e-08, 9.3404e-08, 9.3479e-08, 9.355e-08, 9.3619e-08, 9.3685e-08, 9.3748e-08, 9.3808e-08, 9.3866e-08, 9.392e-08, 9.3972e-08, 9.4022e-08, 9.4068e-08, 9.4112e-08, 9.4153e-08, 9.4191e-08, 9.4226e-08, 9.4259e-08, 9.4289e-08, 9.4316e-08, 9.4341e-08, 9.4362e-08, 9.4382e-08, 9.4398e-08, 9.4412e-08, 9.4423e-08, 9.4431e-08, 9.4437e-08, 9.444e-08, 9.4441e-08, 9.4439e-08, 9.4434e-08, 9.4427e-08, 9.4417e-08, 9.4404e-08, 9.4389e-08, 9.4372e-08, 9.4352e-08, 9.4329e-08, 9.4304e-08, 9.4276e-08, 9.4245e-08, 9.4213e-08, 9.4177e-08, 9.414e-08, 9.4099e-08, 9.4057e-08, 9.4012e-08, 9.3964e-08, 9.3914e-08, 9.3862e-08, 9.3807e-08, 9.375e-08, 9.369e-08, 9.3628e-08, 9.3564e-08, 9.3497e-08, 9.3428e-08, 9.3357e-08, 9.3283e-08, 9.3207e-08, 9.3129e-08, 9.3049e-08, 9.2966e-08, 9.2881e-08, 9.2794e-08, 9.2704e-08, 9.2613e-08, 9.2519e-08, 9.2423e-08, ]
plaw_index_z = [-1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.91, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.92, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.93, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.94, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.95, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.96, -1.97, -1.97, -1.97, ]
z_range = np.array([0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31, 0.33, 0.35, 0.37, 0.39, 0.41, 0.43, 0.45, 0.47, 0.49, 0.51, 0.53, 0.55, 0.57, 0.59, 0.61, 0.63, 0.65, 0.67, 0.69, 0.71, 0.73, 0.75, 0.77, 0.79, 0.81, 0.83, 0.85, 0.87, 0.89, 0.91, 0.93, 0.95, 0.97, 0.99, 1.01, 1.03, 1.05, 1.07, 1.09, 1.11, 1.13, 1.15, 1.17, 1.19, 1.21, 1.23, 1.25, 1.27, 1.29, 1.31, 1.33, 1.35, 1.37, 1.39, 1.41, 1.43, 1.45, 1.47, 1.49, 1.51, 1.53, 1.55, 1.57, 1.59, 1.61, 1.63, 1.65, 1.67, 1.69, 1.71, 1.73, 1.75, 1.77, 1.79, 1.81, 1.83, 1.85, 1.87, 1.89, 1.91, 1.93, 1.95, 1.97, 1.99, 2.01, 2.03, 2.05, 2.07, 2.09, 2.11, 2.13, 2.15, 2.17, 2.19, 2.21, 2.23, 2.25, 2.27, 2.29, 2.31, 2.33, 2.35, 2.37, 2.39, 2.41, 2.43, 2.45, 2.47, 2.49, 2.51, 2.53, 2.55, 2.57, 2.59, 2.61, 2.63, 2.65, 2.67, 2.69, 2.71, 2.73, 2.75, 2.77, 2.79, 2.81, 2.83, 2.85, 2.87, 2.89, 2.91, 2.93, 2.95, 2.97, 2.99, 3.01, 3.03, 3.05, 3.07, 3.09, 3.11, 3.13, 3.15, 3.17, 3.19, 3.21, 3.23, 3.25, 3.27, 3.29, 3.31, 3.33, 3.35, 3.37, 3.39, 3.41, 3.43, 3.45, 3.47, 3.49, 3.51, 3.53, 3.55, 3.57, 3.59, 3.61, 3.63, 3.65, 3.67, 3.69, 3.71, 3.73, 3.75, 3.77, 3.79, 3.81, 3.83, 3.85, 3.87, 3.89, 3.91, 3.93, 3.95, 3.97, 3.99, 4.01, ])

delta_z = 0.02

