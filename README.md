# 📡 picochu._.server

**Smart Attendance System** using **Raspberry Pi Pico**, **RFID (RC522)**, and **DS3231 RTC** integrated with a Flask API and MongoDB.

This project provides an API for handling attendance using RFID cards, saving records in MongoDB, and displaying them in a Student Mobile App. It also integrates with the college portal (ETLab) to fetch and display student attendance.

---

## 🚀 Features

- 📘 **RFID-based Attendance**: Students can mark attendance using RFID cards.
- 🗃️ **MongoDB Storage**: Attendance data is stored in a MongoDB database.
- 🌐 **ETLab Integration**: Fetches attendance data from the college portal.
- 🛠️ **Admin Dashboard**: Admins can view and manage attendance through an app.

---

## 🧰 Technologies Used

- 🧠 **Raspberry Pi Pico** – for scanning RFID cards and recording timestamps
- 📟 **RC522 RFID Module** – used to scan student IDs
- ⏰ **DS3231 RTC** – used for accurate timestamps
- 🐍 **Flask** – Python web framework for API development
- 🍃 **MongoDB** – database to store attendance records
- ▲ **Vercel** – serverless deployment of the Flask API

---

### 🔧 Hardware Setup (📸 Image of RFID + Pico)

---

## 🔧 Hardware Setup

Below is the image of the actual hardware setup using Raspberry Pi Pico, RC522 RFID module, and DS3231 RTC:

<img src="https://github.com/user-attachments/assets/24551007-dbd7-462a-81d8-8c73d0c3ac7c" alt="Hardware Setup" width="400"/>


---

### 📱 Mobile App Screenshots

---

## 📱 Home & Login Pages

<p float="left"> <img src="https://github.com/user-attachments/assets/998727a7-2180-4dac-be7b-f8c73d5da565" alt="Home Page" width="220"/> <img src="https://github.com/user-attachments/assets/58bfaeb3-a0aa-4ecd-b878-61648afe6462" alt="Admin Login" width="220"/> <img src="https://github.com/user-attachments/assets/09a6dd62-28eb-43b6-a1a7-a45e416a2adf" alt="Student Login" width="220"/> </p>

- **Home Page**: The landing screen where users choose to log in as either Administrator or Student.
- **Administrator Login Page**: Interface for admins to securely log in and manage attendance data.
- **Student Login Page**: Interface for students to access their attendance dashboard.


## 🧑‍💼 Admin View – Attendance List

<img src="https://github.com/user-attachments/assets/4098a3af-5e68-4d3d-986c-8d364a62de07" alt="Admin Attendance List" width="300"/>

- **Admin Panel – Attendance List**: Displays a session-wise attendance list of students, showing their presence status.

## 👨‍🎓 Student View – Attendance Overview

<img src="https://github.com/user-attachments/assets/426ab250-68c8-4572-a361-8e2211e65432" alt="Student Attendance Overview" width="300"/>

- **Student Dashboard**: Shows the student’s overall attendance status across all subjects, combining RFID data and ETLab info.



---

## 📡 API Endpoints

### `POST /get_attendance`
Fetches the attendance data for a student.

**Input**:
```json
{
  "Username": "student123",
  "Password": "password123"
}

```

**Output**:



```json
{
  "Status": "Success",
  "message": {
    "Subject1": "Present",
    "Subject2": "Absent"
  }
}
```
### `POST /get_attendance_list`
Fetches the attendance list for a specific class.

**Input**:
```json
{
  "Data": {
    "class_id": "CS101",
    "date": "2025-04-01",
    "hr": "10",
    "sub_id": "MATH"
  }
}

```

**Output**:



```json
{
  "Status": "Success",
  "message": {
    "student_123": "Present",
    "student_456": "Absent"
  }
}

```

### `POST /receive_attendance_list`
Receives and stores attendance data in MongoDB.

**Input**:
```json
{
  "Data": {
    "class_id": "CS101",
    "date": "2025-04-01",
    "hr": "10",
    "sub_id": "MATH",
    "attendance": [
      { "student_id": "123", "status": "present" },
      { "student_id": "456", "status": "absent" }
    ]
  }
}


```

**Output**:



```json
{
  "Status": "Success",
  "message": "Data sent successfully."
}


```
### ⚙️ Setup Instructions
✅ Requirements
 * Python 3.x

 * MongoDB (e.g., MongoDB Atlas)

 * Vercel account for deployment

### 📥 Installation
Clone the repository:

bash
```
git clone https://github.com/IamThejus/picochu._.server.git
cd picochu._.server
```
Install Python dependencies:
```
pip install -r requirements.txt

```
### 🧪 Running Locally
Install Vercel CLI:

```
npm install -g vercel
```
Run the app:

```
vercel dev

```
The app will be available at:
```http://localhost:3000```

### 🌐 Deployment (Vercel)
To deploy the app:

```
vercel
```
Follow the prompts to link your GitHub repository and deploy. After deployment, your API will be accessible at the provided Vercel URL.

### 🔧 Configuration
MongoDB URI
Set your MongoDB URI in the code or use environment variables for security.

```vercel.json``` Example

```
{
  "version": 2,
  "builds": [
    {
      "src": "index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/index.py"
    }
  ]
}
```

### 📄 License
This project is licensed under the MIT License – see the LICENSE file for details.


### 🙏 Acknowledgments
* Huge thanks to the open-source community for the tools and libraries used.

* Special thanks to ETLab for permitting integration with their system.
