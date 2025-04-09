# picochu._.server

**Smart Attendance System** using **Raspberry Pi Pico**, **RFID (RC522)**, and **DS3231 RTC** integrated with a Flask API and MongoDB.

This project provides an API for handling attendance using RFID cards, saving records in MongoDB, and displaying them in a Student Mobile App. The system integrates with the college portal (ETLab) to fetch student attendance and display it.

## Features

- **RFID-based Attendance**: Students can mark attendance using RFID cards.
- **MongoDB Storage**: Attendance data is stored in a MongoDB database.
- **ETLab Integration**: Attendance data from the college portal is fetched and displayed on the Student Mobile App.
- **Admin Dashboard**: Admins can view and manage attendance data through an app.

## Technologies

- **Raspberry Pi Pico** (for scanning RFID cards and recording timestamps)
- **RFID (RC522)** (used to scan student IDs)
- **DS3231 RTC** (used for accurate timestamps)
- **Flask** (Python web framework for creating the API)
- **MongoDB** (database for storing attendance records)
- **Vercel** (for serverless deployment of the Flask API)

## API Endpoints

### `/get_attendance` (POST)
Fetches the attendance data for a student based on the provided username and password.

**Input**:
- `Username` (string): The student’s username.
- `Password` (string): The student’s password.

**Output**:
- JSON response with attendance data or error message.

Example Request:
```json
{
  "Username": "student123",
  "Password": "password123"
}
Example Response:

json
Copy
{
  "Status": "Success",
  "message": {
    "Subject1": "Present",
    "Subject2": "Absent"
  }
}
/get_attendance_list (POST)
Fetches the attendance list for a specific class based on class_id, date, hr, and sub_id.

Input:

Data (object): Contains class_id, date, hr, and sub_id.

Output:

JSON response with the attendance list or an error message.

Example Request:

json
Copy
{
  "Data": {
    "class_id": "CS101",
    "date": "2025-04-01",
    "hr": "10",
    "sub_id": "MATH"
  }
}
Example Response:

json
Copy
{
  "Status": "Success",
  "message": {
    "student_123": "Present",
    "student_456": "Absent"
  }
}
/receive_attendance_list (POST)
Receives and stores attendance data in MongoDB.

Input:

Data (object): Contains the attendance data to be inserted into MongoDB.

Output:

JSON response with a success message or error message.

Example Request:

json
Copy
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
Example Response:

json
Copy
{
  "Status": "Success",
  "message": "Data sent successfully."
}
Setup Instructions
Requirements
Python 3.x

MongoDB (you can use a cloud MongoDB service like MongoDB Atlas)

Vercel account for deployment

Install Dependencies
Clone the repository:

bash
Copy
git clone https://github.com/IamThejus/picochu._.server.git
cd picochu._.server
Install the required Python dependencies:

bash
Copy
pip install -r requirements.txt
Running Locally
To run the Flask app locally:

Install Vercel CLI:

bash
Copy
npm install -g vercel
Run the app locally with:

bash
Copy
vercel dev
Your app will be available at http://localhost:3000.

Deployment
To deploy the app on Vercel:

Deploy using the Vercel CLI:

bash
Copy
vercel
Follow the prompts to link your GitHub repository and deploy the app.

After deployment, your API will be accessible at the URL provided by Vercel.

Configuration
MongoDB URI: Set up your MongoDB URI in the code or using environment variables. For security reasons, avoid hardcoding sensitive information in the codebase.

Vercel Configuration: Ensure your vercel.json is set up correctly. Here's an example:

json
Copy
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
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the open-source community for the libraries and tools used in this project.

Special thanks to ETLab for allowing integration with their system.

vbnet
Copy

### Key Sections Explained:
- **Project Overview**: A concise description of the project and its functionality.
- **API Endpoints**: Describes each API route, including the HTTP method, expected input, and output. Example requests and responses are provided for each endpoint.
- **Setup Instructions**: Guides on how to clone the repository, install dependencies, and run the app locally.
- **Deployment**: Details the steps to deploy the app to Vercel, including the necessary configurations.
- **License and Acknowledgments**: Includes standard open-source sections like the MIT License and acknowledgments for external resources.

Feel free to update the **LICENSE** section with your actual license if it's different from MIT. Let me know if you need any further adjustments!

