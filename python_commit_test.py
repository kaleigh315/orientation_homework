import numpy as np
import matplotlib.pyplot as plt

normal_data = []
for i in range (0, 25):
    normal_data.append(np.random.normal(5, .3))
plt.hist(normal_data, bins = 10)
plt.show()

uniform_data = []
for i in range (0, 25):
    uniform_data.append(np.random.uniform(0,1))
plt.hist(uniform_data, bins = 10)
plt.show()

poisson_data = []
for i in range (0, 25):
    poisson_data.append(np.random.poisson(3))
plt.hist(poisson_data, bins = 10)
plt.show()