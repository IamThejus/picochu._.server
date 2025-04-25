from mfrc522 import MFRC522
import utime
from ssd1306 import *
import ntptime
import network
import time
import urequests
import json
import sys
import machine

# Wi-Fi Configuration
SSID = 'YOUR_WIFI_SSID'
PASSWORD = 'YOUR_WIFI_PASSWORD'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
print("Connecting to Wi-Fi...")
while not wlan.isconnected():
    pass
print("Connected:", wlan.ifconfig())

# Sync time using NTP or fallback API
def set_time_online():
    try:
        ntptime.settime()
        print("Time synced via NTP")
    except:
        try:
            response = urequests.get("http://worldtimeapi.org/api/timezone/Etc/UTC")
            if response.status_code == 200:
                timestamp = response.json()["unixtime"]
                rtc = machine.RTC()
                rtc.datetime(time.gmtime(timestamp))
                print("Time set manually")
        except:
            print("Failed to sync time.")

set_time_online()

# API URL
API_URL = 'https://picochuserver.vercel.app/receive_attendance_list'

# Subject schedule
subjects = ["CST306", "CST302", "PPY"]

# Student database (sample)
students = {
    "Thejus A": {"rfid": [98, 137, 97, 81], "rollno": 44},
    "TD Deepak": {"rfid": [208, 220, 72, 16], "rollno": 43}
}

# RFID Reader
reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)

# OLED Display
oled = create_display()
oled.text("Ready to scan!!", 0, 33)
oled.show()

# Helper functions
def get_date():
    t = time.localtime(time.time() + 19800)  # +5:30 offset
    return f"{t[0]}-{t[1]:02d}-{t[2]:02d}"

def get_time():
    t = time.localtime(time.time() + 19800)
    return f"{t[3]:02d}:{t[4]:02d}:{t[5]:02d}"

def get_subject():
    return subjects[int(get_time().split(":")[1]) % len(subjects)]

def send_attendance(data):
    if not wlan.isconnected():
        print("Wi-Fi not connected.")
        return None
    try:
        response = urequests.post(API_URL, data=json.dumps({"Data": data}), headers={"Content-Type": "application/json"})
        print("Response:", response.text)
        response.close()
    except Exception as e:
        print("Failed to send data:", e)

def already_marked(name, data):
    return any(record["name"] == name for record in data)

# Attendance tracking
attendance = {}
prev_uid = [0]

try:
    while True:
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK and uid != prev_uid:
                for name, info in students.items():
                    if uid == info["rfid"]:
                        minute = int(get_time().split(":")[1])
                        subject = get_subject()
                        timestamp = get_time()

                        if minute not in attendance:
                            # Send previous minute’s data if exists
                            if (minute - 1) in attendance:
                                previous = attendance[minute - 1]
                                payload = {
                                    "class_id": "R6B",
                                    "date": get_date(),
                                    "hr": 3,
                                    "sub_id": "CSL336",
                                    "attendance": [
                                        {
                                            "student_id": str(p["rollno"]),
                                            "status": "present"
                                        } for p in previous
                                    ]
                                }
                                oled.fill(0)
                                oled.text("Sending...", 0, 30)
                                oled.show()
                                send_attendance(payload)
                                time.sleep(2)
                            attendance[minute] = []

                        if not already_marked(name, attendance[minute]):
                            attendance[minute].append({
                                "name": name,
                                "rollno": info["rollno"],
                                "rfid": uid,
                                "time": timestamp,
                                "subject": subject
                            })
                            oled.fill(0)
                            oled.text("Welcome", 0, 30)
                            oled.text(name, 0, 40)
                            oled.show()
                            print(f"{name} marked present at {timestamp} for {subject}")
                        break
                prev_uid = uid
        utime.sleep_ms(50)
except KeyboardInterrupt:
    print("Exiting...")
