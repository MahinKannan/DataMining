import numpy as np
import os
import matplotlib.pyplot as plt 

option = int(input("Enter '1' for 1D Gaussian data or '2' for 2D data: "))
if option == 1:
	u1 = 5
	std1 = 1
	X = np.random.normal(u1, std1, 1000).T
elif option == 2:
	u1 = np.float32([1, 0])
	u2 = np.float32([0, 1.5])
	cov1 = np.float32([[0.9, 0.4], [0.4, 0.9]])
	cov2 = np.float32([[0.9, 0.4], [0.4, 0.9]])
	x1, y1 = np.random.multivariate_normal(u1, cov1, 500).T
	x2, y2 = np.random.multivariate_normal(u2, cov2, 500).T
	x = np.concatenate((x1, x2))
	y = np.concatenate((y1, y2))
	x = x[np.newaxis]
	y = y[np.newaxis]
	X = np.concatenate((x, y), axis=0).T
	#print(x)
else:
	print("Only 1 or 2")
	exit()
#os.system("clear")
h = float(input("Enter value for h (bin size [.1, 1, 5, 10]): "))

def mykde(X,h):
	x, step = np.linspace(-5, 5, num = 1000, retstep = True)  #For 1000 num, step is 0.01
	y, step = np.linspace(-5, 5, num = 1000, retstep = True)
	d = X.ndim								#number of dimensions
	if d == 1:								#for 1D
			px = []
			for i in range(len(x)):			#loop for each x
				summ = 0
				for j in range(len(X)):		#loop for each of the generated Gaussian data point
					k = (x[i] - X[j]) / h
					if abs(k) <= 0.5:
						k = 1
					else:
						k = 0
					summ = summ + k * (1 / h**d)
				final = summ / len(X)
				px.append(final)
			return px,x			
	elif d == 2:								#for 2D
			px = []
			py = []
			for i in range(len(x)):				
				sumx = 0
				sumy = 0
				for j in range(len(X)):
					ky = (y[i] - X[j][1]) / h
					kx = (x[i] - X[j][0]) / h
					if abs(kx) <= 0.5:
						kx = 1
					else:
						kx = 0
					if abs(ky) <= 0.5:
						ky = 1
					else:
						ky = 0
					sumx = sumx + kx * (1 / h**d)
					sumy = sumy + ky * (1 / h**d)
				finalx = sumx / len(X)
				finaly = sumy / len(X)
				px.append(finalx)
				py.append(finaly)
			c = list(set(zip(px,py)))
			#Plot stuff
			plt.xlabel('px') 
			plt.ylabel('py') 
			plt.scatter(px, py, color = "green", marker = "*", label = "px-py") 
			plt.legend()
			plt.show()
			plt.clf()
			plt.plot(x, px, color = "red", label = "x-px")
			plt.plot(y, py, color = "blue", label = "y-py")
			plt.xlabel('x / y')  
			plt.ylabel('px / py') 
			plt.legend()
			plt.show()
			exit()
	else:
		print("Only 1 or 2")
		exit()

px, x = mykde(X, h)
axes = plt.gca()
axes.set_ylim([0, max(px)])
plt.xlabel('discritized x ') 
plt.ylabel('px')
plt.bar(x, px) 
plt.show()

