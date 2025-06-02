import os
import shutil
from pathlib import Path

# Access the download folder of system
downloads = Path.home() / "Downloads"

# Dictionary of known extensions
knownExtensions = {".pdf" : ".pdf",
                   ".exe" : ".exe",
                   ".msi" : ".msi"}

# loop through the download folder and only search for .pdf files and exclude folders
# .iterdir() is needed to loop through the paths
for i in downloads.iterdir():

    # i.is_file only checks for files
    # i.suffix only checks for the file type
    if i.is_file() and i.suffix == '.pdf':

        # shutil.move will move the file
        # first specify the files that will move (i - the source)
        # and then specify where they will move to (the destination)
        shutil.move(i, Path.home() / "Downloads" / ".pdf")

# loop through the download folder and only search for .exe files and exclude folders
for i in downloads.iterdir():

    if i.is_file() and i.suffix == '.exe':
        shutil.move(i, Path.home() / "Downloads" / ".exe")
