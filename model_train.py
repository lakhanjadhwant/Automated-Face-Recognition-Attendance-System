# model_train.py

import os
import numpy as np
import pickle
from deepface import DeepFace
from PIL import Image

# Define your base folder
base_folder = "registered_faces"
model_name = "Facenet512"

# To store all embeddings and labels
embeddings = []
labels = []

# Loop through each folder (student)
for person in os.listdir(base_folder):
    person_folder = os.path.join(base_folder, person)
    if not os.path.isdir(person_folder):
        continue

    for img_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_name)
        try:
            embedding_obj = DeepFace.represent(img_path=img_path, model_name=model_name, enforce_detection=False)[0]
            embeddings.append(embedding_obj["embedding"])
            labels.append(person)
        except Exception as e:
            print(f"❌ Failed for {img_path}: {e}")

# Save embeddings and labels
with open("face_embeddings.pkl", "wb") as f:
    pickle.dump({"embeddings": embeddings, "labels": labels}, f)

print(f"✅ Training completed. Saved {len(embeddings)} embeddings.")
