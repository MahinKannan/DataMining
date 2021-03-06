import numpy as np
import os
import matplotlib.pyplot as plt 
import math
#np.random.seed(1234)
u1 = np.float32([1, 0])
u2 = np.float32([0, 1])
cov1 = np.float32([[1, 0.75], [0.75, 1]])
cov2 = np.float32([[1, 0.75], [0.75, 1]])
c = [0, 1]
x1, y1 = np.random.multivariate_normal(u1, cov1, 500).T
x2, y2 = np.random.multivariate_normal(u2, cov2, 500).T
x = np.concatenate((x1, x2))
y = np.concatenate((y1, y2))
x = x[np.newaxis]
y = y[np.newaxis]
X = np.concatenate((x, y), axis = 0).T
Y = np.repeat(c, 500)

#------------------------
#(700, 300)
#cc = [0]
#ccc = [1]
#l1 = np.repeat(cc, 700)
#l2 = np.repeat(ccc, 300)
#Y = np.concatenate((l1, l2))
#--------------------------

x1, y1 = np.random.multivariate_normal(u1, cov1, 500).T
x2, y2 = np.random.multivariate_normal(u2, cov2, 500).T
x = np.concatenate((x1, x2))
y = np.concatenate((y1, y2))
x = x[np.newaxis]
y = y[np.newaxis]
X_test = np.concatenate((x, y), axis = 0).T
Y_test = np.repeat(c, 500)
os.system('clear')
	#Plot for the generated points and test set.
#print(X, Y, X_test, Y_test)
#print(X_test[Y_test == 0, 0])
#plt.scatter(X_test[Y_test == 0, 0], X_test[Y_test == 0, 1]
#	, color = "green", marker = "*", s = 30, label = "Generated data")  
#plt.scatter(X_test[Y_test == 1, 0], X_test[Y_test == 1, 1]
#	, color = "blue", marker = "+", s = 30, label = "Generated data") 
#plt.show()

def npdf(x, m, s):
	return (1 / (math.sqrt(2 * math.pi * s * s) + 1e-6)
		* math.exp(-1 * math.pow((x - m), 2) / (2 * s * s + 1e-6)))

def naive(X, Y, X_test, Y_test):
	#print(X[Y == 0, 0])
	meanx0 = np.mean(X[Y == 0, 0], axis = 0)
	meany0 = np.mean(X[Y == 0, 1], axis = 0)
	meanx1 = np.mean(X[Y == 1, 0], axis = 0)
	meany1 = np.mean(X[Y == 1, 1], axis = 0)
	stdx0 = np.std(X[Y == 0, 0], axis = 0)
	stdy0 = np.std(X[Y == 0, 1], axis = 0)
	stdx1 = np.std(X[Y == 1, 0], axis = 0)
	stdy1 = np.std(X[Y == 1, 1], axis = 0)
	probclass0 = (Y == 0).sum() / ((Y == 0).sum() + (Y == 1).sum())
	probclass1 = (Y == 1).sum() / ((Y == 0).sum() + (Y == 1).sum())
	post = np.ones(shape = (X_test.shape[0], 2))		#Posterior probability
	for i in range(X_test.shape[0]):
			prod = np.float32([1, 1])
			prod[0] *= (npdf(X_test[i][0], meanx0, stdx0))
			prod[0] *= (npdf(X_test[i][1], meany0, stdy0))
			prod[0] *= (probclass0)
			prod[1] *= (npdf(X_test[i][0], meanx1, stdx1))
			prod[1] *= (npdf(X_test[i][1], meany1, stdy1))
			prod[1] *= (probclass1)
			Z = prod[0] + prod[1]
			prod = prod / (Z + 1e-6)
			post[i] = prod
	pred = np.argmax(post, axis = 1)					#Predicted
	err = (pred != Y_test).sum() / Y_test.shape[0]
	return (pred, post, err)

pred, post, err = naive(X, Y, X_test, Y_test)
tp = 0
tn = 0
fp = 0
fn = 0
tpr = []
fpr = []
for i in range(Y_test.shape[0]):
	if pred[i] == 0 and Y_test[i] == 0:
		tp += 1
	elif pred[i] == 1 and Y_test[i] == 1:
		tn += 1
	elif pred[i] == 0 and Y_test[i] == 1:
		fp += 1
	else:
		fn += 1
print("Confusion Matrix")
print("                                    Actual Class")
print("	                         Positive      Negative")
print(f"Predicted Class     Positive      TP:{tp}         FP:{fp}")
print(f"                    Negative      FN:{fn}         TN:{tn}")
acc = (tp + tn) / (tp + tn + fp + fn)			#Accuracy
print(f"Accuracy = {acc}")
print(f"Error = {1-acc}")
if tp + fn == 0:
	print("Recall = 0/undef (TP + FN = 0)")
else:
	print(f"Recall = {tp / (tp + fn)}")
if tp + fp == 0:
	print("Precision = 0/undef (TP + FP = 0)")
else:
	print(f"Precision = {tp / (tp + fp)}")
