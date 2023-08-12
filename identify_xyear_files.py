#!/usr/bin/env python

# import necessary module
import csv

# open the CSV file with the year modified information of all files
with open(r"P:\\ATH\\TO\\YOUR\\DESKTOP\\filemodified.csv", newline = '') as csv_file:
    reader = csv.reader(csv_file, delimiter='`')
    # save the information in the file as "csv_list"
    csv_list = list(reader)

# go through each pair of filepath and its last modified year
for item in csv_list:

    # the year is the second column of the CSV and the filepath is the first column
    year = str(item[1])
    filepath = str(item[0])

    # if the year listed is the same as the year you're identifying
    if (year == 'X-YEAR-HERE'):

        # save the file's path to a text file of all files from X year
        with open(r"P:\\ATH\\TO\\YOUR\\DESKTOP\\X-YEAR_filepaths.txt", 'a') as yearfile:
            yearfile.write('''%s\n''' % filepath)
