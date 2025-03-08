import random

def cesium_measurement(n0, estimated_decay, elapse_between_measurements, env_factor_min, env_factor_max, t):
    N_t = [n0]
    for _ in t:
        theoretical_decay = estimated_decay * elapse_between_measurements
        actual_measurement = theoretical_decay * random.uniform(env_factor_min, env_factor_max)
        N_t.append(N_t[-1] * (1 - actual_measurement))
    N_t.pop(0)
    return N_t
