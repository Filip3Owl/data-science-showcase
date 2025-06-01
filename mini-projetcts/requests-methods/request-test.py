import requests

import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

r.status_code

print(r.request.headers)

print("request body:", r.request.body)

header=r.headers
print(r.headers)

header['date']

header['Content-Type']

r.encoding

r.text[0:100]