import json
import time
from authlib.jose import JsonWebKey
from authlib.jose import jwt

def validateJWT() :
    print("\n---Validate JWT---")
    print("Enter a JWT: ")
    token = input()
    
    # define public key
    jwk = {
        "crv": "P-256",
        "kty": "EC",
        "alg": "ES256",
        "use": "sig",
        "kid": "a32fdd4b146677719ab2372861bded89",
        "x": "-uTmTQCbfm2jcQjwEa4cO7cunz5xmWZWIlzHZODEbwk",
        "y": "MwetqNLq70yDUnw-QxirIYqrL-Bpyfh4Z0vWVs_hWCM"
    }
    
    # make sure we match what is expected
    claims_options = {
        "iss": { "essential": True, "value": "https://idp.jack.com" },
        "aud": { "essential": True, "value": "api1" }
    }
    
    claims = jwt.decode(token, jwk, claims_options=claims_options)
    claims.validate()
    
    print(json.dumps(claims, indent=2))
    

def main():
    validateJWT()

# Determine if a Python script is being run as the main program or if it 
# is being imported as a module into another script. 
if __name__ == "__main__":
    main()