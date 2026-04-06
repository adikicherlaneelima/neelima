import numpy as np

def moving_average(data, window=5):
    return np.convolve(data, np.ones(window)/window, mode='valid')

def predict_next(data, window=5):
    if len(data) < window:
        return data[-1]
    return np.mean(data[-window:])