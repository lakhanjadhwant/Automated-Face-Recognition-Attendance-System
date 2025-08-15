from deepface import DeepFace
import streamlit as st

def detect_faces(image_path):
    try:
        return DeepFace.extract_faces(
            img_path=image_path,
            detector_backend='retinaface',
            enforce_detection=False,
            align=False
        )
    except Exception as e:
        st.error(f"Detection failed: {e}")
        return []
