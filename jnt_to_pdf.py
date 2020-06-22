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
# TODO: Document handle function.
# TODO: Remove superfluos libraries

###########
# Libraries
###########

# from ahk import AHK # ahk run does not allow for passing args
import os
import time
import shutil
from pathlib import Path
import subprocess
import psutil

###########
# Functions
###########

def find_jnt_paths(rootDirectory):
  """
  Searches iteratively in the root directory for all .jnt files.
  Inputs:
  - A root directory
  Outputs:
  - A list of full paths to all Journal Note files under root directory. 
  """
  list_jnt_paths = []
  for root, dirs, files in os.walk(rootDirectory):
    for file in files:
        if file.endswith(".jnt"):
             list_jnt_paths.append(os.path.join(root, file))
  return list_jnt_paths


def print_jnt(inputPath, outputFilename):
    """
    Inputs:
    - A string with the absolute path to a jnt file
    - A string with the output filename only (excluding path)
    Ouput:
    - A pdf printout of the file, saved in the location where the
    user last printed from JournalNote to PDF manually.  Assumes it is
    the working directory where this program is saved.
    """
    # Remove double quotes in outputFilename
    temp = Path(outputFilename.strip('"'))
    # if the file exists in the working directory prompt user to delete file
    if Path.is_file(temp):
      userInput = input("File " + outputFilename + " already exists. Do you want to delete it? (y/n)")
      if userInput == 'y':
        Path.unlink(temp) # Delete file
      elif userInput == 'n':
        raise SystemExit('The program will abort')
      else:
        raise SystemExit('That was not a valid entry. The program will abort.')
    subprocess.run(['powershell.exe', './jnt_to_pdf.ahk',
                    inputPath, outputFilename])


def move_pdf(sourceFileName, destinationPath):
    """
    Moves the PDF to the location of the Journal Note.  
    Inputs:
    - Name of printed PDF file located in default printing directory
    - Destination filepath
    Outputs:
    - None
    """
    # There are two latencies when printin to PDF
    # First, it takes a short time to create the PDF file file address in the 
    # directory. Initially this will be a file with 0 bytes.
    # Second, it can take minutes for a big file to print. When done it will have > 0 bytes.

    # Check file has been created
    seconds = 0
    timeLimit = 10 # maximum printing time in seconds. Abort if longer.
    while not Path(sourceFileName).is_file(): 
      time.sleep(1)
      seconds += 1
      #  Abort if taking longer than timeLimit seconds to print
      if seconds == timeLimit:
        raise SystemExit("File " + sourceFileName + " has taken more than " + timeLimit + " to be created.  The program will abort.")
    else:
      print('Waited {} seconds for file {} to be created'.format(seconds, sourceFileName))

    # Check if file already exists in destination path
    fullPath = Path(destinationPath).joinpath(sourceFileName)
    if Path.is_file(fullPath):
      raise SystemExit("A PDF file with the same name already exists in the destination folder. Program will abort.")

    # Check file has finished printing before moving.
    # File size is == 0 until done printing.
    #time.sleep(1)
    while os.stat(sourceFileName).st_size == 0:
      time.sleep(1)
    has_handle(r'C:\Users\Fernando\Documents\a\Note-a.pdf')
    while True:
      try:
        shutil.move(sourceFileName, destinationPath)
        break
      except WindowsError:
        time.sleep(1)

def has_handle(fpath):
  for proc in psutil.process_iter():
    try:
      for item in proc.open_files():
        if fpath == item.path:
          return True
    except Exception:
      pass
  return False

###########
# Inputs
###########

# Enter the root directory that you want to search for journal note files.
jntRoot = "C:\\Users\\Fernando\\Documents\\a"


###########
# Outputs
###########

# Find all jnt files in the root directory and return them in a list
jntPathList = find_jnt_paths(jntRoot)

# Loop over the list of jnt file paths
for i in jntPathList:
    # Adding double quotes so we can pass paths with spaces to AHK script
    pdfFilename = "\"" + Path(i).stem + "-jnt.pdf\""
    jntPath = "\"" + i + "\""

    # Print the .jnt file to pdf in default directory
    print_jnt(jntPath, pdfFilename)

    # Move printed PDF file to location of the source .jnt file.
    pdfFilename = Path(i).stem + "-jnt.pdf"
    pdfDestination = Path(i).parent
    move_pdf(pdfFilename, pdfDestination)
