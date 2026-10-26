import numpy as np

def simulate_terminal_prices(S0, r, sigma, T, n_paths, use_antithetic=True, seed=None):
    if seed is not None:
        np.random.seed(seed)

    if use_antithetic:
        half_paths = n_paths // 2
        Z = np.random.standard_normal(half_paths)
        Z = np.concatenate([Z, -Z])
    else:
        Z = np.random.standard_normal(n_paths)

    drift = (r - 0.5 * sigma**2) * T
    diffusion = sigma * np.sqrt(T) * Z
    return S0 * np.exp(drift + diffusion)

def price_european_option(S0, K, T, r, sigma, n_paths=1_000_000, option_type="call", use_antithetic=True):
    ST = simulate_terminal_prices(S0, r, sigma, T, n_paths, use_antithetic=use_antithetic)
    if option_type.lower() == "call":
        payoffs = np.maximum(ST - K, 0.0)
    elif option_type.lower() == "put":
        payoffs = np.maximum(K - ST, 0.0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    discount = np.exp(-r * T)
    price = discount * np.mean(payoffs)
    std_err = discount * (np.std(payoffs) / np.sqrt(len(payoffs)))
    return price, std_err
