import minecraft_launcher_lib as MCLib
import os
max_value = [0]

def install(Version):
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
    runtime()
    print ("Installing", "("+Version+")"+"...")       
    MCLib.install.install_minecraft_version(Version, ".minecraft_files", callback=callback)  

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

def runtime():
    max_value = [0]

    callback = {
        "setStatus": lambda text: print(text+": "),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value)
    } 
    if os.path.isdir(".minecraft_files\\runtime\\java-runtime-beta") is False:
        print("Installing Java...")
        MCLib.runtime.install_jvm_runtime("java-runtime-beta",".minecraft_files", callback=callback)
    else:
        print("Java is Installed.")   
        
