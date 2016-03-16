#!/usr/bin python
import os, sys, time, numpy
from pprint import pprint
import json 

class Song:
    title = ""
    artist = ""
    genre = ""
    segments = []


dataset = {}  #stores filenames by genre
for directory in os.listdir(sys.argv[1]):
    files = os.listdir(sys.argv[1]+"/"+directory)
    dataset[directory] = files

TRAINING_NUM = 5
TESTING_NUM = 5

features = {}
for genre in dataset.keys():

    # READ IN BAG OF FEATURES INTO FEATURES VECTORS
    i = 0
    features[genre] = []
    for musicfile in dataset[genre]:
        if i == TRAINING_NUM:
            break
        i+=1

        s = Song()
        s.genre = genre
        segments = []

        for line in open(sys.argv[1]+"/"+genre+"/"+musicfile):            
            segment = line.strip().split(",")
            if line.startswith("#"):  # the first line
                s.title = line.split("#")[1].strip()
            else:
                segments.append(segment)
            
        s.segments = segments
        features[genre] = features[genre] + segments

    # CALCULATE GAUSSIAN DISTRIBUTION
    means, covariance, inversecov = {}, {}, {}
    sys.stdout.write("Calculating covariance for %s...\n" % genre)
    covariance[genre] = numpy.cov(features[genre])
    sys.stdout.write("Calculating inverse for %s...\n" % genre)
    inversecov[genre] = numpy.linalg.inv(covariance[genre])
    print(covariance[genre])
    print(inversecov[genre])


''' PRINT FEATURES MATRIX '''
for genre in features.keys():
    print genre
    print str(len(features[genre]))+" segments"

    
