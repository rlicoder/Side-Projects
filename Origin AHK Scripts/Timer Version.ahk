#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

sleep, 75000
Loop, 20
{
	BlockInput, On
	SendInput {Escape}
	sleep, 100
	#CommentFlag Move the mouse to the Origin (You must fix the Origin window yourself)
	MouseMove, 1985, 20, 0
	MouseClick

	#CommentFlag Move to Offline
	MouseMove 0, 200, 0, R
	sleep, 150
	MouseClick

	#CommentFlag Move back to origin window
	MouseMove, 0, -200, 0, R
	sleep, 150
	MouseClick

	#CommentFlag Move to Online
	MouseMove 0, 200, 0, R
	sleep, 150
	MouseClick
	
	#CommentFlag Only works for 2 1080p monitors and apex legends is the 11th thing on the taskbar
	#CommentFlag Goes to the Apex session and clicks on it
	MouseMove, -980, 850, 0, R
	MouseClick
	
	#CommentFlag Move to the continue button
	MouseMove, -50, -370, 0, R
	sleep, 250
	MouseClick
	sleep, 150
	
	#CommentFlag Rejoining clicks
	MouseClick
	sleep, 150
	MouseClick
	sleep, 150
	MouseClick
	
	BlockInput, Off
	sleep, 70000
}

#CommentFlag Shift + Escape Kill Switch
+Escape::ExitApp
