from flask import Flask,request,jsonify
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import requests
app=Flask(__name__)


######################################## functions ########################################################################################


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
    
####################################################################################################################################################
@app.route("/")
def home():
    return "Hi welcome"

@app.route("/get_attendance",methods=["POST"])
def attendance():
    if request.method=="POST":
        data=request.json
        if ("Username" in data) and ("Password" in data):
            usrname=data["Username"]
            passwd=data["Password"]
            data=get_attendance(usrname,passwd)
        else:
            data={"Status":"Failed","message":"Used parameters might be wrong use 'Username' for username and 'Password' for password"}
    return jsonify(data)

@app.route("/get_attendance_list",methods=["POST"])
def attendancelist():
    if request.method=="POST":
        data=request.json
        if ("Data" in data):
            log=data["Data"]
            if ("class_id" in log) and ("date" in log) and ("hr" in log) and ("sub_id" in log):
                result=get_attendance_list(log)
                if result!=None:
                    return jsonify({"Status":"Success","message":result})
                else:
                    return jsonify({"Status":"Failed","message":"No Attendance list found."})
            else:
                return jsonify({"Status":"Success","message":"No Attendance list found."})

    else:
        return jsonify({"Status":"Failed","message":"Request method should be POST."})


if __name__=="__main__":
    app.run()
