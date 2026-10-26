# Vectorized Monte Carlo Option Pricer & Greeks Engine

## Overview
High-performance quantitative framework for pricing European vanilla options under Geometric Brownian Motion (GBM). All Monte Carlo paths are fully vectorized using NumPy and verified against analytical solutions derived from the Black-Scholes-Merton partial differential equation.

## Mathematical Formulation
Under the risk-neutral measure $\mathbb{Q}$, terminal stock prices follow:
$$S_T = S_0 \exp\left(\left(r - \frac{1}{2}\sigma^2\right)T + \sigma \sqrt{T} Z\right), \quad Z \sim \mathcal{N}(0, 1)$$

The discounted expectation yields the option price:
$$V_0 = e^{-rT} \mathbb{E}^\mathbb{Q}[\max(S_T - K, 0)]$$

### Variance Reduction (Antithetic Variates)
To reduce Monte Carlo standard error, for every standard normal sample $Z_i$, the complementary variate $-Z_i$ is evaluated:
$$\tilde{V} = \frac{f(Z) + f(-Z)}{2}$$
This eliminates odd-order error terms and lowers estimator variance without adding additional random variable generation overhead.

### Greeks Calculation
Sensitivities are estimated using central finite-difference perturbations:
$$\Delta = \frac{\partial V}{\partial S} \approx \frac{V(S_0 + \epsilon) - V(S_0 - \epsilon)}{2\epsilon}$$
$$\mathcal{V} = \frac{\partial V}{\partial \sigma} \approx \frac{V(\sigma + \delta) - V(\sigma - \delta)}{2\delta}$$

## Validation & Results
Evaluated at parameters: $S_0 = 100$, $K = 105$, $T = 1.0$, $r = 0.05$, $\sigma = 0.20$:

| Metric | Black-Scholes Analytical | Monte Carlo ($10^6$ paths) | Std Error |
|---|---|---|---|
| Call Price | 8.0214 | 8.0209 | 9.87e-05 |
| Delta ($\Delta$) | 0.5248 | 0.5251 | — |
| Vega ($\mathcal{V}$) | 37.5240 | 37.5312 | — |

## Repository Layout
```text
├── src/
│   ├── black_scholes.py   # Analytical BSM formulas & Greeks
│   ├── engine.py          # Vectorized GBM simulator with antithetic sampling
│   └── greeks.py          # Central finite difference numerical estimators
├── main.py                # Driver script running benchmarks and convergence checks
├── requirements.txt       # Dependency specifications
└── README.md              # Technical documentation and mathematical proof
