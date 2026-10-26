from src.black_scholes import black_scholes_price, black_scholes_delta, black_scholes_vega
from src.engine import price_european_option
from src.greeks import estimate_delta, estimate_vega

if __name__ == "__main__":
    S0, K, T, r, sigma = 100.0, 105.0, 1.0, 0.05, 0.20
    print(f"Parameters: S0={S0}, K={K}, T={T}, r={r}, sigma={sigma}\n")

    # Closed-form benchmarks
    bs_call = black_scholes_price(S0, K, T, r, sigma, "call")
    bs_delta = black_scholes_delta(S0, K, T, r, sigma, "call")
    bs_vega = black_scholes_vega(S0, K, T, r, sigma)

    # Monte Carlo estimates
    mc_call, mc_se = price_european_option(S0, K, T, r, sigma, n_paths=1_000_000, use_antithetic=True)
    mc_delta = estimate_delta(S0, K, T, r, sigma, n_paths=500_000)
    mc_vega = estimate_vega(S0, K, T, r, sigma, n_paths=500_000)

    print(f"{'Metric':<15} {'Black-Scholes':<15} {'Monte Carlo':<15} {'Std Error':<10}")
    print("-" * 55)
    print(f"{'Call Price':<15} {bs_call:<15.4f} {mc_call:<15.4f} {mc_se:<10.4e}")
    print(f"{'Delta':<15} {bs_delta:<15.4f} {mc_delta:<15.4f} {'-':<10}")
    print(f"{'Vega':<15} {bs_vega:<15.4f} {mc_vega:<15.4f} {'-':<10}")
