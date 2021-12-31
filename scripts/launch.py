# Modules
import subprocess
import os
import config
def Launch(Version):
    MCVersion=""
    if Version=="1.7":
        MCVersion="1.7.10" 
    elif Version=="1.8":
        MCVersion="1.8.9"
    elif Version=="1.12":
        MCVersion="1.12.2" 
    elif Version=="1.16":
        MCVersion="1.16.5"
    elif Version=="1.17":
        MCVersion="1.17.1"
    elif Version=="1.18":
        MCVersion="1.18.1"
    # Read Values from Options.ini
    Config=config.ConfigRead(Version)
    VersionDir=os.getcwd()+"/.portaluna/game/versions/"+MCVersion
    # Set the Asset Index
    if Version=="1.7":
        AssetIndex="1.7.10"
    else:
        AssetIndex=Version		
    # Launch Variable  
    Launch=[Config[0],"--add-modules",
	"jdk.naming.dns",
	"--add-exports",
	"jdk.naming.dns/com.sun.jndi.dns=java.naming",
	"-Djna.boot.library.path="+VersionDir+"/natives",
	"-Dlog4j2.formatMsgNoLookups=true",
	"--add-opens","java.base/java.io=ALL-UNNAMED"]+Config[1]+["-Djava.library.path="+VersionDir+"/natives",
	"-XX:+DisableAttachMechanism","-cp",
	VersionDir+"/lunar-assets-prod-1-optifine.jar;"
	+VersionDir+"/lunar-assets-prod-2-optifine.jar;"
	+VersionDir+"/lunar-assets-prod-3-optifine.jar;"
	+VersionDir+"/lunar-libs.jar;"
	+VersionDir+"/lunar-prod-optifine.jar;"
	+VersionDir+"/OptiFine.jar;"
	+VersionDir+"/vpatcher-prod.jar",
	"com.moonsworth.lunar.patcher.LunarMain",
	"--version",str(Version),
	"--accessToken","0", 
	"--assetIndex",str(AssetIndex),
	"--userProperties","{}",
	"--gameDir", ".minecraft\\"+Version,
	"--width","854",
	"--height","480",
	"--assetsDir",".portaluna/game/assets"]
    subprocess.Popen(Launch)
