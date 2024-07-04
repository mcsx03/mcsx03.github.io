#https://mcsx03.github.io/2024-07-03-Xworm_AsyncRat
#Rename batch file to input.txt

import re

def extract_variable_key_and_lines(filename):
    variable = None
    key = None
    decoded_lines = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        for index, line in enumerate(lines):
            if line.startswith("&@cls&@set \""):
                parts = lines[index + 1].split('=')
                
                if len(parts) > 1:
                    variable = parts[0].strip()
                    
                key_line = lines[index + 1].strip()
                
                if key_line.startswith(variable):
                    key = key_line.split('=')[1].strip().strip('"')
                    print("Variable:", variable)
                    print("Key:", key)
                   
                    for next_line in lines[index + 2:]:
                        if next_line.startswith(f"{variable}:~"):
                            line_content = next_line.split(f"{variable}:~")[1].rstrip()
                                                     
                            line_content = re.sub(r"1%%.*$", "", line_content)
                            line_content = line_content.replace("1%", "")
                            line_content = line_content.replace(",", "")
                            line_content = line_content.rstrip("%")
                            decoded_content = []
                            i = 0
                            while i < len(line_content):
                                if line_content[i].isdigit():
                                    num_str = line_content[i]
                                    i += 1
                                    while i < len(line_content) and line_content[i].isdigit():
                                        num_str += line_content[i]
                                        i += 1
                                    
                                    index = int(num_str)
                                    if 0 <= index < len(key):
                                        decoded_content.append(key[index])
                                else:
                                    decoded_content.append(line_content[i])
                                    i += 1                            
                            decoded_line = ''.join(decoded_content)
                            decoded_lines.append(decoded_line)
                        elif not next_line.startswith(variable):
                            continue
                        else:
                            break
                    
                    if decoded_lines:
                        final_decoded_string = ''.join(decoded_lines)
                        print("")
                        print(final_decoded_string)
                        print("")
                    else:
                        print("Something didn't work")
                    
                    return
        
        print("No Key")


filename = 'input.txt'
extract_variable_key_and_lines(filename)
