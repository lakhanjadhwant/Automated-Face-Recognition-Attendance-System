import streamlit as st
import datetime
from PIL import Image
import tempfile

from config import SUBJECTS, RECOGNITION_THRESHOLD, DEFAULT_DATE, SPREADSHEET_VIEW_URL
from utils.embeddings import load_embeddings
from utils.detection import detect_faces
from utils.recognition import recognize_face
from utils.sheets import mark_attendance

# Setup page
st.set_page_config(page_title="Face Recognition Attendance", layout="centered")
st.title("📸 Face Recognition Attendance System")

# Load face embeddings
stored_embeddings, stored_labels = load_embeddings()

# Select Subject
selected_subject = st.selectbox("📚 Select Subject", SUBJECTS)
selected_date = st.date_input("📅 Select Date", value=DEFAULT_DATE)
date_str = selected_date.strftime("%d-%m-%Y")

# Upload Images
uploaded_files = st.file_uploader("📤 Upload Group Photos", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Process
if uploaded_files and selected_subject != "Choose Subject" and st.button("🔍 Detect, Recognize and Mark Attendance"):
    recognized_names = set()

    for uploaded_file in uploaded_files:
        st.markdown(f"---\n### 📸 `{uploaded_file.name}`")
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Original Image", use_container_width=True)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            image.save(tmp_file.name)
            faces = detect_faces(tmp_file.name)

        if faces:
            st.success(f"✅ Detected {len(faces)} face(s).")
            cols = st.columns(5)

            for i, face in enumerate(faces):
                face_array = face["face"]
                face_img = Image.fromarray((face_array * 255).astype("uint8"))

                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as f_tmp:
                    face_img.save(f_tmp.name)
                    name, confidence = recognize_face(f_tmp.name, stored_embeddings, stored_labels, threshold=RECOGNITION_THRESHOLD)

                if name != "Unknown":
                    recognized_names.add(name)

                cols[i % 5].image(face_img, caption=f"{name} ({confidence}%)", use_container_width=True)
        else:
            st.warning("No faces detected.")

    # Attendance
    if recognized_names:
        st.success(f"🎉 Total Recognized (Unique): {len(recognized_names)}")
        st.info("📝 Names: " + ", ".join(recognized_names))

        if mark_attendance(selected_subject, date_str, recognized_names):
            st.success(f"✅ Attendance marked in **{selected_subject}** for **{date_str}**!")
            st.markdown(f"🔗 [View Attendance Sheet]({SPREADSHEET_VIEW_URL})", unsafe_allow_html=True)
        else:
            st.error("❌ Failed to mark attendance.")
    else:
        st.warning("⚠️ No recognizable faces found.")
