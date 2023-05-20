"""
This module specifies the information to extract from the documents and saves the data to a JSON file
"""
import json

def extract_information(response):
    extracted_data = {
        'vendor_name': response['vendor']['name'],
        'bill_to_name': response['bill_to']['name'],
        'bill_to_address': response['bill_to']['address'],
        'ship_to_name': response['ship_to']['name'],
        'ship_to_address': response['ship_to']['address'],
        'line_items': [
            {
                'quantity': line_item['quantity'],
                'description': line_item['description'],
                'price': line_item['total']
            }
            for line_item in response['line_items']
        ]
    }
    
    return extracted_data

def save_to_json(data, output_path):
    with open(output_path, "w") as outfile:
        json.dump(data, outfile, indent=4)
