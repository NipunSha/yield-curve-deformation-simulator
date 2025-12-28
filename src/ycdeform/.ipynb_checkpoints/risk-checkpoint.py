import numpy as np
from .bond import bond_price


def eff_duration(times, cashflows, tenors, rates, bump_bp=1):
    bump = bump_bp / 10000
    p0 = bond_price(times, cashflows, tenors, rates)
    pup = bond_price(times, cashflows, tenors, rates + bump)
    pdn = bond_price(times, cashflows, tenors, rates - bump)
    dur = (pdn - pup) / (2 * p0 * bump)
    return float(dur)

def dv01(times, cashflows, tenors, rates, bump_bp=1):
    """
    Desk-style DV01: positive magnitude = price drop for +1bp.
    """
    bump = bump_bp / 10000
    p0 = bond_price(times, cashflows, tenors, rates)
    pup = bond_price(times, cashflows, tenors, rates + bump)
    return float(p0 - pup)

def convexity(times, cashflows, tenors, rates, bump_bp=1):
    bump = bump_bp / 10000
    p0  = bond_price(times, cashflows, tenors, rates)
    pup = bond_price(times, cashflows, tenors, rates + bump)
    pdn = bond_price(times, cashflows, tenors, rates - bump)
    cx = (pup + pdn - 2*p0) / (p0 * bump*bump)
    return float(cx)

def key_rate_dv01(times, cashflows, tenors, rates, key_tenor, bump_bp=1):
    """
    Bump only one key tenor node and reprice.
    Returns DV01 as positive magnitude (p0 - p_up).
    """
    bump = bump_bp / 10000
    r_up = rates.copy()
    idx = int(np.argmin(np.abs(tenors - key_tenor)))
    r_up[idx] += bump

    p0  = bond_price(times, cashflows, tenors, rates)
    pup = bond_price(times, cashflows, tenors, r_up)
    return float(p0 - pup)
