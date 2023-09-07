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
    print('PING')
    useragent = str(request._headers.get('user-agent'))
    timestamp = int(time.time())
    pingdata = {'agent': useragent, 'timestamp': timestamp}
    pid = pingdb.insert(pingdata)
    return {'idnumber': pid, 'ping': pingdata}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
