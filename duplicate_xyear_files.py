#!/usr/bin/env python

# import necessary modules
import sys, os, subprocess

# ------------------------------------------------
# TO MODIFY BEFORE USING:

# source_directory is the path where your content files are located
source_directory = "P:\\ATH\\TO\\YOUR\\SOURCE\\DIRECTORY"

# log_directory is where you want files about this process to be saved 
# this should be the same as in the previous scripts
log_directory = "P:\\ATH\\TO\\LOG\\DIRECTORY"

# x_year is the specific year you want to identify, such as "2005"
x_year = "X-YEAR-HERE"

# destination_directory is the path where you want the duplicated files to be
destination_directory = "P:\\ATH\\TO\\DESTINATION"

# OPTIONAL BEFORE USING:
# category_folder is if there's a folder name that you don't want 
# to appear as a folder in the destination because it represents a 
# status or category. As an example, the simplified structure discussed 
# in the article would want to exclude "P:\\Newspapers\\Current"
category_folder = "P:\\ATH\\OF\\FOLDER\\TO\\EXCLUDE"
# ------------------------------------------------

# set location of the robocopy log
robologpath = "/unilog+:%s\\robocopy_log.txt" % log_directory

# set location of the robocopy errors log
roboerrorspath = "%s\\robocopy_errors.txt" % log_directory

# set counters for successful transfers and transfers with errors
erroracc = 0
successacc = 0

# open the txt file containing paths from X year
with open("%s\\%s_filepaths.txt" % (log_directory, x_year), encoding='utf-8') as cp:
    txtfilepaths = (cp.read()).split('''\n''')

# for each file in X year
for filepath in txtfilepaths:
    if filepath != '':

        # determine file name and source directory
        filename = os.path.basename(filepath)
        filedir = os.path.dirname(filepath)

        # remove any folders that you don't want in the destination location, such as "Current"
        destfiledir = (os.path.dirname(filepath)).replace(category_folder, '').replace(source_directory, '')
        
        # create full destination path
        robodestination = destination_directory + destfiledir
        
        # run robocopy, saving the output as roboresult
        roboresult = subprocess.run(["robocopy", filedir, robodestination, "/COPY:DAT", "/mt", "/w:1", "/r:1", "/np", "/V", "/tee", robologpath, filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # if there's an error, add it to the error log file and the transfer errors counter
        if int(roboresult.returncode) >= 8:
            roboresult_output = '''%s\n%s\n%s\n\n\n''' % (roboresult.returncode, roboresult.stdout, roboresult.stderr)
            erroracc += 1
            with open(roboerrorspath, 'a') as errorsfile:
                errorsfile.write('''%s\n\n\n''' % roboresult_output)
        
        # if it's successful, add to the transfer success counter
        else:
            successacc += 1

# when finished, display text with the counts of errors, successes, and total files
print("Finished duplication of all files.\nErrors: %s\nSuccesses: %s\nTotal attempted files: %s" % (erroracc, successacc, len(txtfilepaths)))
