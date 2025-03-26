square = []
for i in range(100):
    square.append(i*i)

x = list(range(100))

import matplotlib.pyplot as plt

plt.plot(x,square)

plt.show()

