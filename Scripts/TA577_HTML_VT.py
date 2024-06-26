#VT Search: content:{72657475726e20732e73706c6974282222292e7265766572736528292e6a6f696e282222293b} and content:{616c6572742822536f6d657468696e672077656e742077726f6e672122293b} 

import os
import base64
from bs4 import BeautifulSoup

def decode(encoded_string):
    reversed_string = encoded_string[::-1]
    decoded_string = base64.b64decode(reversed_string).decode('utf-8')
    return decoded_string

folder_path = 'samples'
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r') as file:
        try:
            html_code = file.read()
            soup = BeautifulSoup(html_code, 'html.parser')
            encoded_string = soup.find('div', id='uri').text.strip()
            decoded_result = decode(encoded_string)
            print(f"File: {filename}")
            print(decoded_result)
            print("-------------------------------------------")
        except:
            print("no results")

