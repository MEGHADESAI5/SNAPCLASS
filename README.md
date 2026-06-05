# 🧠 SnapClass – AI Powered Attendance System

SnapClass is a next-generation AI-powered attendance system that revolutionizes classroom management using **Computer Vision, Voice Biometrics, and QR-based automation**.  
It enables fast, secure, and accurate student attendance tracking with minimal manual intervention.

---

## 🚀 Overview

SnapClass leverages advanced AI technologies to automate attendance using multiple biometric modalities:

- 📸 **Face Recognition (Computer Vision)**
- 🎙️ **Voice Biometrics (Audio AI)**
- 📱 **QR-Based Course Enrollment System**

The system is designed for **educational institutions** to improve efficiency, reduce manual workload, and enhance attendance accuracy.

---

## ✨ Key Features

### 📸 AI Face Analysis
- Detects and recognizes students from a single class image
- Uses deep learning-based facial embeddings
- Provides fast and highly accurate attendance marking

### 🎙️ Voice ID Recognition
- Students speak “Present” sequentially
- Uses voice embeddings to match stored biometric profiles
- Ensures secure and fraud-resistant attendance validation

### 📱 QR-Driven Enrollment
- Each course generates a unique QR code
- Enables instant student enrollment without manual entry
- Simplifies class onboarding process

---

## ⚙️ System Workflow

### 👨‍🏫 Teacher Journey

1. **Secure Login**
   - Encrypted authentication system for teachers

2. **Dashboard Access**
   - Manage subjects, students, and attendance records

3. **Course Creation**
   - Create subjects and generate QR codes automatically

4. **FaceID Attendance**
   - Capture classroom image and run AI recognition

5. **VoiceID Attendance**
   - Conduct real-time voice-based roll call

6. **Reports & Analytics**
   - Download attendance logs and track performance trends

---

### 🎓 Student Journey

1. **Instant Enrollment**
   - Join courses using QR code or invite link

2. **Biometric Registration**
   - Register FaceID and VoiceID once for authentication

3. **Personal Dashboard**
   - Track attendance percentage and updates in real time

---

## 🏗️ Tech Stack

### 🧠 AI / Machine Learning
- FaceRecognition (Dlib-based models)
- Librosa (Audio feature extraction)
- Resemblyzer (Voice embeddings)

### 💻 Backend & Frontend
- Flask (Web framework)
- Streamlit (Interactive UI)

### ☁️ Database & Cloud
- Supabase (PostgreSQL + Authentication)
- Real-time data synchronization

---

## 📊 System Capabilities

- Real-time biometric authentication
- Multi-modal AI (Face + Voice)
- Automated attendance tracking
- Secure cloud-based storage
- Scalable classroom architecture

---

## 🔐 Security Features

- Encrypted login system
- Biometric authentication for identity verification
- Secure cloud database (Supabase)
- Role-based access (Teacher / Student)

---

## 📦 Project Structure


SnapClass/
│
├── backend/ # AI models and core logic
├── frontend/ # UI (Streamlit / Flask)
├── models/ # Saved ML models (Face + Voice)
├── utils/ # Helper functions (preprocessing, etc.)
├── database/ # Supabase integration scripts
└── app.py # Main entry point


---

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/your-username/snapclass.git
cd snapclass
2. Install Dependencies
pip install -r requirements.txt
3. Run Application
python app.py
4. Open in Browser
http://localhost:5000
🎯 Future Improvements
Live classroom video streaming attendance
Mobile app integration
Emotion detection during attendance
Advanced analytics dashboard
Cloud deployment (AWS / Azure)
👨‍💻 Author

Megha Desai
GitHub: MEGHADESAI5

⭐ Impact

SnapClass simplifies classroom management by combining:

AI-powered automation
Biometric authentication
Real-time cloud tracking
