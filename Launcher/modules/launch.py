# Modules
import subprocess
import os
import config

Natives=os.getcwd()+"\\.lunarclient_files\\offline\\1.8\\natives"

def Launch(Version):
    # Read Values from Options.ini
    Config=config.ConfigRead(Version)
    # Set the Asset Index
    if Version=="1.7":
        AssetIndex="1.7.10"
    else:
        AssetIndex=Version		
    # Launch Variable  
    Launch_1=[Config[0],
	"--add-modules",
	"jdk.naming.dns",
	"--add-exports",
	"jdk.naming.dns/com.sun.jndi.dns=java.naming",
	"-Djna.boot.library.path="+Natives,
	"--add-opens",
	"java.base/java.io=ALL-UNNAMED"]
    Launch_2=["-Djava.library.path="+Natives,
        "-XX:+DisableAttachMechanism",
	"-cp",
	".lunarclient_files\\offline\\"+Version+"\\lunar-assets-prod-1-optifine.jar;"
	+".lunarclient_files\\offline\\"+Version+"\\lunar-assets-prod-2-optifine.jar;"
	+".lunarclient_files\\offline\\"+Version+"\\lunar-assets-prod-3-optifine.jar;"
	+".lunarclient_files\\offline\\"+Version+"\\lunar-libs.jar;"
	+".lunarclient_files\\offline\\"+Version+"\\lunar-prod-optifine.jar;"
	+".lunarclient_files\\offline\\"+Version+"\\OptiFine.jar;"
	+".lunarclient_files\\offline\\"+Version+"\\vpatcher-prod.jar",
	"com.moonsworth.lunar.patcher.LunarMain",
	"--version",
	str(Version),
	"--accessToken",
	"0", 
	"--assetIndex",
	str(AssetIndex),
	"--userProperties",
	"{}",
	"--gameDir",
	".minecraft\\"+Version,
	"--width",
	"854",
	"--height",
	"480",
	"--assetsDir",
	".minecraft_files\\assets"]

    Launch=Launch_1+Config[1]+Launch_2
    subprocess.Popen(Launch)
