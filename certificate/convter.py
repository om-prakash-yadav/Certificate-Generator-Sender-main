import json
import requests



def ppt2pdf(f_path,filename, token):

    headers = {"Authorization": token}
    para = {
        "name": filename,
        "parents": ["1uHeh1v3Bhg1VfwpQAKMHiJpg1rk30rpc"]
        }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(f_path, "rb")
        }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
        )
    fi = r.text.split()
    st = fi[4]
    st = st[1:-2]
    return st