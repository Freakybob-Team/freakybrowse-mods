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

# NOTICE: By running this program, you consent to giving us ANONYMOUS error data via Sentry. Your data is stored in Sentry's European Union (EU) dataset.

import argparse
import urllib.request
import os
import sentry_sdk

sentry_sdk.init(
    dsn="https://102fa20c466815ea763d8a025201ec3c@o4509941003452416.ingest.de.sentry.io/4509941171748944",
    send_default_pii=False,
)

parser = argparse.ArgumentParser(prog='Food', description='A package manager in Python')
parser.add_argument('--i')
parser.add_argument('--t')
args = parser.parse_args()
if args.i:
    if args.i in ["greg"]:
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/Freakybob-Team/food/refs/heads/main/packages/python/" + args.i + ".py",
            args.i + ".py"
        )
if args.i:
    if args.i in ["food"]:
        urllib.request.urlretrieve(
            "https://freakybob-team.github.io/food/src/food.py",
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
