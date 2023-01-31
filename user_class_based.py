import requests
from main import User

class RandomUser:
    def __init__(self) -> None:
        self.url = 'https://randomuser.me/api/'

    def get_randomuser(self) -> dict:
        '''get full data from randomuser
        
        Returns:
            dict: full data
        '''
        responce = requests.get(self.url)
        responce = responce.json()
        return responce
    def get_cell(self) -> str:
        '''get user cell from randomuser
        
        Returns:
            str: user cell
        '''
        results = User()
        cell = results['cell']
        return cell
    
    def get_city(self) -> str:
        '''get user city from randomuser
        
        Returns:
            str: user city
        '''
        result = User()
        city = result['location']['city']
        return city
    
    def get_dob(self) -> dict:
        '''get user dob from randomuser
        
        Returns:
            dict: user dob
        '''
        results = User()
        dob = results['dob']
        return dob
    
    def get_email(self) -> str:
        '''get user email from randomuser
        
        Returns:
            str: user email
        '''
        results = User()
        email = results['email']
        return email
    
    def get_email(self) -> str:
        '''get user email from randomuser
        
        Returns:
            str: user email
        '''
        results = User()
        email = results['email']
        return email
    
    def get_first_name(self) -> str:
        '''get user first name from randomuser
        
        Returns:
            str: user first name
        '''
        results = User()
        first_name = results['name']['first']
        return first_name
    
    def get_last_name(self) -> str:
        '''get user last name from randomuser
        
        Returns:
            str: user last name
        '''
        results = User()
        last_name = results['name']['last']
        return last_name
    
    def get_full_name(self) -> str:
        '''get user full name from randomuser
        
        Returns:
            str: user full name
        '''
        results = User()
        title = results['name']['title']
        first = results['name']['first']
        last = results['name']['last']
        return f"{title} {first} {last}"
    
    def get_gender(self) -> str:
        '''get user gender from randomuser
        
        Returns:
            str: user gender
        '''
        results = User()
        gender = results['gender']
        return gender
    
    def get_id(self) -> dict:
        '''get user id from randomuser
        
        Returns:
            dict: user id
        '''
        results = User()
        id = results['id']
        return id
    
    def get_id_number(self) -> str:
        '''get user id number from randomuser
        
        Returns:
            str: user id number
        '''
        results = User()
        id_number = results['phone']
        return id_number
    
    def get_info(self) -> dict:
        '''get user info from randomuser
        
        Returns:
            dict: user info
        '''
        response = requests.get(self.url)
        response = response.json()
        info = response['info']
        return info
    
    def get_nat(self) -> str:
        '''get user nat from randomuser
        
        Returns:
            str: user nat
        '''
        results = User()
        nat = results['nat']
        return nat
    
    def get_picture(self) -> dict:
        '''get user picture from randomuser
        
        Returns:
            dict: user picture
        '''
        results = User()
        picture = results['picture']
        return picture
