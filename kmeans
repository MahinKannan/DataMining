import numpy as np
import os
import matplotlib.pyplot as plt

#mean and covariance
u1 = np.float32([1, 0])
u2 = np.float32([0, 1.5])
cov1 = np.float32([[0.9, 0.4],[0.4, 0.9]])
cov2 = np.float32([[0.9, 0.4],[0.4, 0.9]])

x1, y1 = np.random.multivariate_normal(u1, cov1, 500).T
x2, y2 = np.random.multivariate_normal(u2, cov2, 500).T
#Create one 2D list of 1000 points
x = np.concatenate((x1, x2))
y = np.concatenate((y1, y2))

plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.scatter(x, y, color = "green", marker = "*", s = 30, label = "Generated data")  
#plt.show()
x = x[np.newaxis]
y = y[np.newaxis]

#Holds the (x, y)
X = np.concatenate((x, y), axis = 0).T
os.system('clear')

def mykmeans(X, k, c = 0):
	"""
		k = number of clusters
		c = center values
		X is the points list we create above
	"""
	exit_flag = 0
	min_dist_point_to_clustCent = 0
	initial_center = np.empty([k, 2])
	if not np.any(c):
		for i in range(k):		#initialize center if not given by user
			initial_center[i][0] = np.random.randn()
			initial_center[i][1] = np.random.randn()
	else:
		initial_center = c
	print("\nInitial cluster centers:")
	for i in range(k):
		print(f"Cluster {i + 1} center: x = {initial_center[i][0]} y = {initial_center[i][1]}")
	for iteration in range(10000):
		min_dist_point_to_clustCent = 0
		w, h = len(initial_center), len(X)
		distance_matrix = np.empty([h, w])
		for i in range(h):
			for j in range(w):		#calculate distance between centers and points
				distance_matrix[i][j] = np.sqrt((X[i][0] - initial_center[j][0])**2 
					+ (X[i][1] - initial_center[j][1])**2)

			#get the closest cluster to the point
			min_dist_point_to_clustCent = np.float32(np.where(distance_matrix[i] 
				== min(distance_matrix[i])))       
			min_dist_point_to_clustCent = min_dist_point_to_clustCent.item()
			for j in range(w):
				if min_dist_point_to_clustCent != j:
					distance_matrix[i][j] = 0
		cluster_center = np.zeros([k, 2])
		count_for_each_center_to_normalize = np.zeros(k)

		#calculate mean among all clusters for the update process
		for i in range(len(distance_matrix)):                  
			for j in range(len(initial_center)):
				if distance_matrix[i][j] != 0:
					cluster_center[j][0] = cluster_center[j][0] + X[i][0]
					cluster_center[j][1] = cluster_center[j][1] + X[i][1]
					count_for_each_center_to_normalize[j] += 1
		for i in range(k):
			cluster_center[i] = cluster_center[i] / count_for_each_center_to_normalize[i]
		for i in range(len(initial_center)):		#check for exit condition
			n0 = np.absolute(np.linalg.norm(initial_center[i]) 
				- np.linalg.norm(cluster_center[i]))
			if n0 <= 0.001:
				exit_flag = 1
				break
		if exit_flag == 1:
			break
		initial_center = np.copy(cluster_center)			#update the centers
	print(f"\nTotal number of iterations: {iteration + 1}")
	return cluster_center


k = int(input("Enter number of clusters :"))
option = input("Define center values? (yes or no) : ")
if option.lower() == 'y' or option.lower() == 'yes':
	c = np.empty([k, 2]) 
	print("{Input format: x-coordinate [space] y-coordinate}")
	for i in range(k):
		h1, h2 = input(f"Enter x and y for center {i + 1} :").split()
		c[i][0] = h1
		c[i][1] = h2
else:
	print("Random initialization chosen.")
	c = 0
cluster = mykmeans(X, k, c)

print("\nFinal cluster centers.")
for i in range(k):
	print(f"Cluster {i + 1} center: x = {cluster[i][0]}  y = {cluster[i][1]}")
plt.scatter(cluster[:, 0], cluster[:, 1], color = "red", marker = "+", 
	s = 200, label = "Cluster Center")
plt.legend()  
plt.show()
