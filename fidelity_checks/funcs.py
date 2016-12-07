__author__ = 'ekahn'
__project__ = 'fidelity_checks'
'''
Supporting functionality for the LCA openLCA data curation business.
'''
import pandas as pd
from tkinter import filedialog as fd
import re
from sys import exit

'''
#Not using this function anymore
def check_file_size(files):
	x = len(files)
	if x > 2:
		print("You selected too many files, select 2 only")
		exit
	elif x < 2:
		print('Select two data files for comparison')
		exit
	return
'''


def read_file(filename, filetype):
	#This is the read file business.
	if filetype == 'csv':
		df = pd.read_csv(filename)
	elif filetype == 'xls':
		df = pd.read_excel(filename)
	elif filetype == 'xlsx':
		df = pd.read_excel(filename)
	else:
		exit('error regarding filetype.  files can be either xls, xlsx or csv only, and should be olca txt dumps')

	return df.dropna()


def getTwoFilenames():
	files = fd.askopenfilenames(title='Select two files containing flows to compare')

	#check_file_size(files)
	#We want two files, not less, not more
	if len(files) > 2:
		exit("You selected too many files, select 2 only")
	elif len(files) < 2:
		exit("Select two data files for comparison, you didn't select enough")

	file1 = files[0]
	file2 = files[1]

	files = [file1, file2]

	#Get the file type extensions
	p = re.compile(r'\.')
	file1_type = re.split(p, file1)[-1]
	file2_type = re.split(p, file2)[-1]

	filetypes = [file1_type, file2_type]

	return [files, filetypes]


def getOneFilename():
	file = fd.askopenfilename(title='Select a file containing merged flows')

	#Get the file type extensions
	p = re.compile(r'\.')
	filetype = re.split(p, file)[-1]

	return [file, filetype]

#getOneFilename()
#getTwoFilenames()