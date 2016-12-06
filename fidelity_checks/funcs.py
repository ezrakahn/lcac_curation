__author__ = 'ekahn'
__project__ = 'fidelity_checkis'
'''
Suuporting functionality for the LCA openLCA data curation business.
'''
import pandas as pd
from tkinter import filedialog as fd
import re

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

#This is the read file business.
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

def getTwoFilenames():
	files = fd.askopenfilenames()
	check_file_size(files)

	file1 = files[0]
	file2 = files[1]

	files = [file1, file2]

	#Get the file type extensions
	p = re.compile(r'\.')
	file1_type = re.split(p,file1)[-1]
	file2_type = re.split(p,file2)[-1]

	filetypes = [file1_type, file2_type]

	return [files, filetypes]

