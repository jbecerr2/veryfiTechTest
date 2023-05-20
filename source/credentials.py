"""
This module loads the API credentials from the environment file, checks if they're corerectly loaded, and returns them once the function is called
"""
import os
from dotenv import load_dotenv

def load_veryfi_credentials(env_file):
    
    load_dotenv(env_file)

    client_id = os.getenv("VERYFI_CLIENT_ID")
    client_secret = os.getenv("VERYFI_CLIENT_SECRET")
    username = os.getenv("VERYFI_USERNAME")
    api_key = os.getenv("VERYFI_API_KEY")

    if not all([client_id, client_secret, username, api_key]):
        raise ValueError("Error: Failed to load Veryfi API credentials, please check the .env file")

    print("Veryfi credentials loaded successfully")

    return client_id, client_secret, username, api_key

