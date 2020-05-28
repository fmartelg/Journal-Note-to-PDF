"""
Convert all .jnt files in my machine to .pdf bc Windows Journal is deprecated.
1. Identify all .jnt files in my documents
2. Print each one to PDF as "name-jnt.pdf" in same location
3. Delete .jnt file
"""

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
def print_jnt(docPath):
    """
    Input: A string with the absolute path to a jnt file
    Ouput: A pdf printout of the file, saved in the last location JournalNote sprinted to PDF manually. Set it manually to current directory!!!
    """
    subprocess.run(['powershell.exe', './jnt_to_pdf.ahk', docPath])
    return docPath

# TODO: Print file from different location, copy PDF to said location, and delete it in working directory.
# TODO: Function that identifies all jnt files in an input directory
# TODO: Make sure PDF does not already exist before printing, else the Journal Note prompt to replace will break the program.

###########
# Inputs
###########
jntPath = "C:\\Users\\Fernando\\Documents\\scripts\\print_journal_notes\\Note1.jnt"

###########
# Outputs
###########
print_jnt(jntPath)