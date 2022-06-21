import os
import requests
full_save_path = os.path.join(os.getcwd())
base_path = os.path.dirname(full_save_path)
if not os.path.isdir(base_path):
    os.makedirs(base_path)

r = requests.get('http://ccmixter.org/content/airtone/airtone_-_bluenotes_6.mp3', headers={'referer': 'http://ccmixter.org/'})
if r.ok:
    with open(full_save_path+'/fuck.mp3', 'wb') as f:
        f.write(r.content)
else:
    r.raise_for_status()
