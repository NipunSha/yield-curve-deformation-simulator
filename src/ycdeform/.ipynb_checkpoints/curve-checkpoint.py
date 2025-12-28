import numpy as np

# -----------------------------
# Core: zero rate + discounting
# -----------------------------

def zero_rate(t, tenors, rates):
    """
    Piecewise-linear interpolation of the zero curve.
    t: time in years (float)
    tenors, rates: arrays of same length
    """
    tenors = np.asarray(tenors, dtype=float)
    rates = np.asarray(rates, dtype=float)
    return float(np.interp(t, tenors, rates))

def discount_factor(t, tenors, rates):
    """
    Continuous compounding discount factor: exp(-r(t) * t)
    """
    r = zero_rate(t, tenors, rates)
    return float(np.exp(-r * t))


# -------------------------------------
# Yield curve deformations (scenario FX)
# -------------------------------------

def _unit_tilt_weights(tenors):
    """
    Convert tenors into smooth weights from roughly -0.5 to +0.5.
    Used for steepeners/flatteners.
    """
    tenors = np.asarray(tenors, dtype=float)
    span = tenors.max() - tenors.min()
    if span == 0:
        return np.zeros_like(tenors)
    return (tenors - tenors.mean()) / span

def apply_parallel(tenors, rates, size_bp=10):
    """
    Shift all rates up/down by size_bp.
    """
    bump = size_bp / 10000.0
    return np.asarray(rates, dtype=float) + bump

def apply_steepener(tenors, rates, size_bp=25):
    """
    Long-end up more than short-end (tilt).
    """
    bump = size_bp / 10000.0
    w = _unit_tilt_weights(tenors)
    return np.asarray(rates, dtype=float) + bump * w

def apply_flattener(tenors, rates, size_bp=25):
    """
    Long-end down relative to short-end (opposite tilt).
    """
    bump = size_bp / 10000.0
    w = _unit_tilt_weights(tenors)
    return np.asarray(rates, dtype=float) - bump * w

def apply_twist(tenors, rates, size_bp=25, pivot=5.0):
    """
    Rates rotate around a pivot maturity:
    - below pivot move one way
    - above pivot move the other way
    """
    bump = size_bp / 10000.0
    tenors = np.asarray(tenors, dtype=float)
    rates = np.asarray(rates, dtype=float)

    # signed distance from pivot, scaled
    span = tenors.max() - tenors.min()
    if span == 0:
        return rates.copy()

    w = (tenors - pivot) / span
    return rates + bump * w

def apply_butterfly(tenors, rates, size_bp=25, belly=5.0):
    """
    Butterfly: belly moves opposite to wings.
    Often used to represent curvature changes.
    """
    bump = size_bp / 10000.0
    tenors = np.asarray(tenors, dtype=float)
    rates = np.asarray(rates, dtype=float)

    # Create a smooth "hump" centered at belly
    span = tenors.max() - tenors.min()
    if span == 0:
        return rates.copy()

    x = (tenors - belly) / span
    hump = np.exp(-(x**2) / (2 * (0.20**2)))  # smooth peak near belly
    hump = hump - hump.mean()                 # make it roughly neutral overall

    return rates + bump * hump
