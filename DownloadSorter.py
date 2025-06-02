import os
import shutil
from pathlib import Path

# Access the download folder of system
downloads = Path.home() / "Downloads"

def sort_files(file):

    # loop through the download folder and only search for .pdf files and exclude folders
    # .iterdir() is needed to loop through the paths
    for i in downloads.iterdir():

        # i.is_file only checks for files
        # i.suffix only checks for the file type
        if i.is_file():

            # variable to store file extensions
            extension = file.suffix

            if extension:

                # name the folder after the extension
                folder_name = extension

                # the file path for the extension
                folder_path = downloads / folder_name

                # make the new directory
                folder_path.mkdir(exist_ok=True)


        # shutil.move will move the file
        # first specify the files that will move (i - the source)
        # and then specify where they will move to (the destination)
        shutil.move(str(i), str(Path.home() / "Downloads"))
