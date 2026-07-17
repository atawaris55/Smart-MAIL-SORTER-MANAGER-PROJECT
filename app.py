import sqlite3
import pandas as pd
import streamlit as st
from src.database import create_database, insert_email
import os

if not os.path.exists("database/email.db"):
    create_database()
    insert_email()

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="SmartMail AI",
    page_icon="📧",
    layout="wide"
)

st.title("📧 SmartMail AI")
st.write("Welcome to Smart Email Management System")

# ----------------------------
# Load Emails from Database
# ----------------------------
@st.cache_data
def load_emails():
    conn = sqlite3.connect("database/email.db")
    df = pd.read_sql("SELECT * FROM emails", conn)
    conn.close()
    return df

emails = load_emails()

# ----------------------------
# Dashboard
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Emails", len(emails))

with col2:
    st.metric("Unique Senders", emails["sender"].nunique())

st.divider()

st.subheader("📬 Email List")
st.dataframe(emails, use_container_width=True)

st.divider()

st.subheader("📊 Emails by Sender")

sender_count = emails["sender"].value_counts()
st.bar_chart(sender_count)