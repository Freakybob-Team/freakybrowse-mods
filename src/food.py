import argparse
import eat
helpstring = """
here's an example of downloading a python app: python3 food.py --i greg --py yes
here's an example of downloading a text file: python3 food.py --i greg --txt yes
formatting: [your python name, ex: python3 or py] food.py --i [packagename] --[type] [anything here, --type just needs something after it]"""
parser = argparse.ArgumentParser(prog='Food', description='A package manager in Python', epilog=helpstring)
parser.add_argument('--i')
#parser.add_argument('--t') - coming soon once again
parser.add_argument('--txt')
parser.add_argument('--py')
args = parser.parse_args()
if args.py:
    print("using python downloads")
    eat.python(args)
if args.txt:
    print("using txt downloads")
    eat.txt(args)