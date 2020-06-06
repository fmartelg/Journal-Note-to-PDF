"""
Convert all .jnt files in my machine to .pdf bc Windows Journal is deprecated.
1. Identify all .jnt files in my documents
2. Print each one to PDF as "filename-jnt.pdf" in same location
3. Delete .jnt file afger printing to PDF (optional)
"""

# DONE: Provide output file name as argument
# DONE: Print file from a different folder
# DONE: copy printed PDF to original location
# DONE: Function that identifies all jnt files in an input directory
# TODO: Make sure PDF does not already exist before printing, else the
#       Journal Note prompt to replace will break the program.
# TODO: Check that there is a PDF version of each jnt in each directory
# TODO: Delete PDF in working directory.

###########
# Libraries
###########
# TODO: Remove all unneeded libraries
# from ahk import AHK # ahk run does not take args!!!
import os
import shutil
from pathlib import Path
import subprocess

###########
# Functions
###########


def print_jnt(inputPath, outputFilename):
    """
    Inputs:
      - A string with the absolute path to a jnt file
      - A string with the output filename only (i.e. excluding path)
    Ouput:
      - A pdf printout of the file, saved in the last location JournalNote 
        sprinted to PDF manually. Need to set it manually to current directory
        before running for first time.
    """
    subprocess.run(['powershell.exe', './jnt_to_pdf.ahk',
                    inputPath, outputFilename])
    return inputPath


def move_pdf(sourceFileName, destinationPath):
    """
    After printing a Journal Note to PDF in the default printer directory, 
    this function copies the PDF to the location of the Journal Note.
    Inputs:
      - Name of source file (assumed is located in default printing directory)
      - Destination filepath
    Outputs:
      - None
    """
    filename = sourceFileName
    destination = destinationPath
    shutil.move(filename, destination)


def find_jnt_paths(rootDirectory):
  """
  Searches in the root directory and all subdirectories iteratigvely to find all .jnt files.
  Inputs:
    - A root directory
  Outputs:
    - A list of full paths to found files. 
  """
  list_jnt_paths = []
  rootDir = rootDirectory
  for root, dirs, files in os.walk(rootDir):
    for file in files:
        if file.endswith(".jnt"):
             list_jnt_paths.append(os.path.join(root, file))
  return list_jnt_paths


###########
# Inputs
###########
jntRoot = "C:\\Users\\Fernando\\Documents\\a"
jntPath = "C:\\Users\\Fernando\\Documents\\a\\Note-a.jnt"
pdfFilename = Path(jntPath).stem + '-jnt.pdf' # Name PDF as "filename-jnt.pdf"
pdfDestination = Path(Path(jntPath).parent).joinpath(pdfFilename)

###########
# Outputs
###########
jntPathList = find_jnt_paths(jntRoot)
print_jnt(jntPath, pdfFilename)
move_pdf(pdfFilename, pdfDestination)