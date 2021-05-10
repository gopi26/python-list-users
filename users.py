import requests

// Mock API list of users under / path
USERS_URL = 'https://myapp.free.beeceptor.com/'

// Mock API list of users under / path printed in main page
x = requests.get('https://myapp.free.beeceptor.com/')
print(x.text)
    
// Unit test case to verify the page return 200 success code
def get_users():
    """Get list of users"""
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    else:
        return None