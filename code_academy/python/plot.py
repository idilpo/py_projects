from matplotlib import pyplot as plt
import random

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12) #chooses a sample of 12 numbers

plt.plot(numbers_a, numbers_b)
plt.show()