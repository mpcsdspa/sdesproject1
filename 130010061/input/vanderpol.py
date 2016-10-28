import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def damping_factor(mu):
    def van_der_pol_dynamics(x, t):
        x1 = x[1]
        x2 = -mu * (x[0] ** 2.0 - 1.0) * x[1] - x[0]
        result = np.array([x1, x2])
        return result
    return van_der_pol_dynamics


def plot_solutions(mu=0.0, x0=[2, 0.5], tf=50.0, N=200):
    d = damping_factor(mu)
    t = np.linspace(0, tf, N)
    x = odeint(d, x0, t)
    plt.figure(figsize=(10, 6))
    plt.plot(t, x[:, 0], marker='.', color='r', linestyle='--', label='x1')
    plt.plot(t, x[:, 1], marker='*', color='g', linestyle='--', label='x2')
    plt.legend(loc=2, prop={'size': 10})
    plt.title("Time variation of Van der Pol equation for $\mu$=" +
              str(mu), fontsize=12)
    plt.xlabel("time(seconds)", fontsize=10)
    plt.ylabel("Van der Pol solutions", fontsize=10)
    plt.savefig('VanderPol_Solutions_mu=' + str(int(mu)) + '.png')


def plot_limit_cycle(mu=0.0, x0=[2, 0.5], tf=50.0, N=200):
    d = damping_factor(mu)
    t = np.linspace(0, tf, N)
    x = odeint(d, x0, t)
    plt.figure(figsize=(10, 6))
    plt.plot(x[:, 0], x[:, 1], marker='.', linestyle='--')
    plt.title("Solution of Van der Pol equation for $\mu$=" +
              str(mu), fontsize=12)
    plt.xlabel("x_1", fontsize=10)
    plt.ylabel("x_2", fontsize=10)
    plt.savefig('Limit_cycle_mu=' + str(int(mu)) + '.png')


def all_mu_limit_cycle(mu=[0.0, 0.01, 1.0, 3.0, 10.0], x0=[2, 0.5], tf=50.0, N=2000):
    for mu1 in mu:
        d = damping_factor(mu1)
        t = np.linspace(0, tf, N)
        x = odeint(d, x0, t)
        plt.plot(x[:, 0], x[:, 1], marker='.', linestyle='--', label=str(mu1))
        plt.legend()
        plt.xlabel("x_1", fontsize=10)
        plt.ylabel("x_2", fontsize=10)
    plt.title("Limit cycles for various $\mu$", fontsize=12)
    plt.savefig('all_in_one.png')


if __name__ == '__main__':
    all_mu_limit_cycle(mu=[0.0, 0.01, 1.0, 3.0, 10.0],
                       x0=[2, 0.5], tf=50.0, N=2000)
    plot_solutions(mu=0.0, x0=[2, 0.5], tf=50.0, N=200)
    plot_limit_cycle(mu=0.0, x0=[2, 0.5], tf=50.0, N=200)
    plot_solutions(mu=1.0, x0=[2, 0.5], tf=30.0, N=200)
    plot_limit_cycle(mu=3.0, x0=[2, 0.5], tf=30.0, N=200)
    plot_solutions(mu=5.0, x0=[2, 0.5], tf=30.0, N=200)
    plot_solutions(mu=1000.0, x0=[2, 0.5], tf=3000.0, N=5000)
