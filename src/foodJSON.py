import argparse
import urllib.request
import os
import sentry_sdk
import json
import sys

parser = argparse.ArgumentParser(prog='Food', description='A package manager in Python')
parser.add_argument('--i')
parser.add_argument('--t')
args = parser.parse_args()

with urllib.request.urlopen("https://food.freakybob.site/autumn/food.json") as url:
    data = json.load(url)
    print("Packages fetched! [autumn]")
if (args.i in data["packages"]):
    urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/Freakybob-Team/food/refs/heads/main/packages/python/" + args.i + ".py", args.i + ".py"
    )
else:
    sys.exit("Package not found. Food will now exit.")