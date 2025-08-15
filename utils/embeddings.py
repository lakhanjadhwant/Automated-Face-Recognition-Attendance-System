import pickle
import numpy as np
import streamlit as st

@st.cache_resource
def load_embeddings():
    with open("face_embeddings.pkl", "rb") as f:
        data = pickle.load(f)
    return np.array(data["embeddings"]), data["labels"]
