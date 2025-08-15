import gspread
from google.oauth2.service_account import Credentials
import streamlit as st

@st.cache_resource
def get_gsheet_client():
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    return gspread.authorize(credentials)

def mark_attendance(sheet_name, date_str, names):
    try:
        client = get_gsheet_client()
        sheet = client.open("Face_Attendance").worksheet(sheet_name)
        header = sheet.row_values(1)

        if date_str not in header:
            sheet.update_cell(1, len(header)+1, date_str)
            header.append(date_str)

        name_col = sheet.col_values(2)
        for idx, name in enumerate(name_col[1:], start=2):
            if name in names:
                col_idx = header.index(date_str) + 1
                sheet.update_cell(idx, col_idx, "P")

        return True
    except Exception as e:
        st.error(f"Failed to mark attendance: {e}")
        return False
