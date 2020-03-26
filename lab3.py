import numpy as np
import random as rnd
import matplotlib.pyplot as plt


def create_harmon():
    harmon = [0 for _ in range(vidlik_number)]
    for i in range(number_of_harmonics):
        A = rnd.uniform(min_number, max_number)
        Fi = rnd.uniform(min_number, max_number)
        for t in range(vidlik_number):
            harmon[t] += A*np.sin(frequency/number_of_harmonics*t*i + Fi)
    return harmon


def get_Fourier(x):
    N = len(x)
    FReal = []
    Fimagine = []
    for p in range(N):
        FReal.append(0)
        Fimagine.append(0)
        for k in range(N):
            FReal[p] += x[k]*np.cos(-2*np.pi*p*k/N)
            Fimagine[p] += x[k]*np.sin(-2*np.pi*p*k/N)
    return FReal, Fimagine

number_of_harmonics = 10
vidlik_number = 256
frequency = 1500
min_number = 0
max_number = 1

x_t = create_harmon()

(FR, Fi) = get_Fourier(x_t)

plt.plot(range(vidlik_number), FR, label='FReal')
plt.plot(range(vidlik_number), Fi, label='Rimagine')
plt.legend()
plt.show()
