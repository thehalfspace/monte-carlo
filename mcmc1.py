# Monte Carlo Markov Chain for dummies

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from scipy.stats import norm
plt.rcParams["patch.force_edgecolor"] = True


# Generate 20 points form a normal distribution centered
# around zero

data = np.random.randn(20)

ax = plt.subplot()
ax.hist(data)
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
ax.set_title("Histogram of observed data")
plt.show()

# We assume we know the standard deviation to be equal to 1
# Our goal is to estimate the posterior of the mean


# Assume: normal distribution of data

# Analytically calculate posterior for this data
def calc_posterior_analytical(data, x, mu0, sigma0):
    sigma = 1
    n = len(data)

    mu_post = (mu0/sigma0**2 + data.sum()/sigma**2)
