# 2301894155 - Valentino Nooril

import base64
import requests


def upload(filename):
    # url yang akan digunakan untuk API upload image
    url = "https://api.imgur.com/3/image"

    # header berisikan token bearer untuk autorisasi agar dapat upload image ke dalam folder spesifik
    headers = {
    'Authorization': 'Bearer [token]'
    }

    # pada params berisikan image yang dibaca sebagai bytes  kemudian di-encode dengan base64
    # lalu masukkan address dari album agar image tersimpan di sana untuk kemudian diakses melalui imgur
    params = {
        'image': base64.b64encode(open(filename, 'rb').read()),
        'album': "jkRjPc1",
    }

    # mengirim request dengan method POST dan data seperti headers dan params
    response = requests.request("POST", url, headers=headers, data=params)
    print('status:', response.status_code)
    return response.text
