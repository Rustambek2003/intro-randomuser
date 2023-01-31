import requests
import json


def get_user(user_data: dict) -> dict:
    '''get user from data
    
    Args:
        user_data (dict): user data from https://randomuser.me/api/
        
    Returns:
        dict: {
            'firstname': user firstname,
            'lastname': user lastname,
            'age': user age,
            'country': user country
        }
    '''
    results = user_data['results'][0]
    user_firstname = results['name']['first']
    user_lastname = results['name']['last']
    user_age = results['registered']['age']
    user_country = results['location']['country']
    dict = {
            'firstname': user_firstname,
            'lastname': user_lastname,
            'age': user_age,
            'country': user_country
        }
    return dict

def get_users(url: str, n: int) -> list:
    '''get n users from url
    
    Args:
        url (str): api url
        n (int): number of users
        
    Returns:
        list: list of users. user from get_user()
    '''
    Users = []
    while n > 0:
        response = requests.get(url).json()
        user = get_user(response)
        Users.append(user)
        n -= 1
    
    return Users

def write_users_to_file(file_path: list, n: int):
    '''write n users to file

    Args:
        url (str): api url
        n (int): number of users
    '''
    file = open('data.json').read()
    file = json.loads(file)
    Users = file_path
    file.extend(Users)

    with open('data.json','w') as f:
        json.dump(file,f,indent=4)

    return file

url = 'https://randomuser.me/api/'
response = requests.get(url).json()
# print(get_user(response))

users = get_users(url=url, n=2)

print(write_users_to_file(users , 2))