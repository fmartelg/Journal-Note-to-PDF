#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

Run, print "C:\Users\Fernando\Documents\scripts\print_journal_notes\Note1.jnt" ; print file
WinWait, Windows Journal ahk_class #32770 ; wait for window to open
SendInput, y ; click yes in popup and dismiss it
WinWait, Save Print Output As ahk_class #32770 ; wait for dialog to activate
SendInput, {raw} qqqqqq ; send file name
SendInput, {Enter} ; Hit enter to save