#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

Run, print "C:\Users\Fernando\Desktop\test\Note1.jnt" ; print file
;WinSet, AlwaysOnTop, Toggle, Windows Journal ; activate warning popup
WinWait, Windows Journal ahk_class #32770
;Sleep, 333 ; wait
SendInput, y ; click yes and dismiss popup
WinWait, Save Print Output As ahk_class #32770 ; wait for dialog to activate
SendInput, {raw} qqqqqq ; send file name
SendInput, {Enter}