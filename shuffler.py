'''
For LAMWITTY project Andrea Cuadra
By Andrea Cuadra, all rights reserved
'''

import os
import sys 
import numpy as np

def create_sets(datadir):
    all_files = os.listdir(os.path.abspath(datadir))
    docs = np.array(all_files)
    idx = np.hstack((np.ones(.7*len(docs)), np.zeros(.3*len(docs))))
    np.random.shuffle(idx)
    train = docs[idx == 1]
    valid = docs[idx == 0]
    testing_divider = len(valid)/2
    test = valid[:testing_divider]
    valid = valid[testing_divider:]
    move_files(datadir, train, valid, test)

def move_files(datadir, train, valid, test):
	file_counter = 0
	for tup in train:
		move_file = 'mv ' + datadir + '/' + tup + ' ' +  datadir.split("/")[0] + '/train/' + datadir.split("/")[1]
		file_counter += 1
		os.system(move_file)
	for tup in valid:
		move_file = 'mv ' + datadir + '/' + tup + ' ' + datadir.split("/")[0] + '/valid/' + datadir.split("/")[1]
		file_counter += 1
		os.system(move_file)
	for tup in test:
		move_file = 'mv ' + datadir + '/' + tup + ' ' + datadir.split("/")[0] + '/test'
		file_counter += 1
		os.system(move_file)

# SCRIPT
if len(sys.argv) < 2:
    print("No data directory given\nUsage: \
    python shuffler.py [datadir]")
    quit()
else:
    datadir = sys.argv[1]
    create_sets(datadir)
