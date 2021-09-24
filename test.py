import numpy.random as rnd
import matplotlib.pyplot as plt


s = [rnd.random_integers(6) for i in range(200)]
f = [rnd.randint(6) for i in range(200)]
p = [rnd.random()*6 for i in range(200)]
print(s,"\n",f)
plt.hist(s, density=True)
plt.hist(f, density=True)
plt.hist(p, density=True)
#plt.plot(bins, linewidth=2, color='r')

plt.show()