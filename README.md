# Frogtek Technical test

This is the Omar Helwani to the Frogtek technical test.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3
```

### How to run Exercise 1

In the downloaded folder, using the command line, type :

```
python exercice1.py <name_of_the_tsv_file_to_be_read> <name_of_the_tsv_file_to_be_written>
```

If you want to execute it using parallelism : 

```
python generate_events.py <name_of_the_tsv_file_to_be_read> <name_of_the_tsv_file_to_be_written> <start_position> <length_to_be_treated> <number_of_threads>
```
length_to_be_treated must be different from 0, which is the default to read the rest of the file.

### How to run Exercise 2

In the downloaded folder, using the command line, type :
```
python generate-events.py --number-of-orders=100 --batch-size=50 --interval=1 --output-directory=/Users/omarhelwani/
```
Parameter values can be changed.

End with an example of getting some data out of the system or using it for a little demo

### How to run Exercise 3

In the downloaded folder, using the command line, type :

```
python exercice3.py <directory_to_be_watched>
```
## Authors

* **Omar Helwani** - *Initial work* - [OmarHelwani](https://github.com/PurpleBooth)
