# stochPathSim

**stochPathSim** is a Python library designed for stochastic modeling, simulations, and statistical analysis. This library implements widely used stochastic models for financial and quantitative research, such as Geometric Brownian Motion (GBM), Heston Model, Vasicek Model, and more. It also includes utilities for statistical evaluation and visualization of simulations, making it ideal for researchers, quants, and data scientists.

---

## Features
- **Simulation of Stochastic Models**:
  - Geometric Brownian Motion (GBM)
  - Heston Model
  - Vasicek Model
  - Hull-White Model
  - Cox-Ingersoll-Ross (CIR) Model
  - Black-Derman-Toy (BDT) Model
  - Ho-Lee Model
- **Statistical Analysis**:
  - Probability levels (P_LEVEL)
  - Quantile-based analysis (99th, 90th, 10th, 1st percentiles)
  - Mean value calculation
  - Exceedance metrics (upper and lower exceedance counts)
- **Visualization**:
  - Static visualizations using Matplotlib

---

## Installation

To install the library from PyPI:

```bash
pip install stochPathSim
```

---

## Usage

### 1. **Simulate Geometric Brownian Motion (GBM)**

```python
from stochPathSim.gbm import GeometricBrownianMotion
from stochPathSim.statistics_utils import calculate_statistics, display_statistics


# Initialize GBM
gbm = GeometricBrownianMotion(mu=0.1, sigma=0.2, s0=100, T=1, n=1000, paths=1000)

# Simulate
time, simulations = gbm.simulate()

# Calculate statistics
initial_value = 100  # Initial value of the simulation
stats_df = calculate_statistics(simulations, initial_value)

# Display statistics
display_statistics(stats_df, time)

# Plot simulation
plot_simulation(time, simulations)
```

### 2. **Statistical Analysis with P_LEVEL and Exceedance Metrics**

```python
from stochPathSim.statistics_utils import calculate_statistics, display_statistics

# Assuming `simulations` is a 2D array of paths and `time` is the time vector
initial_value = 100

# Calculate statistics
stats_df = calculate_statistics(simulations, initial_value)

# Display statistics
display_statistics(stats_df, time)

# Plot simulation with 15 paths
plot_simulation(time, simulations, num_paths=15)
```



## Supported Models

### Geometric Brownian Motion (GBM)
- Simulates the evolution of stock prices under constant drift and volatility.
- **Applications**: Equity modeling, option pricing.

### Heston Model
- Stochastic volatility model with mean-reverting variance.
- **Applications**: Volatility modeling, derivative pricing.

### Vasicek Model
- Mean-reverting interest rate model.
- **Applications**: Fixed income modeling.

### Hull-White Model
- Generalized mean-reverting interest rate model with time-dependent drift.
- **Applications**: Bond pricing.

### Cox-Ingersoll-Ross (CIR) Model
- Mean-reverting interest rate model with non-negative constraints.
- **Applications**: Credit risk modeling.

### Black-Derman-Toy (BDT) Model
- Lognormal interest rate model.
- **Applications**: Term structure modeling.

### Ho-Lee Model
- Arbitrage-free interest rate model with Gaussian increments.
- **Applications**: Pricing interest rate derivatives.

---

## Contributing
We welcome contributions! If you'd like to contribute, please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature-name'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

MIT License

Copyright (c) 2024 Amit Kumar Jha

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## Contact
For questions or feedback, contact:
- **Name**: Amit Kumar Jha
- **Email**: jha.8@iitj.ac.in

