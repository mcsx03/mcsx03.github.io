import os
import zipfile
import re
import tempfile

def extract_urls(path):
    urls = []
    with tempfile.TemporaryDirectory() as tmpdirname:
        with zipfile.ZipFile(path, 'r') as docx:
            docx.extractall(tmpdirname)
        for root, dirs, files in os.walk(tmpdirname):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    found_urls = re.findall(r'(https?://[^\s]+)', content)
                    cleaned_urls = [url.rstrip('"') for url in found_urls]
                    
                    for i in cleaned_urls:
                        # Ensure the URL does not start with any of the specified prefixes
                        if (not i.startswith("http://schemas") and
                            not i.startswith("http://purl.org") and
                            not i.startswith("http://www.w3")):
                            print(i)
                            urls.append(i)

    return urls


path = 'sample.doc'
urls = extract_urls(path)
