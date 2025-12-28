import numpy as np

def _weights_linear(tenors):
    return (tenors - tenors.mean()) / (tenors.max() - tenors.min())

def steepener(tenors, rates, size_bp=25):
    size = size_bp / 10000
    w = _weights_linear(tenors)
    return rates + size * w

def flattener(tenors, rates, size_bp=25):
    size = size_bp / 10000
    w = _weights_linear(tenors)
    return rates - size * w

def twist(tenors, rates, size_bp=25, pivot=5):
    size = size_bp / 10000
    w = (tenors - pivot) / (tenors.max() - tenors.min())
    return rates + size * w

def butterfly(tenors, rates, size_bp=25, belly=5):
    """
    Raise/lower the belly relative to wings.
    """
    size = size_bp / 10000
    # bell-shaped weight around belly
    w = -np.abs(tenors - belly)
    w = (w - w.mean()) / (np.max(np.abs(w)) + 1e-12)
    return rates + size * w
