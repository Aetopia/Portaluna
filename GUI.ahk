;File Description
;@Ahk2Exe-SetName Lunar Client Mini
;@Ahk2Exe-SetDescription Lunar Client Mini
;@Ahk2Exe-SetVersion 1.0.0

#NoEnv
SetBatchLines -1
ListLines Off
SendMode Input
#NoTrayIcon
SetWorkingDir %A_ScriptDir%
#SingleInstance, Force
Files()
global AssetIndex=0
Gui, New
Gui -MinimizeBox +Border
Gui, Font, s10
Gui, Add, Tab3, +0x1000 +0x40 +0x400 -0x800 +0x8000 w480 h380, Launch|Settings|About
Gui, Tab, 1
Gui, Add, Button, x151 y125 w200 h50 +Default vLaunch gLaunch, Launch
Gui, Font, s8
Gui, Add, DropDownList, w100 h110 x152 y180 vVersionList gVersionWrite,  1.7|1.8|1.12|1.16|1.17|1.18
VersionSelect()
Gui, Font, s9
Gui, Add, Button, w96 h23 x255 y179 vInstall_Update gInstall_Update, Install/Update
Gui, Font, s8
Gui, Tab, 2
Gui, Add, Text,, Edit Lunar Client Mini's Config File.
Gui, Add, Button, h25 w75 vEdit gEdit, Edit
Gui, Add, Text,, Reset Lunar Client Mini.
Gui, Add, Button, h25 w75 vReset gReset, Reset 
Gui, Tab,3
Gui, Add, Text,, Lunar Client Mini made by Aetopia.
Gui, Add, Link,, GitHub Repository: <a href="https://github.com/Aetopia/Lunar-Client-Portable">https://github.com/Aetopia/Lunar-Client-Mini</a>
Gui, Add, Link,, Join CTT: <a href="https://discord.gg/CTT">https://discord.gg/CTT</a>
Gui, Show, w500 h400, Lunar Client Mini

Edit(){
	RunWait, execute.exe,, Hide
	Run, Options.ini
}

Reset(){
	FileDelete, LauncherConfig.ini
	FileDelete, Options.ini
	Reload
}	

Launch(){
	IniRead, Selected_Version, LauncherConfig.ini, Main, Version
	RunWait, execute.exe -v %Selected_Version%,, Hide
	ExitApp
}	

Install_Update(){
	VersionSelect()
	IniRead, Selected_Version, LauncherConfig.ini, Main, Version
	RunWait, execute.exe -i %AssetIndex%
	MsgBox, 64, Finished!, LC %Selected_Version% Installed/Updated.
}	

VersionWrite(){
    GuiControlGet, Selected_Version,, VersionList
	IniWrite, %Selected_Version%, LauncherConfig.ini, Main, Version
}

VersionSelect(){
    IniRead, Selected_Version, LauncherConfig.ini, Main, Version
	If (Selected_Version = 1.7) 
	{
		GuiControl, Choose, VersionList, 1
		global AssetIndex="1.7.10"
	}	
	Else If (Selected_Version = 1.8) 
	{
		GuiControl, Choose, VersionList, 2
		global AssetIndex="1.8.9"
	}
	Else If (Selected_Version = 1.12) 
	{
		GuiControl, Choose, VersionList, 3
		global AssetIndex="1.12.2"
	}
	Else If (Selected_Version = 1.16) 
	{
		GuiControl, Choose, VersionList, 4
		global AssetIndex="1.16.5"
	}
	Else If (Selected_Version = 1.17) 
	{
		GuiControl, Choose, VersionList, 5
		global AssetIndex="1.17.1"
	}
    Else If (Selected_Version = 1.18) 
	{
		GuiControl, Choose, VersionList, 6
		global AssetIndex="1.18.1"
	}
	return
}

Files(){
	IfNotExist, LauncherConfig.ini
		IniWrite, 1.8, LauncherConfig.ini, Main, Version
}	

GuiClose(){
	ExitApp
}	