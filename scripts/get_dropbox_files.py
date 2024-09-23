import dropbox
from upload import get_access_token
import pandas as pd

def list_files_in_dropbox_folder(folder_path, dbx):
    """
    List files in a Dropbox folder and return as a pandas DataFrame.
    """
    files_data = []

    try:
        # If folder_path is root, pass an empty string
        if folder_path == "/":
            folder_path = ""

        # List all files in the given Dropbox folder
        result = dbx.files_list_folder(folder_path)

        files_data.extend(
            {
                "Name": entry.name,
                "Client_Mod": entry.client_modified,
                "Server_Mod": entry.server_modified,
            }
            for entry in result.entries
            if isinstance(entry, dropbox.files.FileMetadata)
        )
    except dropbox.exceptions.ApiError as err:
        print(f"Failed to list folder contents: {err}")

    return pd.DataFrame(files_data)



def get_dropbox_files(music_folder_path, acess_token_path):
    """
    Main function to get files from Dropbox and display the DataFrame.
    """
    # Replace with your Dropbox access token
    ACCESS_TOKEN = get_access_token(acess_token_path)

    # Connect to Dropbox
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    return list_files_in_dropbox_folder(music_folder_path, dbx)