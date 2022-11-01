import requests
import os

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
heros = response.json()
list_heros = ['Hulk','Captain America', 'Thanos']
all_heros = {}

for hero in heros:
    if hero['name'] in list_heros:
        all_heros = {hero['name']:hero['powerstats']['intelligence']}

print(max(all_heros, key=all_heros.get))



class YandexDisk:

    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        filename = os.path.basename(file_path)
        path = f'/{filename}'
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": path, "overwrite": True}
        response = requests.get(upload_url, headers=headers, params=params)
        url_upload_file = response.json().get('href')
        resp = requests.put(url_upload_file, data=open(file_path, 'rb'), headers=headers)

if __name__ == '__main__':
    path_to_file = r"C:\Users\JonyBog\Desktop\Hello world.txt"
    token = ...
    uploader = YandexDisk(token)
    result = uploader.upload(path_to_file)












