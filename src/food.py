import argparse
import eat
import cook
helpstring = """
here's an example of downloading a python app: python3 food.py --i greg --type text
here's an example of downloading a text file: python3 food.py --i greg --type python
formatting: [your python name, ex: python3 or py] food.py --i [packagename] --[type] [python or text]"""
parser = argparse.ArgumentParser(prog='Food', description='A package manager in Python', epilog=helpstring)
parser.add_argument('--i')
parser.add_argument('--t')
parser.add_argument('--type')
args = parser.parse_args()
if args.type == "python":
    print("using python downloads")
    eat.python(args)
if args.type == "text":
    print("using txt downloads")
    eat.txt(args)
if args.t:
    print("using temp downloads; python")
    cook.cookpy(args)