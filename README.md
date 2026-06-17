# Face Recognition Attendance System

## Project Overview

This project is a Face Recognition Attendance System developed using Python and OpenCV. The system detects faces through a webcam, recognizes registered users using the LBPH Face Recognizer, and automatically marks attendance with date and time.

## Features

* Face Detection using Haar Cascade Classifier
* Face Recognition using LBPH Face Recognizer
* Automatic Attendance Marking
* CSV-based Attendance Storage
* Duplicate Attendance Prevention
* Real-Time Webcam Recognition

## Technologies Used

* Python
* OpenCV
* NumPy
* CSV Module

## Project Workflow

1. Collect face images.
2. Train the LBPH Face Recognizer.
3. Detect faces through webcam.
4. Recognize registered users.
5. Record attendance with date and time.
6. Prevent duplicate attendance entries for the same day.

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Train the model:

python trainer.py

3. Run the attendance system:

python Attendance.py

## Future Improvements

* Multiple User Support
* GUI Interface
* Database Integration
* Attendance Reports
* Email Notifications

## Author

Bhagyashri Wani

B.Tech CSE (AIML)

Learning Computer Vision and Artificial Intelligence
