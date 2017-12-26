
# These appends the /Utilities/Exercise 3 folder to the system path

import sys
import os
sys.path.append(os.getcwd() + '/Utilities/Exercise 3')

# These are the rest of imports
import glob
import time as tm
from utilities import process_new_files

def waiting_for_files (directory):

	# This function waits for new files and pass them to process_new_files 
	# function.

	has_finished = False
	old_files=[]

	while (not has_finished):

		# actual_files contain all the json files that start with orders-

	    actual_files = glob.glob(directory + "/orders-*.json")

	    # if actual_files contains new files(not in old_files),
	    # process_new_files is called

	    if actual_files != old_files:

	        print ("News!!!")
	        process_new_files(actual_files,old_files)
	        old_files = actual_files

	    else : 

	    # else we have no new files. Nothing to do.

	        print ("Nooooothing")

	    # waits 10 seconds before checking again.

	    tm.sleep(10)

if __name__ == '__main__':

	params = sys.argv

	if len(params) != 2 :
	    
	    print ("You must enter 1 parameter")

	else :

	    directory  = params[1]
	    
	    # Here the process get called 
	    waiting_for_files(directory)