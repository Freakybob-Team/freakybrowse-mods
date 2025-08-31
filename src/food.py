# Food, a package manager in Python.

# 2025 Freakybob Team. Licensed under GPL-3.0.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import argparse
import urllib.request
import os
parser = argparse.ArgumentParser(prog='Food', description='A package manager in Python')
parser.add_argument('--i') # install + package (ex: --i greg)
parser.add_argument('--t') # download temp then delete
parser.add_argument('--ar') # autorun
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