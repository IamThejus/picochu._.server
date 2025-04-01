from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import requests



################################################################################################ FUNCTIONS FOR MONGO DB ############################################################################################


MONGO_URI = "mongodb+srv://picochu:picochu@2hekav0.mongodb.net/?retryWrites=true&w=majority"

def get_attendance_list(data):
    client = MongoClient(MONGO_URI)
    db = client["attendance_system"]
    collection = db["attendance_records"]
    for record in collection.find(data):
        del record["_id"]
        return record
    
def send_attendance_list(data):
    client = MongoClient(MONGO_URI)
    db = client["attendance_system"]
    collection = db["attendance_records"]
    collection.insert_one(data)

############################################################################################## FUNCTIONS FOR SNGCE API ############################################################################################

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

def get_attendance(usrid,passwd):
    attendance="https://sngce.etlab.in/ktuacademics/student/viewattendancesubject/11"
    logged_in=get_loggedin(usrid,passwd)
    if logged_in["request"]==True:
        logged_in=logged_in["session"]
        data=logged_in.get(url=attendance)
        data_content=BeautifulSoup(data.content,"html.parser")
        result={}
        table_header=data_content.find_all("th")
        table_value=data_content.find_all("td")
        for i in range(len(table_header)):
            result[table_header[i].text.strip()]=table_value[i].text.strip()
        return {"Status":"Success","message":result}
    else:
        return {"Status":"Failed","message":logged_in["message"].strip()}


######################################################################################################################################################################################################################
