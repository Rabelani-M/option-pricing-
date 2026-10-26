from .engine import price_european_option

def estimate_delta(S0, K, T, r, sigma, dS=1e-3, n_paths=500_000, option_type="call"):
    p_up, _ = price_european_option(S0 + dS, K, T, r, sigma, n_paths=n_paths, option_type=option_type)
    p_dn, _ = price_european_option(S0 - dS, K, T, r, sigma, n_paths=n_paths, option_type=option_type)
    return (p_up - p_dn) / (2.0 * dS)

def estimate_vega(S0, K, T, r, sigma, d_sigma=1e-3, n_paths=500_000, option_type="call"):
    p_up, _ = price_european_option(S0, K, T, r, sigma + d_sigma, n_paths=n_paths, option_type=option_type)
    p_dn, _ = price_european_option(S0, K, T, r, sigma - d_sigma, n_paths=n_paths, option_type=option_type)
    return (p_up - p_dn) / (2.0 * d_sigma)
