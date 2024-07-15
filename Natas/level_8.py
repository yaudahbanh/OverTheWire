import requests
import re
import base64
requests.packages.urllib3.disable_warnings()

url = "http://natas8.natas.labs.overthewire.org"

def get_encoded_secret():
    r = requests.post(url + "/index-source.html", auth=('natas8', 'xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q'), verify=False)
    if r.status_code == 200:
        encoded = re.findall(r'#DD0000">"(.+)"', r.text)[0]
        split_after_32 = encoded[:32]
    return split_after_32

def decode():
    secret = get_encoded_secret()
    hex_to_binary = bytes.fromhex(secret).decode('utf-8')
    str_reverse = hex_to_binary[::-1]
    base64_decode = base64.b64decode(str_reverse).decode('utf-8')
    return base64_decode

def exp():
    data_post = {
        "secret": decode(),
        "submit": "Submit"
    }
    r = requests.post(url, auth=('natas8', 'xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q'), verify=False, data=data_post)
    if r.status_code == 200:
        password = re.findall("password for natas9 is (.+)", r.text)[0]
        print("Password for natas9: " + password)

if __name__ == "__main__":
    exp()
