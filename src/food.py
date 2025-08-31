import argparse
import urllib.request
parser = argparse.ArgumentParser(prog='Food', description='A package manager in Python')
parser.add_argument('--i', '--install') # install + package
args = parser.parse_args()
if (args.i == "greg"):
    urllib.request.urlretrieve("", args.i + ".py")