import argparse
import urllib.request
import os
parser = argparse.ArgumentParser(prog='Food', description='A package manager in Python')
parser.add_argument('--i', '--install') # install + package (ex: --i greg)
parser.add_argument('--t', '--temp') # download temp then delete
parser.add_argument('--ar', '--ar') # autorun
args = parser.parse_args()
if (args.i == "greg"):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/Freakybob-Team/food/refs/heads/main/packages/greg.py", args.i + ".py")
if 'args.i' in globals():
    with open(args.i + ".py") as file:
        if 'args.ar' in globals():
            exec(file.read())
if (args.t == "greg"):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/Freakybob-Team/food/refs/heads/main/packages/greg.py", args.t + ".py")
with open(args.t + ".py") as file:
    exec(file.read())
    try:
        os.remove(args.t + ".py")
    except:
        print("failed to delete file")