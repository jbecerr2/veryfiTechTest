import os
import json
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

def extract_information(response):
    extracted_data = {}

    # Extract vendor name
    extracted_data['vendor_name'] = response['vendor']['name']

    # Extract bill to information
    bill_to = response['bill_to']
    extracted_data['bill_to_name'] = bill_to['name']
    extracted_data['bill_to_address'] = bill_to['address']

    # Extract ship to information
    ship_to = response['ship_to']
    extracted_data['ship_to_name'] = ship_to['name']
    extracted_data['ship_to_address'] = ship_to['address']

    # Extract line items
    line_items = response['line_items']
    extracted_line_items = []
    for line_item in line_items:
        extracted_line_item = {
            'quantity': line_item['quantity'],
            'description': line_item['description'],
            'price': line_item['total']
        }
        extracted_line_items.append(extracted_line_item)

    extracted_data['line_items'] = extracted_line_items

    return extracted_data

# Specify the file path of the document
file_path = "docs/0001431487.jpg"

# Process the document using Veryfi API
response = veryfi_client.process_document(file_path)

# Extract the desired information
extracted_information = extract_information(response)

# Create a dictionary to store the extracted data
output_data = {"documents": [extracted_information]}

# Save the extracted information to a JSON file
with open("output.json", "w") as outfile:
    json.dump(output_data, outfile, indent=4)
