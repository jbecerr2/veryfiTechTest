import os
import json
from veryfi import Client
from dotenv import load_dotenv

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Function to load veryfi API credentials from envfile
def veryfi_credentials():
    credentials = "envfile.env"
    load_dotenv(credentials)

    client_id = os.getenv("VERYFI_CLIENT_ID")
    client_secret = os.getenv("VERYFI_CLIENT_SECRET")
    username = os.getenv("VERYFI_USERNAME")
    api_key = os.getenv("VERYFI_API_KEY")

    #Check if the credentials are properly loaded from the env file
    if not all([client_id, client_secret, username, api_key]):
        raise ValueError("Error: Failed to load Veryfi API credentials, please check the .env file")
    print("Veryfi credentials loaded successfully")
    
    return client_id, client_secret, username, api_key


#Function to extract the specific information from a document
def extract_information(response):
    extracted_data = {
        'vendor_name':response['vendor']['name'],
        'bill_to_name':response['bill_to']['name'],
        'bill_to_address':response['bill_to']['address'],
        'ship_to_name':response['ship_to']['name'],
        'ship_to_address':response['ship_to']['address'],
        'line_items':[
            {
                'quantity':line_item['quantity'],
                'description':line_item['description'],
                'price': line_item['total']
            }
            for line_item in response['line_items']
        ]

    }  
    return extracted_data

#Function to read all the documents present in a directory
def process_documents(directory_path, client):
    output_data = {"documents":[]}

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        response = client.process_document(file_path)
        extracted_info = extract_information(response)
        output_data["documents"].append(extracted_info)
    return output_data

#Function to save all the processed data into a json file
def save_to_json(data,output_path):
    with open(output_path,"w") as outfile:
        json.dump(data, outfile, indent=4)


def main():
    
    client_id, client_secret, username, api_key = veryfi_credentials()
    veryfi_client = Client(client_id=client_id, client_secret=client_secret, username=username, api_key=api_key)

    directory_path="docs/"
    output_path="output.json"

    output_data = process_documents(directory_path, veryfi_client)
    save_to_json(output_data, output_path)

if __name__=="__main__":
    main()
