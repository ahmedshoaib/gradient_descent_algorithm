The code implements the Incremental GDA as well as Batch mode GDA for the polynomial curve fitting problem 
for any number of features with the format of input files as given below.



Format of input files : 
	input file for training data :
		first line : weights
		following lines : training data 
		Eg:
		W0 W1 W2 ..... Wn
		X1 X2 X3 ....Xn Y
		X1 X2 X3 ....Xn Y
		X1 X2 X3 ....Xn Y
		X1 X2 X3 ....Xn Y
		
	test file : 
	test samples
	Eg:
		X1 X2 X3 ...... Xn
		X1 X2 X3 ...... Xn
		X1 X2 X3 ...... Xn
		X1 X2 X3 ...... Xn
		X1 X2 X3 ...... Xn


