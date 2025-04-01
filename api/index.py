from flask import Flask,request,jsonify
from engine import *

app=Flask(__name__)    
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
def getattendancelist():
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

@app.route("/receive_attendance_list",methods=["POST"])
def recattendancelist():
    if request.method=="POST":
        print("post")
        data=request.json
        print(data)
        if ("Data" in data):
            log=data["Data"]
            send_attendance_list(log)
            return jsonify({"Status":"Success","message":"Data send successfully."})
        else:
            return jsonify({"Status":"Failed","message":"Data not send properly."})

if __name__=="__main__":
    app.run()
