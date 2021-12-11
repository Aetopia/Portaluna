import argparse
import sys
sys.path.insert(1, 'scripts')
import install
import launch
import config
import minecraft_launcher_lib
config.ConfigExist()
parser=argparse.ArgumentParser()
parser.add_argument('-i', 
                    nargs=1, 
                    action="store")
parser.add_argument('-v', 
                    nargs=1, 
                    action="store")
args=parser.parse_args()
if args.i is not None:
    install.Install(args.i[0])
elif args.v is not None:
    launch.Launch(args.v[0])    
