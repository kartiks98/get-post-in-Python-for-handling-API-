import requests

URL = "https://timestamp-for-every-entry-dic.herokuapp.com"


sName = 'Kartik'
sendName = requests.post(url = URL + '/name' + f'/{sName}')
print(sendName)
print(sendName.json())

gName = 'Kartik'
getName = requests.get(url = URL + '/name' + f'/{gName}')
print(getName)
print(getName.json())

NameList = requests.get(url = URL + '/names')
print(NameList)
print(NameList.json())