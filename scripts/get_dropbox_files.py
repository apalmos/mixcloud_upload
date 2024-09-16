'''get files from Dropbox'''

import dropbox
from upload import get_access_token

# Replace with your Dropbox access token
ACCESS_TOKEN = get_access_token("dropbox_access_token")

# Connect to Dropbox
dbx = dropbox.Dropbox(ACCESS_TOKEN)

def list_files_in_dropbox_folder(folder_path):
    try:
        # List all files in the given Dropbox folder
        result = dbx.files_list_folder(folder_path)
        for entry in result.entries:
            print(entry.name)
    except dropbox.exceptions.ApiError as err:
        print(f"Failed to list folder contents: {err}")

# Specify the Dropbox folder path (use '' for root)
folder_path = '/your_folder_path'
list_files_in_dropbox_folder(folder_path)
