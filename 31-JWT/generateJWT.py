import json
import time
from authlib.jose import JsonWebKey
from authlib.jose import jwt

# create a JSON Web Key (private key)
def createJWK() :
    print ("\n---create a jwk---")
    # Generate an RSA key pair
    key = JsonWebKey.generate_key('RSA', 2048)
    # key = JsonWebKey.generate_key('EC', crv='P-256', alg='ES256', use='sig')
    # key = JsonWebKey.generate_key('EC', size=256)

    # Set the parameters manually
    # key.kty = 'EC'
    # key.crv = 'P-256'
    # key.alg = 'ES256'
    # key.use = 'sig'
    
    # Convert the key to a JWK
    jwk = key.as_dict()

    # Pretty print the JWK
    print(json.dumps(jwk, indent=2))


def generateJWT() :
    print("\n---Create JWT---")

    # key
    jwk = {
        "crv": "P-256",
        "kty": "EC",
        "alg": "ES256",
        "use": "sig",
        "kid": "a32fdd4b146677719ab2372861bded89",
        "d": "5nYhggWQzfPFMkXb7cX2Qv-Kwpyxot1KFwUJeHsLG_o",
        "x": "-uTmTQCbfm2jcQjwEa4cO7cunz5xmWZWIlzHZODEbwk",
        "y": "MwetqNLq70yDUnw-QxirIYqrL-Bpyfh4Z0vWVs_hWCM"
    }
    
    # header
    header = {"alg": "ES256"}
    
    # payload
    payload = {
        "iss": "https://idp.jack.com",
        "aud": "api1",
        "sub": "9377717bef5a48c289baa2d242367ca5",
        "exp": int(time.time()) + 300,
        "iat": int(time.time())
    }
    
    # create the token
    token = jwt.encode(header, payload, jwk)
    
    # Print the JWK
    print("\nNext steps is to take the token and decode it.  One good place is https://jwt.io")
    print("\nNote - never put any private data into any public website\n")
    
    print(token.decode("utf-8"))
    # print(json.dumps(jwk, indent=2))

def main():
    print("Create a JWT.")
    createJWK()
    generateJWT()

# Determine if a Python script is being run as the main program or if it 
# is being imported as a module into another script. 
if __name__ == "__main__":
    main()