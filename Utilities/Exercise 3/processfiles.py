def process_new_files(actual_files,old_files):

    # This function waits for new files, and prints their content.

    import json
    import time as tm

    results = {}

    # new_files contains the files that are in the actual_files list and not
    # in the old_files list.

    new_files = [x for x in actual_files if x not in old_files]

    # Each loop process one file

    for new_file in new_files:

        document = []

        # Each loop inserts a whole file in the document list.

        for line in open(new_file, 'r'):

            document.append(json.loads(line))

        # Each loop counts one order and adds it to the number of orders 
        # of that type.

        for order in document:

            if order['Type'] in results:

                results[order['Type']] = results[order['Type']] + 1

            else : 

                results[order['Type']] = 1

        # Prints the final results for each file

        print ('"OrderCancelled": ' + str(results["OrderCancelled"]))
        print ('"OrderAccepted": '  + str(results["OrderAccepted"]))
        print ('"OrderPlaced": '    + str(results["OrderPlaced"]))

        # Time to sleep

        tm.sleep(5)
