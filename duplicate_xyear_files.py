#!/usr/bin/env python

# import necessary modules
import sys, os, subprocess

# set location of the destination directory
basedestination = "P:\\ATH\\TO\\DESTINATION\\OF\\X-YEAR\\"

# set location of the robocopy log
robologpath = "/unilog+:P:\\ATH\\TO\\YOUR\\DESKTOP\\robocopy_log.txt"

# set location of the robocopy errors log
roboerrorspath = r"P:\\ATH\\TO\\YOUR\\DESKTOP\\robocopy_errors.txt"

# set counters for successful transfers and transfers with errors
erroracc = 0
successacc = 0

# open the txt file containing paths from X year
with open(r"P:\\ATH\\TO\\YOUR\\DESKTOP\\X-YEAR_filepaths.txt", encoding='utf-8') as cp:
    txtfilepaths = (cp.read()).split('''\n''')

# for each file in X year
for filepath in txtfilepaths:
    if filepath != '':

        # determine file name and source directory
        filename = os.path.basename(filepath)
        filedir = os.path.dirname(filepath)

        # remove any folders that you don't want in the destination location, such as "Current"
        destfiledir = (os.path.dirname(filepath)).replace('P:\\ATH\\OF\\FOLDER\\TO\\EXCLUDE\\', '').replace('P:\\ATH\\TO\\SOURCE\\DIRECTORY\\', '')
        
        # create full destination path
        robodestination = basedestination + destfiledir
        
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
