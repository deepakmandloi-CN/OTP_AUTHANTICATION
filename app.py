import streamlit as st
import requests
import json

API_URL = "https://9kq8ztr1y5.execute-api.ap-southeast-2.amazonaws.com/prod/otp"

st.set_page_config(page_title="OTP Authentication", layout="centered")
st.title("OTP Authentication System")

email = st.text_input("Enter your email")

def show_response(r):
    try:
        data = r.json()
        body = json.loads(data["body"])
        msg = body.get("message", "No message")
    except Exception:
        msg = r.text or "Invalid server response"

    if r.status_code == 200:
        st.success(msg)
    else:
        st.error(msg)

if st.button("Send OTP", disabled=not email):
    r = requests.post(API_URL, json={
        "action": "send_otp",
        "email": email
    })
    show_response(r)

st.divider()

otp = st.text_input("Enter OTP")

if st.button("Verify OTP", disabled=not (email and otp)):
    r = requests.post(API_URL, json={
        "action": "verify_otp",
        "email": email,
        "otp": otp
    })
    show_response(r)
