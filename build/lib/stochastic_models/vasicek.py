import numpy as np

class VasicekModel:
    def __init__(self, r0, kappa, theta, sigma, T, n, paths):
        """
        Initialize the Vasicek model parameters.
        :param r0: Initial interest rate
        :param kappa: Rate of mean reversion
        :param theta: Long-term mean interest rate
        :param sigma: Volatility of interest rate
        :param T: Time horizon (in years)
        :param n: Number of time steps
        :param paths: Number of simulation paths
        """
        self.r0 = r0
        self.kappa = kappa
        self.theta = theta
        self.sigma = sigma
        self.T = T
        self.n = n
        self.paths = paths

    def simulate(self):
        """
        Simulate interest rate paths using the Vasicek model.
        :return: Simulated interest rate paths
        """
        dt = self.T / self.n
        r = np.zeros((self.paths, self.n))
        r[:, 0] = self.r0

        for t in range(1, self.n):
            dr = (
                self.kappa * (self.theta - r[:, t-1]) * dt
                + self.sigma * np.sqrt(dt) * np.random.normal(size=self.paths)
            )
            r[:, t] = r[:, t-1] + dr

        return r
