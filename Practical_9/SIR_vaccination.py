import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05

vaccination_rates = range(0,101,10)

plt.figure(figsize=(6,4), dpi=150)

for v in vaccination_rates:

    vaccinated = int((N-1)* v / 100)

    S = N - vaccinated - 1
    I = 1
    R = 0

    S_list = [S]
    I_list = [I]
    R_list = [R]

    for t in range(1000):

        infection_prob = beta * (I / N)

        new_infections = np.sum(np.random.choice([0,1], S, p=[1-infection_prob, infection_prob]))
        new_recoveries = np.sum(np.random.choice([0,1], I, p=[1-gamma, gamma]))

        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries

        S_list.append(S)
        I_list.append(I)
        R_list.append(R)

    plt.plot(I_list, label=f"{v}% vaccinated")

plt.xlabel("Time")
plt.ylabel("Infected population")
plt.title("Effect of vaccination")

plt.legend()
plt.savefig("/Users/juanxincai/IBI/IBI1_2025-26/Practical_9/SIR_vaccination_plot.png")
plt.show()