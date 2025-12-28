import pandas as pd

from .bond import bond_price, bond_cashflows
from .risk import eff_duration, dv01, convexity, key_rate_dv01
from . import scenarios as sc



SCENARIO_FUNCS = {
    "Base": None,
    "Steepener (+25bp shape)": lambda t, r: sc.steepener(t, r, 25),
    "Flattener (+25bp shape)": lambda t, r: sc.flattener(t, r, 25),
    "Twist (+25bp, pivot=5y)": lambda t, r: sc.twist(t, r, 25, pivot=5),
    "Butterfly (+25bp, belly=5y)": lambda t, r: sc.butterfly(t, r, 25, belly=5),
}

def simulate_scenarios(tenors, base_rates, times, cashflows, key_tenors=(2,5,10)):
    base_price = bond_price(times, cashflows, tenors, base_rates)

    rows = []
    risk_rows = []
    kr_rows = []

    for name, fn in SCENARIO_FUNCS.items():
        rates = base_rates if fn is None else fn(tenors, base_rates)
        price = bond_price(times, cashflows, tenors, rates)

        rows.append({
            "Scenario": name,
            "BasePrice": base_price,
            "ScenarioPrice": price,
            "PnL_vs_Base": price - base_price
        })

        risk_rows.append({
            "Scenario": name,
            "Price": price,
            "EffDuration": eff_duration(times, cashflows, tenors, rates),
            "DV01_per1bp": dv01(times, cashflows, tenors, rates),
            "Convexity": convexity(times, cashflows, tenors, rates)
        })

        for kt in key_tenors:
            kr_rows.append({
                "Scenario": name,
                "KeyRate": f"{kt}Y",
                "DV01": key_rate_dv01(times, cashflows, tenors, rates, kt)
            })

    scenarios_df = pd.DataFrame(rows)
    risk_df = pd.DataFrame(risk_rows)
    keyrate_df = pd.DataFrame(kr_rows)

    return scenarios_df, risk_df, keyrate_df
