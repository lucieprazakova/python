import matplotlib.pyplot as plt

# %matplotlib inline # for JupyterNotebook to show plots

import numpy as np
x = np.linspace(0,5,11)
y = x **2
x
y

# Functional method
plt.plot(x,y)
plt.show()