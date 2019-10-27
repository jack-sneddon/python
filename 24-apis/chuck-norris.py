# simple call to the chuck norris API
import json
import requests

api_url_base = 'https://api.chucknorris.io'
headers = {'Content-Type': 'application/json'}

# random Chuck Norris Joke
def get_random_chuck_norris_joke() :
    api_url = f"{api_url_base}/jokes/random"
    response = requests.get(api_url, headers=headers)

    print(f"Response Code = {response.status_code}")

    if response.status_code == 200:
        return (response.content)
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None
    

"""
     if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

"""
if __name__ == '__main__':
    random_joke = get_random_chuck_norris_joke()
    if random_joke is not None:
        print(random_joke)
    else:   
        print('No Joke Found')
