import os
import shutil
from pathlib import Path

# Access the download folder of system
downloads = Path.home() / "Downloads"

# loop through the download folder and search for files and exclude folders
# .iterdir() is needed to loop through the paths
for i in downloads.iterdir():

    # i.is_file only checks for files
    if i.is_file():
        print(i)
