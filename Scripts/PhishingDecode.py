#
import os
import re

folder_path = 'Samples'
regpattern = r'(?<=/\()[^|]+(?=\|)'
regpattern1 = r'(?<=\|)[^/]+(?=\)/)'
string_pattern = r'replace\.call\("([^"]+)",/'

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        
    string = re.search(string_pattern, content).group(1)
    pattern = re.search(regpattern, content).group(0)
    pattern1 = re.search(regpattern1, content).group(0)
    stringreplace = string.replace(pattern, '')
    final = stringreplace.replace(pattern1, '')
    print(final)
       
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        process_file(file_path)

