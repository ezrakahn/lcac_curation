__author__ = 'ekahn'
__project__ = 'fidelity_checks'
'''
Script to look for overlapping flows in two different openLCA datasets.  Requires text files with two columns,
the first column is the ref_id, the second is the flow name.

So far, this script compares the flows in two tables.  It identifies which flows occur in both tables, and it checks if
the names are the same.
Next, compare these to tables to the joined set of flows, and see if any did not make it.
'''
import pandas as pd
from tkinter import filedialog as fd
#from tkinter import
import re

'''
To Do:
1) Want to use a dialog link Tkinter widget to get a text to label the tables for output.
	Also, is there a way to message the user with the file dialog?
	https://docs.python.org/3.4/library/tkinter.html#tkinter-modules
2) Modularize the functions
3) Figure out the error handling so we can get better messages
'''
#Get the files to be compared.  These should be tbl_flow dumps as csv or excel


#This is the read file business.  How to modularize these?
def read_file(file,filetype):
	if filetype == 'csv':
		df = pd.read_csv(file)
	elif filetype == 'xls':
		df = pd.read_excel(file)
	elif filetype == 'xlsx':
		df = pd.read_excel(file)
	else:
		return print('file needs to be either excel or csv')
		exit	#This get's us out of this function without returning anything, but the script carries on.

	return df.dropna()


#We want two files, not less, not more
def check_file_size(files):
	x = len(files)
	if x > 2:
		print("You selected too many files, select 2 only")
		exit
	elif x < 2:
		print('Select two data files for comparison')
		exit
	return

#Get the two files and split them into different files
files = fd.askopenfiles(mode='r')
check_file_size(files)

file1 = files[0]
file1_name = file1.name

file2 = files[1]
file2_name = file2.name

#Get the file type extensions
p = re.compile(r'\.')
file1_type = re.split(p,file1_name)[-1]
file2_type = re.split(p,file2_name)[-1]

#print('output : \n',file1_type)

#Write the files to pandas dataframes
left = read_file(file1, file1_type)
right = read_file(file2, file2_type)

#OBE
#lfile = fd.askopenfile(mode='r')
#rfile = fd.askopenfile(mode='r')

#left = pd.read_table(lfile,usecols=[0,1])
#lindx = list(left.columns)[0]

#right =  pd.read_table(rfile,usecols=[2,3])
#rindx = list(left.columns)[0]

#Get ref_ids of overlapping flows.
#Change the index values to the 'ref_id' term.
id_match = left[left['ref_id'].isin(right['ref_id'])].dropna()

#With the id_match, find any mismatched names.
name_mismatch = id_match[~id_match['name'].isin(right['name'])]

#diff = right_in_left[~right_in_left.isin(left_in_right)]
print('matching ids: \n', id_match.to_string(), '\n \n')
print('mismatched names (left names not in right flow name list): \n', name_mismatch.to_string())
#print(lindx)




'''
print(filename[0],'\n\n\n')
print(filename[1],'\n\n\n')
#print(right)
'''