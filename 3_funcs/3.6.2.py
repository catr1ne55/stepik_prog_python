import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/194307.txt'
r = requests.get(url)
res = r.text
while res.startswith('We') is False:
    nurl = 'https://stepic.org/media/attachments/course67/3.6.3/' + res
    print(nurl)
    r = requests.get(nurl)
    res = r.text
    print(res)
print(res)