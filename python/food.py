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
parser.add_argument('--i')
parser.add_argument('--t')
args = parser.parse_args()

if args.i:
    if args.i in ["greg", "food"]:
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/Freakybob-Team/food/refs/heads/main/packages/python/" + args.i + ".py",
            args.i + ".py"
        )

if args.i:
    with open(args.i + ".py") as file:
        exec(file.read())
if args.t:
    if args.t in ["greg"]:
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/Freakybob-Team/food/refs/heads/main/packages/python/" + args.t + ".py",
            args.t + ".py"
        )

if args.t:
    with open(args.t + ".py") as file:
        exec(file.read())
    try:
        os.remove(args.t + ".py")
    except:
        print("failed to delete file")