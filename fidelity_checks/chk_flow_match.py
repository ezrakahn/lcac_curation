__author__ = 'ekahn'
__project__ = 'fidelity_checks'
'''
Script to look for overlapping flows in two different openLCA datasets.  Requires text files with two columns,
the first column is the ref_id, the second is the flow name.

This is the script to run things.  The meat is in funcs.py.

So far, this script compares the flows in two tables.  It identifies which flows occur in both tables, and it checks if
the names are the same.
Next, compare these to tables to the joined set of flows, and see if any did not make it.
'''

from funcs import *

'''
To Do:
1) Want to use a dialog link Tkinter widget to get a text to label the tables for output.
	Also, is there a way to message the user with the file dialog?
	https://docs.python.org/3.4/library/tkinter.html#tkinter-modules
3) Figure out the error handling so we can get better messages
'''


def checkTwoDatabases():

	#Get the two files and split them into different files
	files = getTwoFilenames()
	filenames = files[0]
	filetypes = files[1]

	#Write the files to pandas dataframes
	left = read_file(filenames[0], filetypes[0])
	right = read_file(filenames[1], filetypes[1])

	#Get ref_ids of overlapping flows.
	#Change the index values to the 'ref_id' term.
	id_match = left[left['ref_id'].isin(right['ref_id'])].dropna()

	#With the id_match, find any mismatched names.
	name_mismatch = id_match[~id_match['name'].isin(right['name'])]

	#diff = right_in_left[~right_in_left.isin(left_in_right)]
	print('matching ids: \n', id_match.to_string(), '\n \n')
	print('mismatched names (left names not in right flow name list): \n', name_mismatch.to_string())


def checkThreeDatabases():
	#The idea is to compare separate databases against a merged database.

	#First, get the separate database flow files
	files = getTwoFilenames()

#checkTwoDatabases()
