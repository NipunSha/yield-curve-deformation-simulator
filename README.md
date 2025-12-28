# Yield Curve Deformation Simulator

This project simulates common yield curve shape changes used in macro and rates analysis
and evaluates their impact on bond prices and risk measures.

## What the project does

Starting from a base yield curve, the tool simulates four realistic curve movements:

- **Steepener**: long-term rates move more than short-term rates  
- **Flattener**: short- and long-term rates converge  
- **Twist**: rates rotate around a middle maturity  
- **Butterfly**: middle maturities move differently than short and long ends  

For each scenario, the project computes:

- Bond price and PnL relative to the base curve  
- Effective duration  
- DV01  
- Convexity  
- Key-rate DV01 decomposition  

The results are displayed as tables and visualised using yield curve plots.
Outputs are also saved as CSV files for reproducibility.

## Why this matters

Yield curve movements reflect macroeconomic expectations about growth,
inflation, and monetary policy. Understanding how different curve shapes
affect bond values is central to fixed income, macro trading, and policy analysis.

This project connects macroeconomic intuition with quantitative bond risk metrics
in a transparent and reproducible way.

## Project structure

- `notebook/` – main analysis notebook  
- `src/` – reusable simulation and pricing code  
- `reports/` – exported results (CSV files and plots)

## Tools used

- Python  
- NumPy  
- Pandas  
- Matplotlib  

