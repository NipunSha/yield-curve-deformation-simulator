import numpy as np
from .curve import discount_factor



def bond_cashflows(maturity, coupon_rate, face=100.0, freq=1):
    """
    Generate cashflow times + amounts for a plain-vanilla fixed-rate bond.
    """
    times = np.arange(1, maturity * freq + 1) / freq
    cpn = face * coupon_rate / freq
    cashflows = np.full_like(times, cpn, dtype=float)
    cashflows[-1] += face
    return times, cashflows

def bond_price(times, cashflows, tenors, rates):
    """
    Price a bond by discounting cashflows using the zero curve.
    """
    dfs = np.array([discount_factor(t, tenors, rates) for t in times])
    return float(np.sum(cashflows * dfs))
