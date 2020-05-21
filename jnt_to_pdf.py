#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Convert all .jnt files in my machine to .pdf bc Windows Journal is deprecated.
1. Identify all .jnt files in my documents
2. Print each one to PDF as "name-jnt.pdf" in same location
3. Delete .jnt version
"""

###########
# Libraries
###########

from ahk import AHK
import os
import subprocess

###########
# Functions
###########
def print_jnt(jntPath):
    """
    Input: A string with the location of a jnt file
    Ouput: A pdf printout of the file, in the same location, with the same name 
    """
    # TODO: bring over the .ahk function 
    return XYZ
ahk = AHK()
# ahk run does not take args!!!
# Will need to use powershell

var1 = 'var11'
var2 = 'var22'
subprocess.run(['powershell.exe', './test.ahk', var1, var2])

###########
# Inputs
###########

###########
# Outputs
###########
