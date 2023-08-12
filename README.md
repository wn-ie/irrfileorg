# irrfileorg
**Working Towards Long-Term Preservation in a Non-Preservation Environment: *I*dentifying, *R*eplicating, and *R*estructuring *File Org*anization**
## general requirements
In order to run this code, you'll need python.

To download python on Windows (for free, if it costs money then it's the wrong application!) by searching the Microsoft Store for "python" or going to the following link:
https://www.microsoft.com/store/productId/9NRWMJP3717K

## how to use these files

for each file listed below in the [raw file links section](https://github.com/wn-ie/irrfileorg#raw-file-links), you'll want to:
1. Click the link
2. Open a blank plain text file on your computer (you can use the "Notepad" application that comes with Windows)
3. Copy *all* of the text from the webpage, and paste it into the blank plain text file
4. Save this plain text file with the extension `.py` (instead of `.txt`) 
5. In the same text editor, find and modify the example paths and years (in all caps, they'll look like `P:\\ATH\\TO\\YOUR\\SOURCE\\DIRECTORY\\` or `X-YEAR-HERE`) so that they go to your specific locations. Make sure to use two backslashes (`\\`) instead of one (`\`) and to not accidentally delete the quotation marks(`"`). 
    - Lines that start with `#` are comments, which explain what each portion of the script is doing.
6. Once your new .py file has been modified, then open a new command prompt window (by pressing the start button and then typing 'cmd'). 
7. In this command prompt window, type `py`, followed by the path of the file you want to run. For example, `py P:\ath\to\file.py` or `py P:\ath\to\a\different\file.py`, and hit enter to run the file.

## raw file links
1. [Identify the last modified dates of all files in the original location](https://raw.githubusercontent.com/wn-ie/irrfileorg/main/identify_last_mod_dates.py)
2. [Identify which files were last modified during X year](https://raw.githubusercontent.com/wn-ie/irrfileorg/main/duplicate_xyear_files.py)
3. [Duplicate identified X year files into the X year directory](https://raw.githubusercontent.com/wn-ie/irrfileorg/main/duplicate_xyear_files.py)