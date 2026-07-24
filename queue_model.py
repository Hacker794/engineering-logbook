import random

### 
# 
# THE REAL PROBLEM:
# 
# BUILDING THE QUEUE
# 
# - Shoppers arrive at some rate (e.g., 1 shopper every 2 minutes)
# 
# - A till serves at some rate (e.g., 1 shopper every 3 minutes)
# 
# - if the till is busy, the shopper waits in a queue
# 
# - we want to measure the average wait time for each shopper in the system
# 
# ###

# Implementing the M/M/1 formula for the average wait time in a queueing system
# If arrivals meet or exceed service rate, the system becomes unstable and the average wait time approaches infinity.

def theoretical_wait(lam, mu):
    """M/M/1 average time in system (minutes)."""
    if lam >= mu:
        return float('inf') # queue explodes
    return 1 / (mu - lam)

# Simulating thousands of shoppers with a random exponential distribution for arrival gapsand service times. Also simulating the average time spent in system

def simulate(lam, mu, customers=1000000):
    t = till_free = total = 0.0
    for _ in range(customers):
        t += random.expovariate(lam) # next arrival
        start = max(t, till_free) # wait for the till
        till_free = start + random.expovariate(mu)
        total += till_free - t # time in system
    return total / customers

# Proving the maths
# We will now run a simulation across a range of arrival rates and compare the theoretical and simulated average wait times. They should agree closely if the model is correct.

for lam in [1.0, 1.4, 1.6, 1.8, 1.9]:
    print(lam, round(theoretical_wait(lam, 2), 2), round(simulate(lam, 2), 2))


# line break

print()


# Queue Model no.2 for when there are 2 tills. The average wait time is now halved, as there are 2 tills to serve the shoppers.
# M/M/2 queueing system. 

# Theoretical average wait time in system for M/M/2 queueing system. The formula is more complex than M/M/1, but can be derived from the birth-death process.

def theoretical_wait_mm2(lam, mu):
    """M/M/2 average time in system (minutes)."""
    if lam >= 2 * mu:
        return float("inf")
    rho = lam / (2 * mu)
    a = lam / mu
    p0 = 1 / (
        1
        + a
        + (a ** 2) / (2 * (1 - rho))
    )
    lq = (
        p0 * (a ** 2) * rho
    ) / (
        2 * (1 - rho) ** 2
    )
    wq = lq / lam
    return wq + (1 / mu)
    
# Simulating a lot of shoppers with a random exponential distribution for arrival gaps and service times. Also simulating the average time spent in system

def simulate_mm2(lam, mu, customers=1000000):

    t = 0.0
    total = 0.0

    till1_free = 0.0
    till2_free = 0.0

    for _ in range(customers):

        t += random.expovariate(lam)

        if till1_free <= till2_free:
            start = max(t, till1_free)
            till1_free = start + random.expovariate(mu)
            total += till1_free - t

        else:
            start = max(t, till2_free)
            till2_free = start + random.expovariate(mu)
            total += till2_free - t

    return total / customers

#Call the function:

for lam in [1.0, 1.4, 1.6, 1.8, 1.9]:
    print(lam, round(theoretical_wait_mm2(lam, 2), 2), round(simulate_mm2(lam, 2), 2))

# Fits model to data. This is a simple linear regression model that fits the theoretical wait time to the simulated wait time. The model is then used to predict the average wait time for a given arrival rate.