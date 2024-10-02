import requests

res = requests.get("https://www.hcmue.io.vn")
#print(res)

if  res.status_code == 200:
    print(res.content)