import numpy as np

def foam(z):
    total = 0
    for i in range(len(z)):
        for j in range(len(z)):
            if i != j:
                total += np.linalg.norm(z[i] - z[j])**2
    return total

def grad(z):
    g = np.zeros_like(z)
    for i in range(len(z)):
        for j in range(len(z)):
            if i != j:
                g[i] += (z[i] - z[j])
    return g
