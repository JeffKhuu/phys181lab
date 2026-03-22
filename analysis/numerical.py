from typing import Callable
import numpy as np

"""
rk4 returns the four coefficients k1, k2, k3 and k4 from performing 4th order Runge-Kutta method
    for a function f(x_n, y_n) = dx/dy for the given intial values x_0, y_0 and stepsize h
f       - 1st order differential equation depending on x and y
x_0     - initial value of x_0
y_0     - value of y_0 at x_0
h       - step size
returns - unweighted RK4 coefficients k1, k2, k3 and k4
"""


def rk4(f, x_0, y_0, h):
    k1 = h * f(x_0, y_0)
    k2 = h * f(x_0 + h / 2, y_0 + k1 * h / 2)
    k3 = h * f(x_0 + h / 2, y_0 + k2 * h / 2)
    k4 = h * f(x_0, y_0 + k3 * h)
    return k1, k2, k3, k4


"""
pendulum solves the second order differential equation for the motion of a pendulum
         and returns the angular displacement with the initial values theta_0, omega_0 and t_0
         at h time step intervals
alpha   - change in angular velocity over time
omega   - change in angular displacement over time
omega_0 - initial angular velocity
t_0     - initial time
t_f     - final time
h       - step size
returns - angular displacement at time steps as numpy array
"""


def pendulum(
    alpha: Callable,
    omega: Callable,
    theta_0: float,
    omega_0: float,
    t_0: float,
    t_f: float,
    h: float = 0.001,
):
    n = t_f / h
    t = np.linspace(t_0, t_f, n)

    v = np.zeros(n)
    x = np.zeros(n)
    v[0] = omega_0
    x[0] = theta_0

    for t_n in range(0, n - 1):
        k1_theta = h * omega(v[t_n])
        k1_omega = h * alpha(x[t_n], v[t_n])
        k2_theta = h * omega(v[t_n] + 0.5 * k1_omega)
        k2_omega = h * alpha(x[t_n] + 0.5 * k1_theta, v[t_n] + 0.5 * k1_omega)
        k3_theta = h * omega(v[t_n] + 0.5 * k2_omega)
        k3_omega = h * alpha(x[t_n] + 0.5 * k2_theta, v[t_n] + 0.5 * k2_omega)
        k4_theta = h * omega(v[t_n] + k3_omega)
        k4_omega = h * alpha(x[t_n] + k3_theta, v[t_n] + k3_omega)
        x[t_n + 1] = x[t_n] + (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta) / 6
        v[t_n + 1] = v[t_n] + (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega) / 6
    return t, x, v


def pendulum_step(
    alpha: Callable,
    omega: Callable,
    theta_0: float,
    omega_0: float,
    h: float = 0.001,
):
    k1_theta = h * omega(omega_0)
    k1_omega = h * alpha(theta_0, omega_0)

    k2_theta = h * omega(omega_0 + 0.5 * k1_omega)
    k2_omega = h * alpha(theta_0 + 0.5 * k1_theta, omega_0 + 0.5 * k1_omega)

    k3_theta = h * omega(omega_0 + 0.5 * k2_omega)
    k3_omega = h * alpha(theta_0 + 0.5 * k2_theta, omega_0 + 0.5 * k2_omega)

    k4_theta = h * omega(omega_0 + k3_omega)
    k4_omega = h * alpha(theta_0 + k3_theta, omega_0 + k3_omega)

    theta_n = theta_0 + (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta) / 6
    omega_n = omega_0 + (k1_omega + 2 * k2_omega + 2 * k3_omega + k4_omega) / 6
    return theta_n, omega_n
