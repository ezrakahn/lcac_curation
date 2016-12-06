__author__ = 'ekahn'
__project__ = 'fidelity_checks'

import pandas as pd
from tkinter import filedialog as fd
import re
'''
Try using the tkinter dialog, get the tile type, and then pick which read method.
There are three types, .xls .xlsx .csv
'''

'''
To Do:
Figure out how to exit the script in the case of wrong filetype
'''

def read_file(file,filetype):
	if filetype == 'csv':
		df = pd.read_csv(file)
	elif filetype == 'xls':
		df = pd.read_excel(file)
	elif filetype == 'xlsx':
		df = pd.read_excel(file)
	else:
		return print('file needs to be either excel or csv')

	return df

file = fd.askopenfile(mode='r')
filename = file.name

p = re.compile(r'\.')
filetype = re.split(p,filename)[-1]

df = read_file(file, filetype)

print(df.head())





'''
test = pd.read_csv('flow_dump.csv')

print(test)
'''