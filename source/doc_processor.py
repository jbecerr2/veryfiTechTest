"""
This module has the function process_documents. This function reads the directory called "docs" that is specified in directory_path, 
to process each file using the Veryfi client
"""

import os
from veryfi import Client
from extract_json import extract_information

def process_documents(directory_path, client):
    output_data = {"documents": []}

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        response = client.process_document(file_path)
        extracted_info = extract_information(response)
        output_data["documents"].append(extracted_info)

    return output_data
