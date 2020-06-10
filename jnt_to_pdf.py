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
# TODO: Check that there is a PDF version of each jnt in each directory
# TODO: Delete PDF in working directory.
# TODO: Remove superfluos libraries

###########
# Libraries
###########

# from ahk import AHK # ahk run does not allow for passing args
import os
import shutil
from pathlib import Path
import subprocess

###########
# Functions
###########

def find_jnt_paths(rootDirectory):
  """
  Searches in the root directory and all subdirectories iteratigvely to find
  all .jnt files.
  Inputs:
    - A root directory
  Outputs:
    - A list of full paths to found Journal Note files. 
  """
  list_jnt_paths = []
  rootDir = rootDirectory
  for root, dirs, files in os.walk(rootDir):
    for file in files:
        if file.endswith(".jnt"):
             list_jnt_paths.append(os.path.join(root, file))
  return list_jnt_paths


def print_jnt(inputPath, outputFilename):
    """
    Inputs:
      - A string with the absolute path to a jnt file
      - A string with the output filename only (i.e. excluding path)
    Ouput:
      - A pdf printout of the file, saved in the location where the user
        last printed from JournalNote to PDF manually.  Assumes it is 
        the working directory where this oprogram is saved.
    """
    # Remove double quotes in outputFilename
    temp = Path(outputFilename.strip('"'))
    if Path.is_file(temp): # if the file exists in the working directory
      # Prompt user to delete file
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
    After printing a Journal Note to PDF in the default printer directory, 
    this function moves the PDF to the location of the Journal Note.
    Inputs:
      - Name of printed PDF file located in default printing directory
      - Destination filepath
    Outputs:
      - None
    """
    # Check if file already exists in destination path
    fullPath = Path(pdfDestination).joinpath(pdfFilename)
    if Path.is_file(fullPath): # If file already exists
      raise SystemExit("A PDF file with the same name already exists in the destination folder. Program will abort.")
    else:
      # Move file
      shutil.move(sourceFileName, destinationPath)


###########
# Inputs
###########

# Enter the root directory that you want to search for journal note files.
jntRoot = "C:\\Users\\Fernando\\Documents\\a\\b"
# pdfDestination = Path(Path(jntPath).parent).joinpath(pdfFilename)

###########
# Outputs
###########

jntPathList = find_jnt_paths(jntRoot)
for i in jntPathList:
    # Print the .jnt file to pdf in default directory
    # add double quotes so we can pass paths with spaces to AHK script
    pdfFilename = "\"" + Path(i).stem + "-jnt.pdf\""
    jntPath = "\"" + i + "\""
    print_jnt(jntPath, pdfFilename)

    # Move printed PDF file to location of the source .jnt file.
    pdfFilename = Path(i).stem + "-jnt.pdf"
    pdfDestination = Path(i).parent
    move_pdf(pdfFilename, pdfDestination)

    