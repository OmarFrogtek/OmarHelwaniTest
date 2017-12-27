
# These appends the /Utilities/Exercise 2 folder to the system path

import sys
import os
sys.path.append(os.getcwd() + '/Utilities/Exercise 2')

# These are the rest of imports

import datetime
import os
import json
import time as tm
import math
from generateorder import create_OrderId



def generate_events(number_of_orders, batch_size , interval , output_directory ):

	# This function creates a given number of orders (number_of_orders), where 
	# each file contains a given number of orders (batch_size). The process 
	# stores the files in the directory provided (output_directory), sleeping
	# a number of seconds between files (interval) 

	orders_processed = 0
	number_of_files = math.ceil(number_of_orders / batch_size)

	for i in range(0, number_of_files): 

		# Each loop creates a different file

		time = datetime.datetime.now().strftime("%Y-%m-%d-%I-%M-%S-%f")
		file_name = output_directory + "orders-" + time + ".json"

		with open(file_name, 'w') as outfile:

				# If the numbers of remaining orders are less than the batch 
				# size the number of the last batch size is changed.

				if orders_processed + batch_size > number_of_orders:

						batch_size = number_of_orders - orders_processed

				# Each loop creates a different order

				for j in range(0, batch_size):

						timestamp = datetime.datetime.now().isoformat()
						order_id = create_OrderId()
						order_placed = {"Type": "OrderPlaced",
										"Data": {"OrderId": order_id,
												 "TimestampUtc": timestamp}
										}

						# Every five orders a OrderCancelled is created

						if j % 5 == 0:

							second_order = {"Type": "OrderCancelled",
											"Data": {"OrderId": order_id,
													 "TimestampUtc": timestamp
													 }
											}

						# Else a  OrderAccepted is created

						else:

							second_order = {"Type": "OrderAccepted",
											"Data": {"OrderId": order_id,
													 "TimestampUtc": timestamp
													 }
											}

						# Orders are inserted in the file in different lines.

						json.dump(order_placed, outfile)
						outfile.write('\n')
						json.dump(second_order, outfile)
						outfile.write('\n')

		# The file is closed, and the number of orders is updated.
		# Afterwards the process sleep is performed.

		outfile.close()
		orders_processed = orders_processed + batch_size
		tm.sleep(interval)

if __name__ == '__main__':
    
    params = sys.argv
    
    if len(params) != 5 :
        
        print ("You must enter 4 parameters")
    
    else :

        number_of_orders  = int(params[1].replace("--number-of-orders=",""))
        batch_size        = int(params[2].replace("--batch-size=",""))
        interval          = int(params[3].replace("--interval=",""))
        output_directory  = params[4].replace("--output-directory=","")
        
        # Here the process get called 
        generate_events(number_of_orders,batch_size,interval,output_directory)


