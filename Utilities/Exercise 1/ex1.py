from utilities import read_tsv, join_bad_rows, treat_bad_rows

def read_and_clean_tsv(p):

    # This function recieves a list with four parameters. With these parameters,
    # reads a file (first parameter), writes a clean file (second parameter),
    # It also can read a portion of the file (the third parameter marks the
    # the start of the portion to read in bytes and the fourth parameter marks 
    # the end of the portion to read)

    file_to_load = p[0]

    clean_file = p[1]

    position = p[2]

    length = p[3]

    clean_rows, bad_rows = read_tsv(file_to_load, position, length)

    if bad_rows:  

        # If in the portion read there are bad rows, they are treated

        joined_bad_rows = join_bad_rows(bad_rows)
        clean_rows = treat_bad_rows(clean_rows, joined_bad_rows)

    if clean_rows:  
        
        # If there are rows to insert in the new file,the files are append 
        # to the file

        with open(clean_file, 'a') as file:
            file.writelines('\t'.join(i) + '\n' for i in clean_rows)
