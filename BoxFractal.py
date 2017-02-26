import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
 # class Fractal():
 	# def __init__(self):
 		# self.Matrix=np.matrix([1])


M=np.matrix([1])
for t in range(6):
	n=len(M)
	Z= np.zeros((n,n))
	MZ1=np.concatenate((M, Z, M), axis=1)
	MZ2=np.concatenate((Z, M, Z), axis=1)
	M=np.concatenate((MZ1, MZ2, MZ1), axis=0)

cmap= mpl.colors.ListedColormap(['black', 'white'])
bounds=[-.5,.5,1.5]
norm=mpl.colors.BoundaryNorm(bounds, cmap.N)
img=plt.imshow(M, cmap=cmap, norm=norm)
plt.show()