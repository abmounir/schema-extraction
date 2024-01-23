from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from typing import Annotated
import datetime
from datetime import timedelta
import secrets
from time import gmtime, strftime
from decode_token import *
from db import Operations
dbname = "upwork"
user = "postgres"
password = "mounir"
host = "localhost"
port = "5432"
from decode_token import *
import os
app = FastAPI()

@app.post('/v1/db_login', status_code=201)
async def login(creds: dict):
    # read credentials
    # expires=0
    username=creds['username']
    db_name=creds['dbname']
    password=creds['password']
        
    db_connect = Operations(dbname=dbname,
                        user=username,
                        password=password,
                        ).connect()
    if db_connect is not None:
        # generate jwt token
        token=generate_jwt_token('das',data={'username':username,'db_name':dbname,'password':password})
        return {"message": "success", "token":token}
    else:
        return {"message": "failed! wrong credentials, try again"}
    
    
@app.get('/v1/list_tables',status_code=200)
async def list_schema_info( token: Annotated[str | None, Header()] = None):
    if decode_jwt_token(token=token,secret_key='das') :
        db_connect = Operations(dbname=decode_jwt_token(token=token,secret_key='das')['dbname'],
                                user=decode_jwt_token(token=token,secret_key='das')['username'],
                                password=decode_jwt_token(token=token,secret_key='das')['password'],
                                )
        
        with db_connect.connect() as connection:
            data=db_connect.list_tables()
            return {"tables":data}
        
