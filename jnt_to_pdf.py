"""
Convert all .jnt files in my machine to .pdf bc Windows Journal is deprecated.
1. Identify all .jnt files in my documents
2. Print each one to PDF as "name-jnt.pdf" in same location
3. Delete .jnt file
"""

# DONE: Provide output file name as argument
# TODO: Print file from a different folder, copy printed PDF to original location, and delete PDF in working directory.
# TODO: Function that identifies all jnt files in an input directory
# TODO: Make sure PDF does not already exist before printing, else the Journal Note prompt to replace will break the program.

###########
# Libraries
###########
# TODO: Remove all unneeded libraries
# from ahk import AHK # ahk run does not take args!!!
import os
from pathlib import Path
import subprocess

###########
# Functions
###########
def print_jnt(inputPath, outputFilename):
    """
    Inputs: 
      - A string with the absolute path to a jnt file
      - A string with the output filename (not path)
    Ouput: 
      - A pdf printout of the file, saved in the last location JournalNote sprinted to PDF manually. Need to set it manually to current directory before running for first time.
    """
    subprocess.run(['powershell.exe', './jnt_to_pdf.ahk', inputPath, outputFilename])
    return inputPath

###########
# Inputs
###########
jntPath = "C:\\Users\\Fernando\\Documents\\scripts\\print_journal_notes\\Note1.jnt"

###########
# Outputs
###########
pdfFilename = Path(jntPath).stem + '-jnt' # Name PDF as "name-jnt.pdf"
print_jnt(jntPath, pdfFilename)