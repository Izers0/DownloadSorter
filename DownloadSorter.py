import shutil
from pathlib import Path
from plyer import notification
from datetime import datetime

time = datetime.now()
currentTime = time.strftime("%H:%M")

# Access the download folder of system
downloads = Path.home() / "Downloads"

def sort_files():

    # loop through the download folder and only search for .pdf files and exclude folders
    # .iterdir() is needed to loop through the paths
    for i in downloads.iterdir():

        # i.is_file only checks for files
        # i.suffix only checks for the file type
        if i.is_file():

            # variable to store file extensions
            extension = i.suffix

            if extension:

                # name the folder after the extension
                # [1:] removes the . from the folder name
                folder_name = extension[1:]

                # the file path for the extension
                folder_path = downloads / folder_name

                # make the new directory
                folder_path.mkdir(exist_ok=True)

                # shutil.move will move the file
                # first specify the files that will move (i - the source)
                # and then specify where they will move to (the destination)
                shutil.move(str(i), str(folder_path / i.name))

                notification.notify(
                    title="Files Moved",
                    message=f"{i.name} -> {folder_name} at {currentTime}"
                )


sort_files()
