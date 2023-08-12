#!/usr/bin/env python

# import necessary modules
import os, time, datetime, csv

# ------------------------------------------------
# TO MODIFY BEFORE USING:

# source_directory is the path where your content files are located
source_directory = "P:\\ATH\\TO\\YOUR\\SOURCE\\DIRECTORY"

# log_directory is where you want files about this process to be saved 
# (files like the list of all your files and their last modified dates). 
# I'd recommend somewhere easy to find, like a new folder on your desktop.
log_directory = "P:\\ATH\\TO\\LOG\\DIRECTORY"
# ------------------------------------------------

# create variables to store all of the filepaths
all_filepaths = set()

# create variable to store all last modified years
mod_dict = {}

# create variables to store the frequency of last modified years and the quantity of files
frequency = {}
frequency_set = set()
year_totaler = 0

# for each file in your source folder location
for root, dirs, files in os.walk(source_directory):
    for file in files:

        # find the full path for the file
        filepath = os.path.join(root, file)

        # add the full path to the ongoing list of all filepaths
        all_filepaths.add(filepath)

# for each filepath in all_filepaths
for i in all_filepaths:

    # try to calculate the last modified year
    try:
        modified_year = time.strftime('%Y', time.localtime(os.path.getmtime(i)))
        # if successful, add this info to the variable storing the paths and their modified years
        mod_dict[i] = modified_year

    # if there's an error, pause for one second and then try again
    except:
        time.sleep(1)
        try:
            modified_year = time.strftime('%Y', time.localtime(os.path.getmtime(i)))
            mod_dict[i] = modified_year

        # if there's still an error
        except:
            # say the last modified year is "9000" and add the pair to the same variable (mod_dict)
            modified_year = 9000
            mod_dict[i] = modified_year

# save the results to a csv file on your desktop
with open("%s\\files_modifiedyears.csv" % log_directory, 'w', newline = '') as export_csv:
    writer = csv.writer(export_csv, delimiter='`')
    for key in mod_dict.keys():
        writer.writerow((key,mod_dict[key]))

# open that same file 
with open("%s\\files_modifiedyears.csv" % log_directory, newline = '') as csv_file:
    reader = csv.reader(csv_file, delimiter='`')
    # save the information in the file as "csv_list"
    csv_list = list(reader)

# go through each file/year pair one at a time to find the frequency of last modified years
for item in csv_list:
    frequency_set = set(frequency)

    # identify the last modified year as being in the second column of the csv
    year = str(item[1])

    # if this year is already in the list of years, then +1 to the tally of that year for this file
    if year in frequency_set:
        frequency[year] += 1
    
    # if it isn't, then add the year to the list of years, with the number of files in that year as 1
    else:
        frequency[year] = 1

# in ascending order, display each year and the number of files in that year
for year, counter in sorted(frequency.items()):
    print(('%s: %s' % (year, counter)))

    # add that number of files to a tally for the grand total number of files
    year_totaler += int(frequency[year])

# display the grand total
print('Grand Total:', year_totaler)
