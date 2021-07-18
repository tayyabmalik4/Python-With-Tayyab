import requests
import test9_akhbar
import json

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2021-07-06&'
       'sortBy=popularity&'
       'apiKey=cf5af7b0baa74b0ca672576619eb187d')
# url1 ="https://newsapi.org/v2/top-headlines/sources?apiKey=cf5af7b0baa74b0ca672576619eb187d "

response = requests.get(url)
akhbar=response.text
print(akhbar)
convert = json.loads(akhbar)
# resp = ''.join(key + str(val) for key, val in convert.items())
# print(resp)
# test9_akhbar.speak(resp)

# print(response.json)
# print(response.text)

f=open("test9.2.py")
data=json.load(f)
for i in data["sources"]:
    # /////for converting the dictionary to strings
    res = ''.join(key + str(val) for key, val in i.items())
    print(res)
    test9_akhbar.speak(res)
    resp = ''.join(key + str(val) for key, val in convert.items())
    print(resp)
    test9_akhbar.speak(resp)
    print(resp)
f.close()