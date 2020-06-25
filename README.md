# Journal Note to PDF

*Journal Note to PDF* is a set of scripts for batch printing Journal Note Files (.JNT) to Portable Document Format (.PDF).

## Warning

Microsoft discontinued its Windows Journal notetaking application in 2016 "due to the Windows Journal file format (Journal Note File, or JNT) being susceptible to security exploits." ([Wikipedia](https://en.wikipedia.org/wiki/Windows_Journal), accessed 2020-06-24 21:51:06).

**Be careful opening and printing any JNT files you have not created yourself (e.g. received by email, etc).**  *Journal Note to PDF* **scripts do not check for any security exploits.** _Caveat emptor_.

## Requirements

I've only run the scripts in the following environment.

- Windows 10
- [Windows Journal](https://www.microsoft.com/en-us/download/details.aspx?id=53003) (ensure it is on the Windows path and associated with .JNT files)
- Microsoft Print to PDF (set as default printer).
- [AutoHotkey](https://www.autohotkey.com/) (ensure it is on the Windows path so it can be called from PowerShell)
- [Python 3.7.7](https://www.python.org/downloads/release/python-377/)
- [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7)

## Usage

1. Copy the following to a working directory of choice:
   1. `jnt_to_pdf.ahk`
   2. `jnt_to_pdf.py`
2. Open `jnt_to_pdf.py` and replace the the full path in quotes in the following line with the full path to the directory where your .JNT files are to be found: `python
jntRoot = "C:\\Users\\User\\Documents\\myfolder"`
3. Save `jnt_to_pdf.py`
4. Use Windows Journal to open any .JNT file.  Print it to PDF.  When prompted, select your working directory (were you placed the scripts in Step 1) as the destination for the PDF. Windows Journal will now use this directory as the default print to directory, as required by the scripts.
5. Run `jnt_to_pdf.py`.

The script will search for all .JNT files in the directory (including all its subdirectories), and store their full file paths in a list.  

It will then loop over the list, calling the AutoHotkey script `jnt_to_pdf.ahk` to print each .JNT file to .PDF in place.

(A large file can take several minutes to print.  If, like me, you have hundreds of files, expect to wait a while.)

## Why use AutoHotkey

### The problem

The legacy version of Windows Journal available from Microsoft throws up a security popup window every time it is opened.  This window needs to be dismissed by clicking "OK".  

Trying to print a .JNT file from the command line opens Windows Journal, and the irksome pop up warnings.  So we need a way  to interact with these windows programmatically.

### The Solution

Enter AutoHotkey, an automation scripting language for Windows.  Using AutoHotkey we can program a macro (much like a Visual Basic Script) so we can interact programmatically with the Windows Journal user interface (i.e the point and click windows). 

Please take a look at the script by opening `jnt_to_pdf.ahk`.  Refer to the AutoHotkey [docs](https://www.autohotkey.com/docs/AutoHotkey.htm) for reference.

(I tried using [AHK](https://pypi.org/project/ahk/), a python library that provides a wrapper around AutoHotkey, to do everythyin in Python.  However, at the time of coding, the library was not able to pass arguments to AutoHotkey, so I could not use it.)

## Project Status / Contributions

At this point I consider  the project complete. However, if you are reading this and want to contribute some improvements for the benefit of others please DM me on Twitter.  My Twitter handle is: [@fmg_twtr](https://twitter.com/fmg_twtr?lang=en)

## License

MIT 2020 Fernando Martel García
