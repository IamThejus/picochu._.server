from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import requests

MONGO_URI = "mongodb+srv://picochu:picochu@2hekav0.mongodb.net/?retryWrites=true&w=majority"

def get_attendance_list(data):
    client = MongoClient(MONGO_URI)

    # Select database & collection
    db = client["attendance_system"]
    collection = db["attendance_records"]

    data=[]
    for record in collection.find(data):
        del record["_id"]
        return record
    


url="https://sngce.etlab.in/user/login"



            
def get_loggedin(usrid,passwd):
    payload={
        'LoginForm[username]':usrid,
        'LoginForm[password]':passwd,
        "yt0":""
    }

    session=requests.Session()

    request=session.post(url,data=payload)
    data=BeautifulSoup(request.text,"html.parser")
    result={}
    message=data.find(class_="flash-error")
    if message is None:
        result={"request":True,"session":session}
    else:
        result={"request":False,"message":message.text.strip()}
    return result
