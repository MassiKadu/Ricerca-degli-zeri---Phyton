import matplotlib.pyplot as plt
import numpy as np
import math
import simpy as sp

x = np.linspace(-10,10)

funzione1 = input('Dammi la funzione: ')

inizio = input("Dammi l'inizio del range: ")
fine = input("Dammi la fine del range: ")
inizio = eval(inizio)
fine = eval(fine)

def f1(x):
    global funzione1
    return eval(funzione1)


y1 = f1(x)
# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.title(funzione1)
plt.ylim([-10,10])
plt.axvline(0, c='black', ls='--')
plt.axhline(0, c='black', ls='--')

# plot the function
plt.plot(x,y1, 'r')
plt.scatter(inizio,0, marker='o')
plt.scatter(fine,0, marker='o')
#plt.plot(x,y2, 'r', color='blue')

A = f1(inizio)
B = f1(fine)
x0 = inizio

x_values = [inizio, fine]
y_values = [A, B]

n = input("Dimmi quante volte ripetere: ")
n = eval(n)+1
nDecimali = input("Inserire numero di cifre dopo la virgola: ")

i = 1
valori = {}
valori[0] = x0

valoriX = {}
valoriX[0] = x_values

valoriY = {}
valoriY[0] = y_values

while i<n:
    key = i
    value = valori[key-1] - (((fine-valori[key-1])/(f1(fine)-f1(valori[key-1])))*f1(valori[key-1]))
    valori[key] = value
    valoriX[key] = [value,fine]
    valoriY[key] = [f1(value),f1(fine)]
    plt.scatter(value,0,marker='o')
    i+=1

for i in range(n):
    print("X"+str(i)+": "+str("{:.{}f}".format(valori[i],nDecimali)))
    plt.plot(valoriX[i],valoriY[i])

plt.plot()

# show the plot
plt.show()

