from tinydb import TinyDB, Query
from fastapi import FastAPI, Request
import time
# from typing import Optional

app = FastAPI()
db = TinyDB('tinydb.json')
pingdb = db.table('ping')
userdb = db.table('user')
datadb = db.table('data')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping")
async def root(request: Request):
    useragent = str(request._headers.get('user-agent')).split('(')[1].split(')')[0]
    timestamp = int(time.time())
    pingdata = {'agent': useragent, 'timestamp': timestamp}
    pid = pingdb.insert(pingdata)
    return {'idnumber': pid, 'ping': pingdata}

@app.get("/pinglist")
async def root():
    return pingdb.all()