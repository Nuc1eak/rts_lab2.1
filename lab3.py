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

def Tabl_method(x):  # Табличний метод
    N = len(x)
    w = []
    for i in range(N):
        if i < N//4:
            w.append((np.cos(-2*np.pi*i/N),
                      np.sin(-2*np.pi*i/N)))
        elif i < N//2:
            w.append((w[i-N//4][1],
                      -w[i-N//4][0]))
        else:
            w.append((-w[i-N//2][0], -w[i-N//2][1]))
    FR = []
    Fi = []
    for i in range(N):
        FR.append(sum([w[(i*j)%N][0]*x[j] for j in range(N)]))
        Fi.append(sum([w[(i*j)%N][1]*x[j] for j in range(N)]))
    return FR, Fi

number_of_harmonics = 10
vidlik_number = 256
frequency = 1500
min_number = 0
max_number = 1

x_t = create_harmon()

(FR, Fi) = get_Fourier(x_t)
(FR_tabl, Fi_tabl) = Tabl_method(x_t)

fig = plt.figure()

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)

ax_1.plot(range(vidlik_number), FR)
ax_2.plot(range(vidlik_number), Fi)
ax_3.plot(range(vidlik_number), FR_tabl)
ax_4.plot(range(vidlik_number), Fi_tabl)

ax_1.set(title='FR')
ax_2.set(title='Fi')
ax_3.set(title='FR_tabl')
ax_4.set(title='Fi_tabl')

plt.show()
