import argparse
import install
parser=argparse.ArgumentParser()
parser.add_argument('-i', 
                    nargs=1, 
                    action="store")
args=parser.parse_args()
if args.i is not None:
    install.install(args.i[0])
