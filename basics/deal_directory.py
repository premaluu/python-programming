'''
    name : deal_directory.py
    Created by : Premal Upadhyay
    Date : 31-01-2022
'''

from pathlib import Path

path = Path("test")
currentPath = Path()

print(path.exists())
path.mkdir()
path.rmdir()

#Iterating Generator object.
for file in currentPath.glob("*.py"):
    print(file)