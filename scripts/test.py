import json
import requests

headers = {
  'x-auth-key': 'Z7uPzbYQ3pDBtpVZlaNf',
  'x-auth-secret': 'da3849a3f0e947562db54c95',
  
  'Accept': 'application/json',
}

text = """
the volcano is a human body and 
"""

body = {
  "text": text.rstrip(), # remove trailing spaces, yields much better results.
  "model_id": "Ukg1ClHdlG03aG7cAu8J",
  "creativity": 5,
  "stop": ".",
  "max": 100,
}

response = requests.post('http://api.usegrand.com/generate', json=body, headers=headers)
jsonResponse = response.json()

if jsonResponse.get('ok') == False:
  print(f"Error from Grand: {jsonResponse.get('reason')}")
else:
  print(jsonResponse.get('data').get('text'))