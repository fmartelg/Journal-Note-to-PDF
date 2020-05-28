#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir% ; sets working directory to script location

file_to_print := A_Args[1] ; assign variable from first element of incoming parameter array A_Args
Run, print %file_to_print% ; print file
WinWait, Windows Journal ahk_class #32770 ; wait for window to open
SendInput, y ; click yes in popup and dismiss it
WinWait, Save Print Output As ahk_class #32770 ; wait for dialog to activate
SendInput, {raw} qqqqqq ; send file name
SendInput, {Enter} ; Hit enter to save in last folder Journal Note saved a PDF