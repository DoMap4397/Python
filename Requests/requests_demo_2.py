import requests
import io


def writeHTMLfile(data):
    file = io.open('code.html', 'w', encoding='utf-8')
    file.write(data)
    file.close()


# Add Params (query string)

# Cách viết 1:
# response = requests.get('https://api.github.com/search/repositories?q=requests+language:python')

# Cách viết 2:
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

print('total_count', response.json()['total_count'])
# https://api.github.com/search/repositories

proxies = {
    "http": 'http://operator:operator@113.161.210.88:1080/',
    "https": 'http://operator:operator@113.161.210.88:1080/'
}

response = requests.get('https://api.myip.com', proxies=proxies)
print(response.json())
myip = response.json()['ip']
print(myip)
