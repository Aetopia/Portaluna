#Modules
import sys
sys.path.insert(1, 'modules')
import argparse
import launch
import config
import subprocess
import os
import ctypes
try:
    os.mkdir(".minecraft")
except:
    pass
#Checks if Options.ini exists or not.
config.ConfigExist()
#CLI Arguments
parser=argparse.ArgumentParser()
command=parser.add_mutually_exclusive_group(required=True)
command.add_argument('-v','-version',
                     action="store",
                     nargs=1,
                     metavar=("<Version>"))
args = parser.parse_args()

#Arguments
if args.v != None:
    launch.Launch(str(args.v[0])) 
