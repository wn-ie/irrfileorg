#!/usr/bin/env python

# import necessary module
import csv

# ------------------------------------------------
# TO MODIFY BEFORE USING:

# log_directory is where you want files about this process to be saved 
# this should be the same as in the script to identify the last modified dates
log_directory = "P:\\ATH\\TO\\LOG\\DIRECTORY"

# x_year is the specific year you want to identify, such as "2005"
x_year = "X-YEAR-HERE"
# ------------------------------------------------

# open the CSV file with the year modified information of all files
with open("%s\\files_modifiedyears.csv" % log_directory, newline = '') as csv_file:
    reader = csv.reader(csv_file, delimiter='`')
    # save the information in the file as "csv_list"
    csv_list = list(reader)

# go through each pair of filepath and its last modified year
for item in csv_list:

    # the year is the second column of the CSV and the filepath is the first column
    year = str(item[1])
    filepath = str(item[0])

    # if the year listed is the same as the year you're identifying
    if (year == str(x_year)):

        # save the file's path to a text file of all files from X year
        with open("%s\\%s_filepaths.txt" % (log_directory, x_year), 'a') as yearfile:
            yearfile.write('''%s\n''' % filepath)
