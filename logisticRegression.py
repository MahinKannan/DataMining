import numpy as np
import os
import matplotlib.pyplot as plt 
import math
import sys
#np.random.seed(1444)
def sigmoid(x):
	k = lambda l : 1 / (1 + np.exp(-l))
	s = k(x)
	return s
u1 = np.float32([1, 0])
u2 = np.float32([0, 1.5])
cov1 = np.float32([[1, 0.75], [0.75, 1]])
cov2 = np.float32([[1, 0.75], [0.75, 1]])
c = [0, 1]
x1, y1 = np.random.multivariate_normal(u1, cov1, 500).T
x2, y2 = np.random.multivariate_normal(u2, cov2, 500).T
x = np.concatenate((x1, x2))
y = np.concatenate((y1, y2))
x = x[np.newaxis]
y = y[np.newaxis]
X = np.concatenate((x, y) , axis = 0).T
Y = np.repeat(c, 500)[np.newaxis].T
x1, y1 = np.random.multivariate_normal(u1, cov1, 500).T
x2, y2 = np.random.multivariate_normal(u2, cov2, 500).T
x = np.concatenate((x1, x2))
y = np.concatenate((y1, y2))
x = x[np.newaxis]
y = y[np.newaxis]
X_test = np.concatenate((x, y), axis = 0).T
Y_test = np.repeat(c, 500)
bias = 1												#bias
weights = np.random.rand(2)[np.newaxis].T 				#weights
###########################################################################################

lr = 0.1	# [1,0.1,0.01,0.001]			#########Learning rate here!!!!#########

###########################################################################################

counter = 0
total_iterations = 0
#print(weights)
loss_list = []
total_gradient_per_step_list = []
option = sys.argv[1]

if option == 'batch':
	while True:
		total_iterations += 1
		loss = 0
		net = np.dot(X, weights) + bias
		o = sigmoid(net)
		loss = -np.sum(Y * np.log(o + 1e-7) + (1 - Y) * np.log(1 - o + 1e-7))
		loss /= 1000
		loss_list.append(loss)
		gradient = np.multiply(o - Y, X)
		gradient = gradient.sum(axis = 0)[np.newaxis]
		gradient = (gradient / X.shape[0]).T
		total_gradient_per_step_list.append(np.sum(abs(gradient)))
		weights = weights - lr * gradient
		bias = bias - lr * sum(gradient)
		counter += 1
		if np.sum(abs(gradient)) < 0.001 or counter > 100000:
			break
	print(f"Counter = {counter}")
	print(f"New Weights:\n{weights}")
else:
	run = True
	total_iterations = 0
	inn = 0
	while run:
		inn = 0		
		for row, yval in zip(X, Y) :
			inn += 1
			total_iterations += 1
			net = np.dot(row, weights) + bias
			o = sigmoid(net)
			loss = -np.sum(yval * np.log(o + 1e-7) + (1 - yval) * np.log(1 - o + 1e-7))
			gradient = np.multiply(o - yval, row)
			loss_list.append(loss)
			total_gradient_per_step_list.append(np.sum(abs(gradient)))
			weights = weights - lr * (gradient[np.newaxis].T)
			bias = bias - lr * (sum(gradient))
			if np.sum(abs(gradient)) < 0.001 :
				run = False;break
		counter += 1		
		if counter > 100000:
			run=False;break
	print(f"Counter = {counter}")
	print(f"Inner count = {inn}")
	print(f"Total iterations = {total_iterations}")

test_set_class = sigmoid(np.dot(X_test, weights) + bias)
for i in range(len(test_set_class)):
	if test_set_class[i] >= 0.5:
		test_set_class[i] = 1
	else:
		test_set_class[i] = 0
tp = 0
tn = 0
fp = 0
fn = 0
for i in range(Y_test.shape[0]):
	if test_set_class[i] == 0 and Y_test[i] == 0:
		tp += 1
	elif test_set_class[i] == 1 and Y_test[i] == 1:
		tn += 1
	elif test_set_class[i] == 0 and Y_test[i] == 1:
		fp += 1
	else:
		fn += 1
acc = (tp + tn) / (tp + tn + fp + fn)
print(f"Accuracy = {acc}")

plt.scatter(X_test[Y_test == 0, 0], X_test[Y_test == 0, 1]
	, color = "green", marker = "*", s = 30, label = "Test data Class 0")  
plt.scatter(X_test[Y_test == 1, 0], X_test[Y_test == 1, 1]
	, color = "blue", marker = "+", s = 30, label = "Test data Class 1")  
plt.legend()
linex = [[min(X_test[:, 0]), max(X_test[:, 1])]]
liney = -(bias + np.multiply(weights[0], linex)) / weights[1]
plt.plot([linex[0][0], linex[0][1]], [liney[0][0], liney[0][1]])
plt.show()
plt.figure("iteration / loss")
plt.plot(range(total_iterations), loss_list)
plt.xlabel('iteration')
plt.ylabel('loss')
plt.show()
plt.figure("iteration / gradient")
plt.xlabel('iteration')
plt.ylabel('gradient')
plt.plot(range(total_iterations), total_gradient_per_step_list)
plt.show()
