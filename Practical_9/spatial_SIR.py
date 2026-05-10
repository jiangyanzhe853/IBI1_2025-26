import numpy as np
import matplotlib.pyplot as plt

# population grid
population = np.zeros((100,100))

# random outbreak
outbreak = np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]] = 1

# parameters
beta = 0.3
gamma = 0.05
for t in range(50):

    # find infected cells
    infected_positions = np.where(population == 1)

    new_population = population.copy()

    for x,y in zip(infected_positions[0], infected_positions[1]):

        # check neighbours
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:

                nx = x + dx
                ny = y + dy

                # skip itself
                if dx == 0 and dy == 0:
                    continue

                # boundary check
                if nx < 0 or nx >= 100 or ny < 0 or ny >= 100:
                    continue

                # infect susceptible neighbour
                if population[nx,ny] == 0:
                    if np.random.random() < beta:
                        new_population[nx,ny] = 1

        # recovery
        if np.random.random() < gamma:
            new_population[x,y] = 2

    population = new_population

# plot heatmap
plt.figure(figsize=(5,5))
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title(f"time = {t}")
plt.colorbar()
plt.show()