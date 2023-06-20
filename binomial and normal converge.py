<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
normal_data = []
small_binomial_dataset = []
large_binomial_dataset = []
for i in range (0, 1000):
    normal_data.append(np.random.normal(5, .3))
    large_binomial_dataset.append(np.random.binomial(5, .3))
for i in range (0, 100):
    small_binomial_dataset.append(np.random.binomial(5, .3))
y1 = normal_data
y2 = large_binomial_dataset
y3 = small_binomial_dataset
plt.hist(y1, bins = 5, label="Normal")
plt.hist(y2, bins = 5, label="Binomial with Large N")
plt.hist(y3, bins = 5, label="Binomial with Small N")
plt.legend(loc="upper left")
plt.show() #See that binomial with larger end is closer to a normal distribution
=======
import numpy as np
import matplotlib.pyplot as plt
normal_data = []
small_binomial_dataset = []
large_binomial_dataset = []
for i in range (0, 1000):
    normal_data.append(np.random.normal(5, .3))
    large_binomial_dataset.append(np.random.binomial(5, .3))
for i in range (0, 100):
    small_binomial_dataset.append(np.random.binomial(5, .3))
y1 = normal_data
y2 = large_binomial_dataset
y3 = small_binomial_dataset
plt.hist(y1, bins = 5, label="Normal")
plt.hist(y2, bins = 5, label="Binomial with Large N")
plt.hist(y3, bins = 5, label="Binomial with Small N")
plt.legend(loc="upper left")
plt.show() #See that binomial with larger end is closer to a normal distribution
>>>>>>> c304089b5f052ff2a069dc2423a0e5495771c070
