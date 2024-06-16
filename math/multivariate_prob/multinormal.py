#!/usr/bin/env python3
""" Implements the Multinormal class
"""
import numpy as np


class MultiNormal:
    """ Class to model a multivariate normal distribution
    """
    def __init__(self, data):
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError('data must be a 2D numpy.ndarray')

        _, n = data.shape

        if n < 2:
            raise ValueError('data must contain multiple data points')

        mean = np.mean(data, axis=1).reshape(1, -1).T

        deviations = data - mean

        self.mean = mean
        self.cov = deviations @ deviations.T / (n - 1)

import numpy as np
class MultiNormal:
    def __init__(self, data):
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1).reshape(d, 1)

        data_centered = data - self.mean

        self.cov = np.dot(data_centered, data_centered.T) / (n - 1)

    def pdf(self, x):
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det_cov = np.linalg.det(self.cov)
        inv_cov = np.linalg.inv(self.cov)
        norm_factor = 1 / np.sqrt((2 * np.pi) ** d * det_cov)
        x_centered = x - self.mean
        exponent = -0.5 * np.dot(np.dot(x_centered.T, inv_cov), x_centered)

        pdf_value = norm_factor * np.exp(exponent)

        return float(pdf_value)
