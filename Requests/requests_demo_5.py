import requests
import io


def writeHTMLfile(data):
    file = io.open('code.html', 'w', encoding='utf-8')
    file.write(data)
    file.close()


# POST data json
response = requests.post('https://httpbin.org/post', json={'name': 'nghia', 'age': 20})
print(response.text)

proxies = {
    "http": 'http://operator:operator@113.161.210.88:1080/',
    "https": 'http://operator:operator@113.161.210.88:1080/'
}

response = requests.get('https://api.myip.com', proxies=proxies)
print(response.json())
myip = response.json()['ip']
print(myip)
