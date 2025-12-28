# Yield Curve Deformation Simulator

This project simulates realistic yield curve shape changes and studies how they
affect bond prices and interest rate risk measures.

It is designed to connect **macroeconomic intuition** about interest rates with
**quantitative fixed-income risk analysis**.

---

## What is a yield curve?

A yield curve shows interest rates for loans of different maturities
(short-term to long-term).

Changes in the *shape* of the yield curve reflect expectations about:
- economic growth
- inflation
- monetary policy
- long-term risk premia

---

## What this project does

Starting from a base yield curve, the simulator applies four standard
curve deformations used in macro and rates analysis:

- **Steepener** – long-term rates move more than short-term rates  
- **Flattener** – short- and long-term rates converge  
- **Twist** – rates rotate around a middle maturity  
- **Butterfly** – middle maturities move differently from the short and long ends  

For each scenario, the project computes:

- Bond price and PnL relative to the base curve  
- Effective duration  
- DV01 (price sensitivity to a 1bp rate change)  
- Convexity  
- Key-rate DV01 decomposition  

Results are presented as tables and yield curve plots, and exported as CSV files.

---

## Why this matters

Yield curve movements are central to macroeconomic analysis and fixed-income
markets. Different curve shapes imply different risks for bond portfolios.

This project demonstrates how:
- macro expectations translate into curve shape changes, and
- curve shape changes translate into bond price and risk outcomes.

---

## Project structure

yield-curve-deformation-simulator/
├── notebook/ # Main analysis and demonstration notebook
├── src/ycdeform/ # Core simulation, pricing, and risk engine
├── reports/ # Generated outputs (CSV tables)
├── data/ # Placeholder for future data (if required)
├── README.md
└── pyproject.toml

---

## How to run

1. Clone the repository  
2. Set up a Python environment (Anaconda or pip)
3. Open and run the notebook:

notebook/01_build_core_engine.ipynb

Running the notebook will:
- simulate yield curve scenarios
- compute prices and risk measures
- generate tables and plots
- save outputs to the `reports/` folder

---

## Tools used

- Python  
- NumPy  
- Pandas  
- Matplotlib  

---

## Intended audience

This project is intended for:
- economics and finance students  
- macro and fixed-income researchers  
- anyone interested in yield curve dynamics and bond risk analysis  
