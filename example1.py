import requests
import json
from env.key import key
print("key")
APIkey = "3c50bbfe9ef1bd837eb70d4686ef6674"
city = "Vancouver"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}"
data = requests.get(url)
print( type(data) )
print(f"request response:{data}")
print("")
print( type(data.text))
print(f"request text {data.text}")
print("")
jData = json.loads(data.text)
print(type(jData))
print(jData)
print("")
for i in jData:
    """
    iterating through the dictionary prints the keys for the dictionary elements
    To access the values, you need to reference the key from the dictionary
    """
    print(i, jData[i])