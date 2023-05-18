import os
from veryfi import Client
from dotenv import load_dotenv
#from pathlib import Path

#Load veryfi API credentials from envfile
credentials = "envfile.env"
load_dotenv(credentials)

client_id = os.getenv("VERYFI_CLIENT_ID")
client_secret = os.getenv("VERYFI_CLIENT_SECRET")
username = os.getenv("VERYFI_USERNAME")
api_key = os.getenv("VERYFI_API_KEY")

#Check if credentials are loaded correctly
if not all([client_id, client_secret, username, api_key]):
    print("Error: Failed to load veryfi API credentials, please check envfile.env and verify your credentials")
    exit()
else:
    print("Credentials loaded successfully")
    

#Create client with the veryfi credentials
veryfi_client = Client(client_id=client_id, client_secret=client_secret, username=username, api_key=api_key)


#---------------------------------------------------------------------------------------------------------------

def check_files_in_folder(folder_name):
    # Get the directory path
    script_dir = os.path.dirname(os.path.abspath(__file__))

    #folder path
    folder_path = os.path.join(script_dir, folder_name)

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_name}' does not exist.")
        return

    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Check if there are files in the folder
    if len(files) == 0:
        print(f"No files found in the folder '{folder_name}'.")
    else:
        print(f"Files in the folder '{folder_name}':")
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            print(file_path)

# Specify the folder name
folder_name = "docs"

# Check if there are files in the folder
check_files_in_folder(folder_name)


