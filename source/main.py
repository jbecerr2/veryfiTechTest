"""
This project processes documents using the veryfi API to extract specific data and saves it to a JSON file.

main.py imports the modules and functions, loads the API credentials from an env file, and  calls the necessary functions to 
process the documents and save the data to a JSON file 

usage: /python3 main.py
"""

import os
from veryfi import Client
from credentials import load_veryfi_credentials
from doc_processor import process_documents
from extract_json import save_to_json

def main():
    
    #Paths to each file and directory
    source_dir = os.path.dirname(os.path.abspath(__file__))
    env_file = os.path.join(source_dir, "..", "envfile.env")
    docs_directory = os.path.join(source_dir, "..", "docs")
    output_path = os.path.join(source_dir, "..", "output.json")

    #Call the veryfi credentials and create the client
    client_id, client_secret, username, api_key = load_veryfi_credentials(env_file)
    veryfi_client = Client(client_id=client_id, client_secret=client_secret, username=username, api_key=api_key)

    #Process and save the data to a JSON file
    output_data = process_documents(docs_directory, veryfi_client)
    save_to_json(output_data, output_path)

if __name__ == "__main__":
    main()


