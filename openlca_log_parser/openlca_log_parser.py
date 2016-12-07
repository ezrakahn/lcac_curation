# This script parses openLCA logs into a more readable format.

def import_libs():
    '''
        Import Pandas and Numpy libraries
    '''
    import pandas as pd
    import numpy as np

def set_filepath(filepath=None):
    '''
        Create string object containing filepath for html file.
    '''
    if filepath is None:
        filepath = 'C:\Users\zac.coventry\Documents\GitHub\openlca_log_parser\log.html'
    else:
        pass

if __name__ == '__main__':

    filepath = set_filepath()
    print filepath
