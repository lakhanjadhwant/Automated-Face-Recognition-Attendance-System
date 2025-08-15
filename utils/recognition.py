from deepface import DeepFace
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recognize_face(face_img, stored_embeddings, stored_labels, model_name="Facenet512", threshold=0.4):
    try:
        face_embedding = DeepFace.represent(
            img_path=face_img,
            model_name=model_name,
            enforce_detection=False
        )[0]["embedding"]

        similarities = cosine_similarity([face_embedding], stored_embeddings)[0]
        max_idx = np.argmax(similarities)
        confidence = similarities[max_idx]

        if confidence >= (1 - threshold):
            name = stored_labels[max_idx]
        else:
            name = "Unknown"

        return name, round(confidence * 100, 2)
    except Exception as e:
        print(f"Recognition failed: {e}")
        return "Unknown", 0.0
