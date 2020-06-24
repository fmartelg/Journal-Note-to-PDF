"""
Convert all .jnt files in a directory (including sub directories,etc) to pdf.
1. Identify all .jnt files in a directory
2. Print each one to PDF as "filename-jnt.pdf" and move to same location
3. Optional: Delete .jnt file after printing to PDF
"""

# DONE: Provide output file name as argument
# DONE: Print file from a different folder
# DONE: copy printed PDF to original location
# DONE: Function that identifies all jnt files in an input directory
# DONE: Make sure PDF does not already exist before printing, else the
#       Journal Note prompt to replace will break the program.
# DONE: Document handle function.
# DONE: Refactor the move_pdf function into 3+ functions.
# DONE: Remove superfluos libraries

###########
# Libraries
###########

# from ahk import AHK - not useful bc ahk run does not allow for passing args
import os
import time
import shutil
from pathlib import Path
import subprocess
import psutil

###########
# Functions
###########

def find_jnt_paths(myDirectory):
  """
  Searches iteratively in the root directory for all .jnt files.
  Inputs:
  - A root directory
  Outputs:
  - A list of full paths to all Journal Note files under root directory. 
  """
  list_jnt_paths = []
  for root, dirs, files in os.walk(myDirectory):
    for file in files:
        if file.endswith(".jnt"):
             list_jnt_paths.append(os.path.join(root, file))
  return list_jnt_paths


def print_jnt(fullPath, myFilename):
    """
    Inputs:
    - A string with the full path to a jnt file
    - A string with the output filename
    Ouput:
    - A pdf printout of the file, saved in the location where the
    user last printed from JournalNote to PDF manually.  Assumes it is
    the working directory where this program is saved.
    """
    # Remove double quotes in myFilename
    temp = Path(myFilename.strip('"'))
    # if the file exists in the working directory prompt user to delete file
    if Path.is_file(temp):
      userInput = input("File " + myFilename + " already exists. Do you want to delete it? (y/n)")
      if userInput == 'y':
        Path.unlink(temp) # Delete file
      elif userInput == 'n':
        raise SystemExit('The program will abort')
      else:
        raise SystemExit('That was not a valid entry. The program will abort.')
    subprocess.run(['powershell.exe', './jnt_to_pdf.ahk',
                    fullPath, myFilename])


def check_pdf_duplicate(myFilename, destinationPath):
  '''
  Check if file already exists in destination directory
  Inputs:
  - Name of printed PDF file in working directory
  - Destination filepath
  Outputs:
  - None
  '''
  fullPath = Path(destinationPath).joinpath(myFilename)
  if Path.is_file(fullPath):
    raise SystemExit("A PDF file with the same name already exists in the destination folder. Program will abort.")


def wait_pdf_created(myFilename):
  '''
  Wait for PDF file to be created during printing of jnt
  Inputs:
  - Name of printed PDF file in working directory
  Outputs:
  - None
  '''
  seconds = 0
  timeLimit = 10 # maximum printing time in seconds. Abort if longer.
  while not Path(myFilename).is_file(): 
    time.sleep(1)
    seconds += 1
    #  Abort if taking longer than timeLimit seconds to print
    if seconds == timeLimit:
      raise SystemExit("File " + myFilename + " has taken more than " + timeLimit + " to be created.  The program will abort.")
  else:
    print('Waited {} seconds for file {} to be created'.format(seconds, myFilename))


def wait_file_printed(myFilename):
  '''
  Check file has finished printing (i.e. file size > 0).
  '''
  while os.stat(myFilename).st_size == 0:
    time.sleep(1)


def has_handle(myFilePath):
  '''
  Iterates over all running processes and checks if they have myFilePath open.
  Input:
  - A full file path
  Otput:
  - TRUE if myFilePath is open, FALSE otherwise 
  '''
  for proc in psutil.process_iter():
    try:
      for item in proc.open_files():
        if myFilePath == item.path:
          return True
    except Exception:
      pass
  return False


###########
# Inputs
###########

# Enter the root directory that you want to search for journal note files.
jntRoot = "C:\\Users\\User\\Documents\\myfolder"


###########
# Outputs
###########

# Find all jnt files in the root directory and return them in a list
jntPathList = find_jnt_paths(jntRoot)

# Loop over the list of jnt file paths and print each one.
for i in jntPathList:

    # Check if file already exists in destination folder.
    # Abort if so.
    pdfFilename = Path(i).stem + "-jnt.pdf"
    pdfDestination = Path(i).parent
    check_pdf_duplicate(pdfFilename, pdfDestination)

    # Kick off printing process of .jnt file to pdf
    # Adding double quotes so we can pass paths with spaces to PowerShell
    strFilename = "\"" + Path(i).stem + "-jnt.pdf\""
    strPath = "\"" + i + "\""
    print_jnt(strPath, strFilename)

    # Wait for PDF file to be created
    # This can take a few seconds
    wait_pdf_created(pdfFilename)

    # Wait for PDF file to finish printing.  
    # This can take several minutes, depending on the jnt file. 
    wait_file_printed(pdfFilename)

    # Wait for printing process to release handle on printed PDF
    # This can take several seconds.
    pdfPath = Path(os.getcwd()).joinpath(pdfFilename)
    while has_handle(pdfPath):
      time.sleep(1)
    
    # Move file
    shutil.move(pdfFilename, pdfDestination)  
