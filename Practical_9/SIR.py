# import libraries
import numpy as np
import matplotlib.pyplot as plt

# initial population
N = 10000
S = 9999
I = 1
R = 0

# parameters
beta = 0.3
gamma = 0.05

# arrays to record results
S_list = [S]
I_list = [I]
R_list = [R]

# time loop
for t in range(1000):

    # infection probability
    infection_prob = beta * (I / N)

    # how many susceptible become infected
    new_infections = np.sum(np.random.choice([0,1], S, p=[1-infection_prob, infection_prob]))

    # how many infected recover
    new_recoveries = np.sum(np.random.choice([0,1], I, p=[1-gamma, gamma]))

    # update numbers
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries

    # record values
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# plot
plt.figure(figsize=(6,4), dpi=150)

plt.plot(S_list, label="Susceptible")
plt.plot(I_list, label="Infected")
plt.plot(R_list, label="Recovered")

plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Stochastic SIR Model")

plt.legend()
plt.savefig("/Users/juanxincai/IBI/IBI1_2025-26/Practical_9/SIR_plot.png")
plt.show()
