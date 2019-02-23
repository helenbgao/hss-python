# top_zip.py
#
# write a program that finds the 10 five-digit zip codes that hold the most wine and beer suppliers in missouri
# these 10 zip codes are listed in decreasing order by number of suppliers
# nine digit zip codes are converted to five digit zip codes by truncating the last four digits
# the program takes a filename for a csv file on the command line
# Usage:
#     % python top_zip.py sys.argv[1] (provided that sys.argv[1] is a csv file in the same directory as top_zip.py)
#
# Helen Gao, 7-23-2018 by 11am


# import the sys library so that python can run command line arguments
import sys

# import the csv library so that python can read csv files
import csv

# if two arguments are not provided
# the program will print the proper usage rather than displaying an error message
if len(sys.argv) != 2:

    # print the proper usage
    print('Usage: python', sys.argv[0], "<filename>")

# if the arguments properly provided
try:

    # the program opens sys.argv[1] for reading
    with open(sys.argv[1], "r") as file:

        # the program uses the csv library's reader to read the csv file
        reader = csv.reader(file)

        # an empty dictionary is created
        # this will later hold the zip codes and number of suppliers from each zip code
        zipdict = {}

        # the next function skips the header
        next(reader)

        # for every row in the read csv file
        for row in reader:

            # the variable zipcode is set to the first five characters in the second row
            # this will truncate 9-digit zip codes and leave 5-digit zip codes intact
            zipcode = row[1][:5]

            # if the new zip code is not in the dictionary of zip codes
            if zipcode not in zipdict:

                # the zip code is added to zipdict as a key with value 1 since it has appeared in only one instance
                zipdict[zipcode] = 1

            # if the new zip code is already in the dictionary of zip codes
            else:

                # the value of the zip code in the dictionary increases by one since it has appeared multiple times
                zipdict[zipcode] = zipdict[zipcode] + 1

        # a new list of supplier amounts and zip codes using list comprehension
        zipcodelist = [[zipdict[zipcode], zipcode] for zipcode in zipdict]

        # the list is sorted
        # since the number of suppliers are in the keys of the dictionary the list is in increasing order of suppliers
        zipcodelist.sort()

        # the program prints the last 10 items in the list using slicing
        print(zipcodelist[:-11:-1])

# in the case of a file not found error
except FileNotFoundError:

    # print an error message saying that the file was not found
    print('File', sys.argv[1], 'was not found')

# in the case of another error
except:

    # print an error message saying that the program could not read the file
    print('Could not read the file')

# note: went to joe's thursday section where we all worked on/discussed this top_zip program