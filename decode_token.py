# from datetime import datetime
import jwt
from datetime import timedelta
import datetime

def decode_jwt_token(secret_key, token):
    # Decode the JWT token
    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])

    return decoded_token


# print(decode_jwt_token('das', token)['dbname'])




def generate_jwt_token(secret_key, data, expiration_minutes=60):
    import datetime
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)

    # Build the payload
    payload = {
        "exp": expiration_time,
        **data
    }

    # Generate the JWT token
    token = jwt.encode(payload, secret_key, algorithm="HS256")

    return token



# print(generate_jwt_token('das',data={'username':'postgres','password':'mounir','dbname':'upwork'})) 


