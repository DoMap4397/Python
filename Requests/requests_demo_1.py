import requests
import io


def writeHTMLfile(data):
    file = io.open('code.html', 'w', encoding='utf-8')
    file.write(data)
    file.close()


# GET requests
res = requests.get('https://www.youtube.com/results?search_query=nghiahsgs')
writeHTMLfile(res.text)

response = requests.get('https://api.github.com')
print('response.status_code', response.status_code)
print(response.json()['current_user_url'])

print('headers', response.headers['Content-Type'])

proxies = {
    "http": 'http://operator:operator@113.161.210.88:1080/',
    "https": 'http://operator:operator@113.161.210.88:1080/'
}

response = requests.get('https://api.myip.com', proxies=proxies)
print(response.json())
myip = response.json()['ip']
print(myip)
