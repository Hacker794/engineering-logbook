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

#Proving the maths
#We will now run a simulation across a range of arrival rates and compare the theoretical and simulated average wait times. They should agree closely if the model is correct.

for lam in [1.0, 1.4, 1.6, 1.8, 1.9]:
    print(lam, round(theoretical_wait(lam, 2), 2), round(simulate(lam, 2), 2))