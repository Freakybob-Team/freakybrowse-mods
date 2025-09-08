import urllib.request
import os
import json
import sys

def cookpy(args):
    with urllib.request.urlopen("https://food.freakybob.site/autumn/cook.json") as url:
        data = json.load(url)
        print("Packages fetched! [autumn, cook.json]")
    if (args.t in data["pypackages"]):
        print("Package found!")
        urllib.request.urlretrieve(
            "https://food.freakybob.site/packages/python/" + args.t + ".py", args.t + ".py"
        )
        print("Package downloaded!")
        print("The package will now run.")
        print("-----")
        with open(args.t + ".py") as file:
            exec(file.read())
            try:
                os.remove(args.t + ".py")
            except:
                print("failed to delete file")
    else:
        sys.exit("Package not found. Food will now exit.")