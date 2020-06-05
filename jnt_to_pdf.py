"""
Convert all .jnt files in my machine to .pdf bc Windows Journal is deprecated.
1. Identify all .jnt files in my documents
2. Print each one to PDF as "filename-jnt.pdf" in same location
3. Delete .jnt file afger printing to PDF (optional)
"""

# DONE: Provide output file name as argument
# DONE: Print file from a different folder
# DONE: copy printed PDF to original location
# TODO: Function that identifies all jnt files in an input directory
# TODO: Make sure PDF does not already exist before printing, else the
#       Journal Note prompt to replace will break the program.
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


###########
# Inputs
###########
jntPath = "C:\\Users\\Fernando\\Documents\\a\\Note-a.jnt"
pdfFilename = Path(jntPath).stem + '-jnt.pdf' # Name PDF as "filename-jnt.pdf"
pdfDestination = Path(Path(jntPath).parent).joinpath(pdfFilename)

###########
# Outputs
###########
print_jnt(jntPath, pdfFilename)
move_pdf(pdfFilename, pdfDestination)
