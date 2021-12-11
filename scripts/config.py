# Modules
import os
import configparser

#Variables


# Check if "Options.ini" exists or not.
def ConfigExist():
    if os.path.isfile("Options.ini") is False:
        ConfigCreate()
        
# Create a "Options.ini" file.    
def ConfigCreate():
    config = configparser.ConfigParser()
    config['Java'] = {'Arguments': "-Xms3G -Xmx3G -Xmn1G -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M",
                      '1.7 Java': ".lunarclient_files\\jre\\zulu17.30.15-ca-fx-jre17.0.1-win_x64\\bin\\javaw.exe",
                      '1.8 Java': ".lunarclient_files\\jre\\zulu17.30.15-ca-fx-jre17.0.1-win_x64\\bin\\javaw.exe",
                      '1.12 Java': ".lunarclient_files\\jre\\zulu17.30.15-ca-fx-jre17.0.1-win_x64\\bin\\javaw.exe",
                      '1.16 Java': ".lunarclient_files\\jre\\zulu17.30.15-ca-fx-jre17.0.1-win_x64\\bin\\javaw.exe",
                      '1.17 Java': ".lunarclient_files\\jre\\zulu17.30.15-ca-fx-jre17.0.1-win_x64\\bin\\javaw.exe",
                      '1.18 Java': ".lunarclient_files\\jre\\zulu17.30.15-ca-fx-jre17.0.1-win_x64\\bin\\javaw.exe",
                      }
    with open('Options.ini', 'w') as configfile:
        config.write(configfile)
        
# Read Values from "Options.ini".       
def ConfigRead(Version):
    ConfigExist()
    config = configparser.ConfigParser()
    config.read('Options.ini')
    Arguments_String=config['Java']["Arguments"]
    Arguments_List=Arguments_String.split()
    # 1.7
    if Version=="1.7":
        Java_Path=config['Java']["1.7 Java"]
        
    # 1.8    
    elif Version=="1.8":
        Java_Path=config['Java']["1.8 Java"]
        
    # 1.12    
    elif Version=="1.12":
        Java_Path=config['Java']["1.12 Java"]
        
    # 1.16    
    elif Version=="1.16":
        Java_Path=config['Java']["1.16 Java"]
        
    # 1.17    
    elif Version=="1.17":
        Java_Path=config['Java']["1.17 Java"]
        
    # 1.18    
    elif Version=="1.18":
        Java_Path=config['Java']["1.18 Java"]

    # Return Values
    return [Java_Path, Arguments_List]
