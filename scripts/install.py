import minecraft_launcher_lib as MCLib
import subprocess
max_value = [0]

def Install(Version):
    InstallLC(Version)
    InstallMC(Version)

def InstallMC(Version):
    if Version == "1.7.10" or Version == "1.8.9" or Version == "1.12.2" or Version == "1.16.5" or Version == "1.17.1" or Version == "1.18.1":
        pass
    else:
        while True:
            print("Specified Version isn't supported by LC.")
            pause=input()
            exit()

    max_value = [0]

    callback = {
        "setStatus": lambda text: print(text+": "),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value)
    } 
    print ("Installing", "("+Version+")"+"...")       
    MCLib.install.install_minecraft_version(Version, ".minecraft_files", callback=callback)

def InstallLC(Version):
    LCVersion=""
    if Version=="1.7.10":
        LCVersion="1.7"
        
    elif Version=="1.8.9":
        LCVersion="1.8"
        
    elif Version=="1.12.2":
        LCVersion="1.12"
        
    elif Version=="1.16.5":
        LCVersion="1.8"
        
    elif Version=="1.17.1":
        LCVersion="1.17"

    elif Version=="1.18.1":
        LCVersion="1.18"
        
    subprocess.run(["powershell",
                    "iex",
                    '"&',
                    '{$(irm https://raw.githubusercontent.com/Aetopia/Lunar-Client-Mini/main/LCFilesInstaller.ps1)}',
                    LCVersion+'"'])    
        
    

def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
def maximum(max_value, value):
    max_value[0] = value         
