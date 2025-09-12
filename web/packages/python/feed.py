import urllib.request
import os
print("Feed; a Food updater. Now downloading/updating food...")
urllib.request.urlretrieve(
    "https://food.freakybob.site/src/food.py", "food.py"
)
urllib.request.urlretrieve(
    "https://food.freakybob.site/src/eat.py", "eat.py"
)
urllib.request.urlretrieve(
    "https://food.freakybob.site/src/cook.py", "cook.py"
)
print("Downloaded Food, Eat and Cook! Thanks for using Feed.")