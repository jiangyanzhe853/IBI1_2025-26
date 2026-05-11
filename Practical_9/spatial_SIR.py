# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# define parameters
beta = 0.3
gamma = 0.05

# create 100 x 100 population array
# 0 = susceptible
# 1 = infected
# 2 = recovered
population = np.zeros((100, 100))

# randomly select one infected individual
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# plot initial outbreak
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Initial Outbreak')
plt.colorbar(label='State')
plt.show()

# -------------------------------------------------------------------
# PSEUDOCODE
# -------------------------------------------------------------------
# For each time point:
#   1. Find all infected cells in the population array
#   2. For every infected cell:
#       a. Check all 8 neighbouring cells
#       b. If neighbour is susceptible:
#           - infect neighbour with probability beta
#       c. Allow infected cell to recover with probability gamma
#   3. Update the population array
#   4. Plot the population heat map
# -------------------------------------------------------------------

# simulate disease spread for 100 time points
for t in range(100):

    # copy current population so updates do not interfere immediately
    new_population = population.copy()

    # find infected cells
    infected_cells = np.where(population == 1)

    # loop through infected cells
    for i, j in zip(infected_cells[0], infected_cells[1]):

        # check all neighbouring cells
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:

                # skip the centre cell itself
                if dx == 0 and dy == 0:
                    continue

                # calculate neighbour coordinates
                nx = i + dx
                ny = j + dy

                # ensure neighbour is inside array boundaries
                if 0 <= nx < 100 and 0 <= ny < 100:

                    # infect susceptible neighbours
                    if population[nx, ny] == 0:
                        if np.random.random() < beta:
                            new_population[nx, ny] = 1

        # allow infected individual to recover
        if np.random.random() < gamma:
            new_population[i, j] = 2

    # update population
    population = new_population.copy()

    # plot progression
    plt.figure(figsize=(5, 5), dpi=120)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f'Spatial SIR Model - Time {t + 1}')
    plt.colorbar(label='State')
    plt.pause(0.05)
    plt.show(block=False)

plt.show()