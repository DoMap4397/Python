import requests
import io


def writeHTMLfile(data):
    file = io.open('code.html', 'w', encoding='utf-8')
    file.write(data)
    file.close()


# Thay đổi request header
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json',

             },
)

json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')

proxies = {
    "http": 'http://operator:operator@113.161.210.88:1080/',
    "https": 'http://operator:operator@113.161.210.88:1080/'
}

response = requests.get('https://api.myip.com', proxies=proxies)
print(response.json())
myip = response.json()['ip']
print(myip)
