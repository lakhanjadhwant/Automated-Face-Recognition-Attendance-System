# Automated Face Recognition Attendance System

An **AI-powered attendance system** that uses deep learning for face detection and recognition to automate the process of marking attendance. The application allows users to select a subject and date, upload classroom images, detect and recognize student faces, and automatically mark attendance in a Google Sheet in real time.

---

## 🚀 Features

- **Automated Attendance** – Marks attendance directly from classroom images.  
- **Face Detection & Recognition**:  
  - **RetinaFace** for high-accuracy face detection.  
  - **FaceNet512** embeddings for recognition.  
- **User-Friendly Interface** – Built with **Streamlit** for simple and intuitive use.  
- **Real-Time Data Updates** – Integrates with Google Sheets using **Gspread**.  
- **Cloud Integration** – Uses **GCP service accounts** for secure access and data management.  
- **Scalable** – Works efficiently for small and large classrooms.

---

## 🛠️ Technologies Used

- **Python**  
- **Streamlit** – UI framework  
- **DeepFace** – Face detection & recognition  
- **Scikit-learn** – Cosine similarity for embedding comparison  
- **Gspread** – Google Sheets API integration  
- **Google Cloud Platform (GCP)** – Credential management and secure API access  

---

## 📋 How It Works

1. Select the subject and date from the application interface.  
2. Upload classroom images.  
3. Detect and recognize faces in the images using **DeepFace**.  
4. Mark attendance based on recognized students.  
5. Update the attendance data in Google Sheets in real time.
