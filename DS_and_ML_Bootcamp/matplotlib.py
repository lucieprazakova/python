import matplotlib.pyplot as plt

# %matplotlib inline # for JupyterNotebook to show plots
plt.show() # other
 
import numpy as np
x = np.linspace(0,5,11)
y = x **2
x
y


## Functional method
plt.plot(x,y)
plt.show()


# How to add titles and adjust the line
plt.plot(x,y,'g-') # green line
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()


#
plt.subplot(1,2,1) # nb of rows, columns and nb of plot reffering to
plt.plot(x,y,'r-') # red line
plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()


## OO (Object oriented method)
fig = plt.figure() # blank canvas
axes = fig.add_axes([0.1,0.1,0.8,0.9]) # left, bottom, width, height
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')
plt.show()

#
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3]) # % # left, bottom, width, height
axes1.set_xlabel('X Label')
axes1.set_ylabel('Y Label')
axes1.set_title('Larger plot')
axes1.plot(x,y)
axes2.plot(y,x)
axes2.set_title('Smaller plot')
plt.show()


#
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,y)
plt.show()

