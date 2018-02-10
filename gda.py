
#please read the README.TXT file for format of input file(training data) and test file(containing test cases)

def expected_value(w,x):        #find H(X) for given weight array - w and X array -x
	i = 0
	h = 0
	for constant in w:
		if (i == 0):
			h += float(constant)
		else : 
			h += float(constant)*float(x[i-1])
		i += 1
	return h
def incremental(alpha):      #implements incremental GDA approach
	
	threshold = float(input("Enter the max. tolerable change in cost function:\n"))
	delta = 0.0
	flag = 0
	feature_count = 0
	constants = []
	training_data = []
	inp = input("enter training file name :\n")
	input_file = open(inp,'r')
	print("Training ...\n")
	for line in input_file:                    #extracting training data from input file
		word = line.split()
		if(flag == 0):
			flag = 1;
			feature_count = len(word)
			constants = word
		else :
			training_data.append(word)
	
	while(1):                       #running training steps until del(J) reaches a threshold
		
		print("last delta : ",delta)
		count = 0
		for sample in training_data:                      #for each sample set in training data
			h = expected_value(constants,sample)
			err = float(sample[feature_count - 1]) - h
			i = 0
			flag = 0                           #flag used for X0 as X0 is always 1
			for w in constants:             #for each w
				weight = float(w)
				if(flag == 0):
					weight = weight + alpha*err          #update the weights
					constants[0] = str(weight)
					flag = 1
				else:
					weight = weight + alpha*err*float(sample[i])
					i += 1
					constants[i] = str(weight)
			count +=1
			delta = (err*err) + delta                 #keep record of (Y-H(X)) for calculation of Cost Function change
			if(count == feature_count) : break
			
		delta = delta*0.5
		if(delta <= threshold):
			break
	print("Training done.\n")
	test_file = open(input("enter test file name :\n"),'r')   #give a test file for testing
	
	for line in test_file:
		feat = line.split()
		i = 0
		out = 0
		flag = 0 
		for omega in constants:
			if(flag == 0):
				out = out + float(omega)
				flag = 1
			else :
				out = out + float(omega)*float(feat[i])
				i+=1
	
		print("Output : ",out)
		

		
def batch(alpha):
	
	threshold = float(input("Enter the max. tolerable change in cost function:\n"))
	delta = 0.0
	flag = 0
	step_count = 0
	feature_count = 0   #count of no of features
	constants = []
	training_data = []
	inp = input("enter training file name :\n")
	input_file = open(inp,'r')
	print("Training ...\n")
	for line in input_file:
		word = line.split()
		if(flag == 0):
			flag = 1;
			feature_count = len(word)
			constants = word                 # assigning one line to constants list
		else :
			training_data.append(word)     #assigning training data to training_data list.
	
	while(1):      	#for training steps
		j = 0                                         #j represents Wj
		print("running step : \n",step_count)
		print("last delta : ",delta)
		big = 0 
		
		for w in constants:                  #for each W
			weight = float(w)

			sum = 0
			if(j == 0):                 #for first W i.e W0
				for sample in training_data:             #for corresponding X values to the W
					h = expected_value(constants,sample)
					err = float(sample[feature_count - 1]) - h
					sum = sum + err*1
				
			else:     #for rest of Ws
			
				for sample in training_data:      #for corresponding X values to the W
					h = expected_value(constants,sample)
					err = float(sample[feature_count - 1]) - h
					sum = sum + err*float(sample[j-1])            #calculate (Y-H(X))*Xj
				
			weight = weight + alpha*sum              #update weight
			constants[j] = str(weight)
			j += 1         #go to next W
		for sample in training_data:         #for the cost function
			h = expected_value(constants,sample)
			err = float(sample[feature_count - 1]) - h
			big = big + err*err
		delta = big/2
			
			
		step_count += 1     
		if(delta <= threshold):       
			break
		

		
	print("Training done.\n")
	test_file = open(input("enter test file name :\n"),'r')
	
	for line in test_file:
		feat = line.split()
		i = 0
		out = 0
		flag = 0 
		for omega in constants:
			if(flag == 0):
				out = out + float(omega)
				flag = 1
			else :
				out = out + float(omega)*float(feat[i])
				i+=1
	
		print("Output : ",out)

	
		
import sys
alpha  = float(input("Enter learning rate : "))   #  (10e-5 for batch mode test input is good)(0.0001 for incremental mode is good)
if (alpha <= 1 and alpha > 0):

	mode = int(input("Enter mode number : \n1. Incremental\n2. Batch\n"))
	if (mode == 1 or mode == 2) :
		if (mode == 1 ):
			
			incremental(alpha)
		if (mode == 2):
			batch(alpha)
	else :
		print("Invalid option")
else:
	print("Wrong learning rate ")
	
	

