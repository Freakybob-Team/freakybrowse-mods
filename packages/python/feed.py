import urllib.request
import os
print("Feed; a Food updater. Now updating food...")
urllib.request.urlretrieve(
    "https://food.freakybob.site/src/food.py", "food.py"
)
print("Downloaded Food! Thanks for using Feed.")
print("Removing Feed...")
os.remove("feed.py")