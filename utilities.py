def separate_data(data):

    # This function returns the data separeted into two list based on
    # if each row contains five fields (clean_rows list) or not (bad_rows
    # list).

    bad_rows = []
    clean_rows = []

    for line in data:

        x = (line.replace("\n", "")   # Removes the end of line character
                 .replace(" ", "")    # Removes the spaces inside the fields
                 .split("\t"))        # Splits the row in a list
                                      # where each word is an element

        if len(x) == 5:               # If the list contains 5 elements
                                      # I suppose that the row is correct
            clean_rows.append(x)

        else:                         # Else, I add it to the bad_rows list
                                      # to correct them
            bad_rows.append(x)

    return clean_rows, bad_rows


def clean_bad_rows(bad_rows):

    # This function removes the empty fields generated in the bad_rows list
    # in order to avoid data quality issues.

    clean_bad_rows = []                   # Here all the clean rows will be 
                                          # inserted 
    for row in bad_rows:

        clean_row = []                    # Here each row will be inserted clean

        for element in row:

            if element != "":

                clean_row.append(element) # If the element is not empty, it's
                                          # inserted in the clean_row list
        clean_bad_rows.append(clean_row)  # The clean rows are inserted in 
                                          # clean_bad_rows list
    return clean_bad_rows


def read_tsv(file_to_load, position, length):

    # This function reads a file (file_to_load) from a given position (position)
    # and for a given number of bytes (length).
    # Afterwards the full file or a subset of it is splitted into two list
    # using the separate_data function.

    import sys

    with open(file_to_load, encoding="UTF-16LE") as file:

        section = []

        length_read = 0

        end_position = position + length

        if position != 0:

            # If a position different from 0 is passed, it reads untill it 
            # reaches the first new line after that point

            while (length_read < position):
                new_line = file.readline()
                length_read = length_read + sys.getsizeof(new_line)

        if length != 0:

            # If a length different from 0 is passed, it reads all the lines 
            # from the starting point untill it reaches the row where the bytes 
            # length ead is bigger than the length variable. All these lines are 
            # stored in the section list.

            while (length_read < end_position):
                new_line = file.readline()
                section.append(new_line)
                length_read = length_read + sys.getsizeof(new_line)

        else:

            # When position and length are equal to 0, all the file is read and
            # and stored in the section list.

            for row in file:
                section.append(row)

        # returns all the read rows splitted into two list using the
        # separate_data funtion to know which rows have to be treated
        # (bad_rows list)

        clean_rows, bad_rows = separate_data(section)

        bad_rows = clean_bad_rows(bad_rows)

    return clean_rows, bad_rows

def join_bad_rows (bad_rows):

    # This function returns a dictionary, which will contain an entry with 
    # a rowid (row) as a key and all the parts that will build the clean rows
    # as value.

    row = 0
    joined_rows = {}
    
    for bad_row in bad_rows:

        # If the first item of each part is a number below 1000, this part
        # will be treated as the start of the new rows.

        if (bad_row[0].isdigit()):

            if int(bad_row[0]) < 1000:       
                                            
                row = row + 1                
                joined_rows [row] = list(bad_row)

        # The rest of parts will be concateneted to the last created row.

            else : 
                joined_rows [row] = joined_rows [row] + bad_row

        else : 
            joined_rows [row] = joined_rows [row] + bad_row

    return joined_rows

def treat_bad_rows (clean_rows,joined_bad_rows):

    # This function removes the fourth item (which is the second surname)
    # of all the rows that contain more than five items

    new_row = []
    
    for i in joined_bad_rows.values() :
        
        if (len(i) == 5):              # The rows with 5 elements are appended 
                                       # as they are.
            clean_rows.append(i)

        else : 
            
            new_row = []        
            
            for d in (0,1,2,4,5):      # The rows with 6 elements are appended
                                       # without the fourth element.
                new_row.append(i[d])
                
            clean_rows.append(new_row)
            
    return clean_rows
