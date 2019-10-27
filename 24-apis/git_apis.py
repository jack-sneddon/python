import json
import requests

api_url_base = 'https://api.github.com'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'Python Student',
           'Accept': 'application/vnd.github.v3+json'}

def list_apis() :
    api_url = api_url_base
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
        # return (response.content)
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

def user_url(user) :
    api_url = f"{api_url_base}/users/{user}"
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

def list_repos(user) :
    api_url = f"{api_url_base}/users/{user}/repos"
    
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

if __name__ == '__main__':
    apis = list_apis()
    print(' ----- APIs -----')
    if apis is not None:
        print(json.dumps(apis, indent=4))
    else:   
        print('No apis Found')
    
    user_url = user_url('jack-sneddon')
    print(' ----- User Url -----')
    if user_url is not None:
        print(json.dumps(user_url, indent=4))
    else:   
        print('No user url found')
    
    repos = list_repos('jack-sneddon')
    print(" ----- List Repos for 'jack-sneddon' -----")
    if repos is not None:
        print(json.dumps(repos, indent=4))
    else:   
        print(f'No repos Found for jack-sneddon')
