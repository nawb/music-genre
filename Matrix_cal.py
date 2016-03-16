import numpy as np

def print_matrix(matrix):
	for ele in matrix:
		print(ele)

def read_file(file_name):
	with open('dataset/'+file_name,'r') as f:
		# read all lines in file as a list
		# each element in the list represent a line in string form
		lines = f.read().splitlines()	

	lines.pop(0)	# delete the first comment line in file

	m = len(lines)	# number of rows
	n = len(lines[0].split(','))	# number of columns

	for i in range(m):
		lines[i] = lines[i].split(',')	# convert string form into list form
		for j in range(n):
			lines[i][j] = float(lines[i][j])	# convert each element in the list into float form
	return lines
'''
def combine_file(file_list):
	result = []
	with open(file_list, 'r') as l:
		# file_name is a list, in which each element is a file name in string form
		file_name = l.read().splitlines()

	for name in file_name:
		feature_matrix = read_file(name)	# get the feature matrix for each song

	for vector in feature_matrix:
		result.append(vector)		# combine the feature matrix of all the songs into result

	return result
'''

def get_mean_vector(matrix):	# should input transposed feature matrix
	m = len(matrix[0])	#number of columns of transposed feature matrix
	n = len(matrix)		#number of rows of transposed feature matrix
	return [(sum(matrix[i]) / m) for i in range(n)]		#compute mean vector

def get_UNLL(test_feature, mean_vector, cov_matrix_inversed):
	result = []
	for test_feature_vector in test_feature:
		sub = np.subtract(test_feature_vector, mean_vector)
		sub_transposed = list(zip(sub))
		# result contains UNLL for each vector in test song feature matrix
		result.append(np.dot(np.dot(sub, cov_matrix_inversed),sub_transposed))
	
	return(np.mean(result))

def output_trained_matrix(file_list):
	for song_name in file_list:
		feature_matrix_classical = read_file(song_name)
		feature_transpose_classical = list(zip(*feature_matrix_classical))		#get transposed feature matrix

		# compute mean vector and covariance matrix

		mean_vector_classical = get_mean_vector(feature_transpose_classical)

		# compute the covariance matrix of feature matrix using module numpy
		covariance_matrix = np.cov(feature_transpose_classical)	
		# compute the inverse of cov matrix
		covariance_matrix_inversed = np.linalg.inv(covariance_matrix)

		for i in range(len(mean_vector_classical)):
			mean_vector_classical[i] = str(mean_vector_classical[i])

		covariance_matrix_inversed = list(covariance_matrix_inversed)
		for i in range(len(covariance_matrix_inversed)):
			covariance_matrix_inversed[i] = list(covariance_matrix_inversed[i])
			for j in range(len(covariance_matrix_inversed[i])):
				covariance_matrix_inversed[i][j] = str(covariance_matrix_inversed[i][j])

		my_file = open('dataset/'+song_name+'_matrixes', 'w')

		my_file.write("The first line is mean vector, the rest are inversed covariance matrix." + '\n')
		my_file.write(','.join(mean_vector_classical) + '\n')

		for item in covariance_matrix_inversed:
			my_file.write(','.join(item) + '\n')

		my_file.close()






