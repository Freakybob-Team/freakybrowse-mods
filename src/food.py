import argparse
import urllib.request
import os
import json
import sys

parser = argparse.ArgumentParser(prog='Food', description='A package manager in Python')
parser.add_argument('--i')
#parser.add_argument('--t') - coming soon once again
args = parser.parse_args()

with urllib.request.urlopen("https://food.freakybob.site/autumn/food.json") as url:
    data = json.load(url)
    print("Packages fetched! [autumn]")
if (args.i in data["packages"]):
    print("Package found!")
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/Freakybob-Team/food/refs/heads/main/packages/python/" + args.i + ".py", args.i + ".py"
    )
    print("Package downloaded!")
    print("The package will now run.")
    print("-----")
    with open(args.i + ".py") as file:
        exec(file.read())
else:
    sys.exit("Package not found. Food will now exit.")