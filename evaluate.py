import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.metrics


def residuals(actual, predicted):
    return actual - predicted


def SSE(actual, predicted):
    return (residuals(actual, predicted) ** 2).sum()


def MSE(actual, predicted):
    n = actual.shape[0]
    return SSE(actual, predicted) / n


def RMSE(actual, predicted):
    return math.sqrt(MSE(actual, predicted))


def ESS(actual, predicted):
    return ((predicted - actual.mean()) ** 2).sum()


def TSS(actual):
    return ((actual - actual.mean()) ** 2).sum()


def regression_errors(actual, predicted):
    return pd.Series({
        'SSE': SSE(actual, predicted),
        'ESS': ESS(actual, predicted),
        'TSS': TSS(actual),
        'MSE': MSE(actual, predicted),
        'RMSE': RMSE(actual, predicted),
        'R^2': (ESS(actual, predicted))/(TSS(actual)),
    })


def baseline_mean_errors(actual):
    predicted = actual.mean()
    return {
        'SSE': SSE(actual, predicted),
        'MSE': MSE(actual, predicted),
        'RMSE': RMSE(actual, predicted),
    }


def better_than_baseline(actual, predicted):
    rmse_baseline = RMSE(actual, actual.mean())
    rmse_model = RMSE(actual, predicted)
    return rmse_model < rmse_baseline


def model_significance(ols_model):
    return {
        'r^2 -- variance explained': ols_model.rsquared,
        'p-value -- P(data|model == baseline)': ols_model.f_pvalue,
    }


def plot_residuals(actual, predicted):
    residuals = actual - predicted
    plt.hlines(0, actual.min(), actual.max(), ls=':')
    plt.scatter(actual, residuals)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title('Actual vs Residual')
    plt.show()
