#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir% ; sets working directory to script location

input_file_path := A_Args[1] ; assign jnt full file path from first element of incoming parameter array (A_Args)
output_file_name := A_Args[2] ; assign pdf filename from second element of A_Args 
Run, print %input_file_path% ; print file
WinWait, Windows Journal ahk_class #32770 ; wait for window to open
SendInput, y ; click yes in popup and dismiss it
WinWait, Save Print Output As ahk_class #32770 ; wait for dialog to activate
SendInput, {raw} %output_file_name% ; send output file name
SendInput, {Enter} ; Hit enter to save in last folder Journal Note saved a PDF