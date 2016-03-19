from Matrix_cal import *
import sys
#**********************************************************************
if len(sys.argv) == 1:
                print("Usage: python test.py <test file list>")

k = 3
#int(raw_input("Set k in KNN (k should be a odd integer):"))

with open(sys.argv[1],'r') as f:
		# read all lines in file as a list
		# each element in the list represent a line in string form
		test_list = f.read().splitlines()

test_length = len(test_list)
correct_result = 0.0

#while(raw_input("Wanna use genre classify machine? y/n: ") == 'y'):
for test_song in test_list:
	#test_song = raw_input("Input the file name of the song you want to classify:")

	Song = {'classical':0, 'country': 0, 'jazz':0, 'pop':0, 'rock':0, 'techno':0}

	with open('train_list_3','r') as f:
		# read all lines in file as a list
		# each element in the list represent a line in string form
		train_list = f.read().splitlines()

	UNLL_vector = []	# vector to store the UNLL value for each test song

	# get feature matrix for test song
	feature_matrix_test = read_file(test_song)
	
	for training_song in train_list:
		
		# get the genre for given training song so we store it with UNLL value in UNLL vector
		for key in Song:
			if key in training_song:
				genre = key
				break

		# read mean vector and cov matrix for given training song
		get_classical_matrixes = read_file(training_song+'_matrixes')	
		mean_vector_classical = get_classical_matrixes[0]
		covariance_matrix_inversed = get_classical_matrixes[1:]

		# add UNLL value for given test song and training song, and the genre of training song to UNLL vector
		UNLL_vector.append([get_UNLL(feature_matrix_test, mean_vector_classical, covariance_matrix_inversed), genre])

	UNLL_vector = sorted(UNLL_vector)	# sort UNLL vector from the lowest value to highest
	#print_matrix(UNLL_vector)

	for i in range(k):
		Song[UNLL_vector[i][1]] += 1	# get k neatest neighbor

	result_genre = ""

	while True:
		result_genre = max(Song, key = Song.get)	# get the genre with highest vote
		max_vote = Song[result_genre]
		if (list(Song.values())).count(max_vote) == 1:
			break
		else:
			Song[UNLL_vector[k][1]] += 1
			k = k+1

	k = 3


	if result_genre in test_song:
		correct_result += 1.0

	print test_song, 'is in genre', result_genre
'''
	for key in Song:
		print key,':',Song[key]

	print '\n'
'''
if test_length != 1:
                print "The accuracy is:",str(round(correct_result / test_length * 100))+'%'
                #dont print accuracy if we're only testing one file





