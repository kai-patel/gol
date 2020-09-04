import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import random

cells = np.array([[random.randint(0, 0) for _ in range(16)] for _ in range(16)])

cells[6][6] = 1
cells[7][6] = 1
cells[8][6] = 1

fig = plt.figure()
ax = plt.axes()
plot = plt.matshow(cells, fignum=0)

def iterate(a):
    print(a)
    currentCells = cells.copy()
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            cells[i][j] = checkRules(i, j, currentCells)
    plot.set_data(cells)
    return [plot]


def getNeighbours(i, j, cells):
    total = 0
    minH, maxH = 0, len(cells[i]) - 1
    minV, maxV = 0, len(cells) - 1

    for v in range(i-1, i+2):
        for h in range(j-1, j+2):
            if minH <= h <= maxH and minV <= v <= maxV:
                    if not (v == i and h == j):
                        #print(f"Checking neighbour for ({i}, {j}) at ({v}, {h})")
                        if cells[v][h] == 1:
                            #print(f"Cell ({v}, {h}) is on and next to ({i}, {j})")
                            total += 1
                        
    return total

def checkRules(i, j, cells):
    cell = cells[i][j]
    neighbours = getNeighbours(i, j, cells)
    if cell == 1:
        if neighbours < 2:
            cell = 0
        if neighbours == 2 or neighbours == 3:
            cell = 1
        if neighbours > 3:
            cell = 0
    else:
        if neighbours == 3:
            cell = 1
    return cell


anim = animation.FuncAnimation(fig, iterate, interval=100, frames=200, blit=True)
#iterate(1)
plt.show()