import matplotlib.pyplot as plt
import numpy as np
from random import *
import cmath
from math import *
from time import *

w = 1500
N = 1024
n = 8
amp = uniform(0, 1)
sh = uniform(0, 1)
x = [0 for i in range(N)]

start = time()
for i in range(n):
    for j in range(0, N):
        x[j] += amp * sin(w / n * j * i + sh)
end = time()

Fr = list()
Fi = list()


for i in range(N):
    Fr.append(x[i] * cos(-2 * pi * i * i / N))
    Fi.append(x[i] * sin(-2 * pi * i * i / N))



if __name__ == "__main__":
    signal = list()

print(end - start)


#ТАБЛИЧНЫЙ МЕТОД .... 

def table(x):
    start = time()
    N = len(x)
    table = np.cos(2 * pi / N * np.linspace(0, N-1, N)) \
            -1j * np.sin(2 * pi / N * np.linspace(0, N-1, N))
    spectre = np.zeros(N, dtype=np.complex64)
    for p in range(N):
        indicies = np.linspace(0, N-1, N, dtype=np.int32) * p % N
        spectre[p] = np.dot(x, table[indicies])
    print(f"Execution MakeTable time: {time() - start}")
    return spectre

spectr = table(x)
polar_spectr = np.array(list(map(lambda x: cmath.polar(x), spectr)))
plt.ylabel('phase')
ampl = plt.plot(polar_spectr[:, 0])
plt.grid()
plt.savefig("amplitude.png")
plt.clf()
phase = plt.plot(polar_spectr[:, 1])
plt.ylabel('phase')
plt.grid()
plt.savefig("phase.png")

print(spectr)