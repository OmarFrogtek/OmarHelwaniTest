
# These appends the /Utilities/Exercise 1 folder to the system path

import sys
import os
sys.path.append(os.getcwd() + '/Utilities/Exercise 1')

# These are the rest of imports

from multiprocessing import Pool
from utilities import read_tsv, join_bad_rows, treat_bad_rows
from ex1 import read_and_clean_tsv


def exercice1(file_to_load, clean_file, position=0, length=0, splits=1):

    # This function is the one that executes the process of reading and cleaning
    # a tsv file. If the length parameter is different from 0 and a split value 
    # is passed as parameter, the process executes "splits" threads to execute
    # the process in parallel
    
    threads = []
    number_of_processes = splits

    if length != 0:

    # If the length parameter is different from 0, "splits" threads are created.

        space = int(length / splits)
        
        for i in range(0, splits):
            start_position = position + i * space
            threads.append((file_to_load, clean_file, start_position, space))

    else:
        threads.append((file_to_load, clean_file, position, 0))

    pool = Pool(processes=number_of_processes)
    
    result_list = pool.map(read_and_clean_tsv, threads)


if __name__ == '__main__':
    
    params = sys.argv
    
    if len(params) < 3 :
        
        print ("You must enter the name of the field and at least 2 parameters")
    
    elif len(sys.argv) > 6 :
        
        print ("You must enter the name of the field and between 2" + 
               "and 5 parameters")
    
    else :
        
        for param in range (len(params),6):
            
            if param == 5 :
                
                params.append(1)
            
            else :
                params.append(0)

        file_to_load = params[1]
        clean_file   = params[2]
        position     = int(params[3])
        length       = int(params[4])
        splits       = int(params[5])

        # Here the process get called 
        exercice1(file_to_load,clean_file,position,length,splits)



