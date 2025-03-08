from function_generator import cesium_measurement
import numpy as np
import datetime

simulations = 0
while True:
    try:
        simulations = int(input("How often should the simulation be run?\n> "))
        if simulations <= 0:
            print("Invalid input! Input must be > 0\n")
        else:
            break
    except ValueError:
        print("Invalid input! Input must be a whole number\n")

ESTIMATED_DECAY = 0.023
INITIAL_AMOUNT = 100
ENV_FACTOR_MAX = 4
ENV_FACTOR_MIN = 1.2
TIME_STEPS = np.linspace(0, 110, 4000)
ELAPSE_BETWEEN_MEASUREMENTS = TIME_STEPS[1] - TIME_STEPS[0]

def predicate(x):
    return x <= 10

def binary_search(measurements):
    low = 0
    high = len(measurements)
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if predicate(measurements[mid]):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result * ELAPSE_BETWEEN_MEASUREMENTS

years = []
start_time = datetime.datetime.now()
for i in range(simulations):
    measurements = cesium_measurement(
        INITIAL_AMOUNT,
        ESTIMATED_DECAY,
        ELAPSE_BETWEEN_MEASUREMENTS,
        ENV_FACTOR_MIN,
        ENV_FACTOR_MAX,
        TIME_STEPS
    )
    years.append(binary_search(measurements))

print("Habitability is reached after:")
print(f"avg:        {np.average(years)}")
print(f"med:        {np.median(years)}")
print(f"max:        {np.max(years)}")
print(f"min:        {np.min(years)}")
print(f"std-dev:    {np.std(years)}")
print(f"var:        {np.var(years)}")
