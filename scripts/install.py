import requests
import os
import urllib.request 
import shutil
import minecraft_launcher_lib
import ctypes

Dirs=(".portaluna/game",".portaluna/licenses",".portaluna/jre")
max_value = [0]

def AssetIndex(Version):
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

    return MCVersion 

def InstallLC(Version):
    MCVersion=AssetIndex(Version)

    print("Installing Lunar Client","("+Version+")"+"...")
    for Index in range(len(Dirs)):    
        if os.path.exists(Dirs[Index]) is False:
            os.makedirs(Dirs[Index])

    if os.path.exists(Dirs[0]+"/versions/"+MCVersion) is False:
        os.makedirs(Dirs[0]+"/versions/"+MCVersion)
        VersionDir=Dirs[0]+"/versions/"+MCVersion
    else:    
        VersionDir=Dirs[0]+"/versions/"+MCVersion

    if os.path.exists(VersionDir+"/"+"natives") is False:
        os.mkdir(VersionDir+"/"+"natives")

    Params={"hwid":"0","hwid_private":"0","os":"win32","arch":"x64","launcher_version":"0","version":Version,"branch":"master","launch_type":"0","classifier":"0"} 
    Response=requests.post('https://api.lunarclientprod.com/launcher/launch',json=Params)
    Response=Response.json()
    # Artifacts
    for Index in range(len(Response.get("launchTypeData").get("artifacts"))):
        Artifact=Response.get("launchTypeData").get("artifacts")[Index].get("url")
        ArtifactName=Response.get("launchTypeData").get("artifacts")[Index].get("name")
        print("Download", ArtifactName+"...") 
        try:
            urllib.request.urlretrieve(Artifact, VersionDir+"/"+ArtifactName)
        except:    
            break 
    Natives=VersionDir+"/"+Response.get("launchTypeData").get("artifacts")[6].get("name")      
    shutil.unpack_archive(Natives,VersionDir+"/"+"natives", "zip",)

    #Licenses
    for Index in range(len(Response.get("licenses"))):
        License=Response.get("licenses")[Index].get("url")    
        LicenseName=Response.get("licenses")[Index].get("file") 
        print("Download", LicenseName+"...") 
        try:
            urllib.request.urlretrieve(License, VersionDir+"/"+ArtifactName)
        except:    
            break  
    # Java Runtime Environment   
    if os.path.exists(Dirs[2]+"/"+Response.get("jre").get("executablePathInArchive")[0]) is False:
        print("Download Lunar Client Java Runtime...")    
        urllib.request.urlretrieve(Response.get("jre").get("download").get("url"), Dirs[2]+"/"+Response.get("jre").get("executablePathInArchive")[0]+"."+Response.get("jre").get("download").get("extension"))
        print("Extract Lunar Client Java Runtime...")
        shutil.unpack_archive(Dirs[2]+"/"+Response.get("jre").get("executablePathInArchive")[0]+"."+Response.get("jre").get("download").get("extension"), Dirs[2], "zip")
        os.remove(Dirs[2]+"/"+Response.get("jre").get("executablePathInArchive")[0]+"."+Response.get("jre").get("download").get("extension"))

def InstallMC(Version):
    Version=AssetIndex(Version)
    callback = {"setStatus": lambda text: print(text+"..."),"setProgress": lambda value: printProgressBar(value, max_value[0]),"setMax": lambda value: maximum(max_value, value)} 
    print ("Installing", "("+Version+")"+"...")       
    minecraft_launcher_lib.install.install_minecraft_version(Version, Dirs[0], callback=callback)

def Install(Version):
    ctypes.windll.kernel32.SetConsoleTitleW("Installing Minecraft ("+AssetIndex(Version)+")...")
    InstallMC(Version)
    print("")
    ctypes.windll.kernel32.SetConsoleTitleW("Installing Lunar Client ("+Version+")...")
    InstallLC(Version)
    print("Finished!")

def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=0, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(0 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    if iteration == total:
        print()

def maximum(max_value, value):
    max_value[0] = value              
