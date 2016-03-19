from Matrix_cal import *

#******************************************************

with open('train_list','r') as f:
	# read all lines in file as a list
	# each element in the list represent a line in string form
	train_list = f.read().splitlines()

output_trained_matrix(train_list)

print ("Training Complete.")


