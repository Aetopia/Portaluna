import argparse
import sys
sys.path.insert(1, 'scripts')
import install
import launch
import config
import minecraft_launcher_lib
config.ConfigExist()
parser=argparse.ArgumentParser(add_help = False)
parser.add_argument('-i', 
                    nargs=1, 
                    action="store",
                    metavar=("Version"))
parser.add_argument('-v', 
                    nargs=1, 
                    action="store",
                    metavar=("Version"))
args=parser.parse_args()
if args.i is not None:
    install.Install(args.i[0])
elif args.v is not None:
    launch.Launch(args.v[0])
else:
    pass
