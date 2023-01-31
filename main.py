'''test requests'''
import requests
def User():
    url = 'https://randomuser.me/api/'
    response = requests.get(url)
    response = response.json()
    results = response['results'][0]
    return results

