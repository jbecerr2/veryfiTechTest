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


#documents folder path
docs_path = "/home/jmb/Documents/Projects/Tech_tests/veryfiTechTest/docs/"

