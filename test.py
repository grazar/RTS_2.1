import matplotlib.pyplot as plt
from math import *
from cmath import exp, pi
from random import *
from time import time

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

    plt.subplot(221)
    plt.ylabel('real')
    plt.plot(Fr)
    plt.subplot(222)
    plt.ylabel('image')
    plt.plot(Fi)

    plt.savefig("plot.png")

print(end - start)
