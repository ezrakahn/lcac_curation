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
1) Test with full data table dump. Currently using just subset.

2) Need better streamline of workflow.  It currently asks you to select files too many times and it's annoying.
	Also, need to get the file writer a little smarter about the size of the list it's receiving.

3) Need to finish the report document writer.

Later:
--	Want to use a dialog link Tkinter widget to get a text to label the tables for output.
	Also, is there a way to message the user with the file dialog?
	https://docs.python.org/3.4/library/tkinter.html#tkinter-modules

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

	print('matching ids: \n', id_match.to_string(), '\n \n')
	print('mismatched names (left names not in right flow name list): \n', name_mismatch.to_string())

	return [id_match, name_mismatch]


def checkThreeDatabases():
	#The idea is to compare separate databases against a merged database.

	#First, get the separate database flow files
	files = getTwoFilenames()
	filenames = files[0]
	filetypes = files[1]

	#Write these to pandas datafames
	dfone = read_file(filenames[0], filetypes[0])
	dftwo = read_file(filenames[1], filetypes[1])

	#Get the merged dataset
	file = getOneFilename()
	filename = file[0]
	filetype = file[1]

	merged = read_file(filename,filetype)

	#Check if the any of the flows are not in the merged dataframe
	dropped_one = dfone[~dfone['ref_id'].isin(merged['ref_id'])]
	dropped_two = dftwo[~dftwo['ref_id'].isin(merged['ref_id'])]

	print('dropped flows from first dataset: \n', dropped_one.to_string(), '\n \n')
	print('dropped flows from second dataset: \n', dropped_two.to_string(), '\n \n')

	return [dropped_one, dropped_two]

def writereport(analysis):
	#This doesn't quite work yet.  The report string is not the right form.
	#Generate the report
	header1 = 'matching ids: \n'
	header2 = 'mismatched names (left names not in right flow name list): \n'
	header3 = 'dropped flows from first dataset: \n'
	header4 = 'dropped flows from second dataset: \n'

	report = [header1, analysis[0][0], header2, analysis[0][1], header3, analysis[1][0], header4, analysis[1][1]]

	#return print(report)
	#Get down to the business of writing the file
	filename = fd.asksaveasfilename()

	with open(filename, 'w') as report_file:
		'''
		report_file.write('matching ids: \n',
						  analysis[0][0],
						  '\n \n mismatched names (left names not in right flow name list):',
						  analysis[0][1],
						  '\n \n dropped flows from first dataset:',
						  analysis[1][0],
						  'dropped flows from second dataset:',
						  analysis[1][1]
		)
		'''
		output =
		report_file.write('\n'.join(report))

analysis=[]
analysis.append(checkTwoDatabases())
analysis.append(checkThreeDatabases())

writereport(analysis)