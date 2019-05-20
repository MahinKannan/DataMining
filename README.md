I might have implemented some parts wrongly (bad logic)/
I didn't really document anything. 



1. K-means
2. Kernel Density Estimation
3. Naive Bayes classifier (ROC implementation is wrong (commented))
4. Logistic Regression  (should be perfect)







________________________________________________________________________________
Running K-means
python [pname].py

Then,
Enter the values asked in the command prompt

Number of clusters: n
Define center values: yes (If you want to enter custom center coordinates)
......................no  (If you want random centers)

If you chose yes, enter the x and y values of the centers separated by a space for a center and hit enter.

Enter x and y for center 1 :  x-value y-value
Enter x and y for center 2 :  x-value y-value


________________________________________________________________________________
Running Kernel density

python [pname].py

Then,
Enter the values asked

Enter '1' for 1D Gaussian data or '2' for 2D data: 1 (for 1D Gaussian data)
...................................................2 (for 2D Gaussion data)	
Enter value for h: h (binsize)
_______________________________________________________________________________
Running Naive Bayes 

python [pname].py
_______________________________________________________________________________
Running logistic regression

For batch training
	python [pname].py batch
For online
	python [pname].py online


To change learning rate, open code and change it.


