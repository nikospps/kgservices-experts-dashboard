# "user1@mail.com"
# "!user1!"
import json
import requests
##Beautiful usage in python
def add_quote(a):
    return '"{0}"'.format(a)

def status(username,password):
    import requests
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    params = (
        ('setCookie', 'false'),
    )
    data = '{ "username":'+ add_quote(username) + ', "password":' + add_quote(password) +'}'
    # return data
    response = requests.post('https://iam-backend.alamedaproject.eu/api/v1/auth/login', headers=headers, params=params,data=data)
    status_code = response.status_code
    # return result
    return (status_code)

def access_token(username,password):
    import requests
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    params = (
        ('setCookie', 'false'),
    )
    data = '{ "username":'+ add_quote(username) + ', "password":' + add_quote(password) +'}'
    # return data
    response = requests.post('https://iam-backend.alamedaproject.eu/api/v1/auth/login', headers=headers, params=params,data=data)
    nn=response.text
    nnn = nn.split(',', 1)
    nnnn=nnn[0]
    nnnnn = nnnn.split('{', 1)
    nnnnnnn=nnnnn[1]
    bbb = nnnnnnn.split(':', 1)
    f = bbb[1]
    acc_tok=eval(f)
    # status_code = response.status_code
    # result=response.json()
    # acc_tok = str(result['access_token'])
    # ref_tok = result['refresh_token']
    # return result
    return (acc_tok)
    # return ('nikos')

def login(username,password):
    import requests
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    params = (
        ('setCookie', 'false'),
    )
    data = '{ "username":'+ add_quote(username) + ', "password":' + add_quote(password) +'}'
    # return data
    response = requests.post('https://iam-backend.alamedaproject.eu/api/v1/auth/login', headers=headers, params=params,data=data)
    status_code = response.status_code
    # result=json.loads(response.text)
    result=response.json()
    acc_tok = result['access_token']
    # ref_tok = result['refresh_token']
    # return result
    return (acc_tok)#,ref_tok)

# (status_code,acc_token,refresh_token)=login("user1@mail.com","!user1!")##=====>
# data1=login("user1@mail.com","!user1!")

def users_profiles(username,password):
    acc_token = access_token(username,password)
    # acc_token = login(username,password)#
    bearer= 'Bearer ' + acc_token
    headers = {
        'accept': 'application/json',
        'Authorization': bearer
    }
    response1 = requests.get('https://iam-backend.alamedaproject.eu/api/v1/account', headers=headers)
    result1=response1.json()
    return result1

def cross_correlation(bearer, userid):
    bearer = 'Bearer ' + bearer
    url = 'https://iam-backend.alamedaproject.eu/api/v1/user/' + userid
    headers = {
        'accept': 'application/json',
        'Authorization': bearer,
    }

    response = requests.get(url,headers=headers)
    return (response.status_code,response.json())
# #Functions to be executed
# status_code=status("user1@mail.com","!user1!")##=====>
# (acc_token,refresh_token)=login("user1@mail.com","!user1!")##=====>
#acc_token=login("iccs-service@cn.ntua.gr","dFpiyRclN2nS6ES63ubIOifGuJdwvZia5fcnqPq6")##=====>
#prof = users_profiles("iccs-service@cn.ntua.gr","dFpiyRclN2nS6ES63ubIOifGuJdwvZia5fcnqPq6")
# profile=users_profiles(acc_token)##=====>
# def testing(username,password):
#     import requests
#     headers = {
#         'accept': 'application/json',
#         'Content-Type': 'application/json',
#     }
#     params = (
#         ('setCookie', 'false'),
#     )
#     data = '{ "username":'+ add_quote(username) + ', "password":' + add_quote(password) +'}'
#     # return data
#     response = requests.post('https://iam-backend.alamedaproject.eu/api/v1/auth/login', headers=headers, params=params,data=data)
#     status_code = response.status_code
#     # result=json.loads(response.text)
#     # result=response.json()
#     # acc_tok = result['access_token']
#     # ref_tok = result['refresh_token']
#     # return result
#     return response.text

#prof['id']
