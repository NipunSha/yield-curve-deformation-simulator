import argparse
import numpy as np
import pandas as pd

from ycdeform.engine import simulate_scenarios
from ycdeform.bond import bond_cashflows


def main():
    parser = argparse.ArgumentParser(description="Yield Curve Deformation Simulator")
    parser.add_argument("--maturity", type=float, default=5.0)
    parser.add_argument("--coupon", type=float, default=0.04)
    parser.add_argument("--face", type=float, default=100.0)
    parser.add_argument("--size-bp", type=float, default=25.0)

    args = parser.parse_args()

    # Simple default curve
    tenors = np.array([0.25, 0.5, 1, 2, 5, 10, 30])
    rates  = np.array([0.045, 0.046, 0.047, 0.045, 0.043, 0.042, 0.041])

    times, cashflows = bond_cashflows(args.maturity, args.coupon, face=args.face, freq=1)

    scenarios_df, risk_df, keyrate_df = simulate_scenarios(
        tenors=tenors,
        base_rates=rates,
        times=times,
        cashflows=cashflows,
        key_tenors=[2, 5, 10],
        size_bp=args.size_bp
    )

    print("\n=== Scenario Prices & PnL ===")
    print(scenarios_df.to_string(index=False))

    print("\n=== Risk Summary ===")
    print(risk_df.to_string(index=False))

    print("\n=== Key Rate DV01 (all scenarios) ===")
    print(keyrate_df.to_string(index=False))


if __name__ == "__main__":
    main()
