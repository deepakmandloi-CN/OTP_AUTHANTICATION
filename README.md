# OTP_AUTHANTICATION

🔐 OTP Authentication System (AWS + Streamlit)

A production-ready OTP (One-Time Password) authentication system built using AWS Lambda, API Gateway, DynamoDB, Amazon SES, and Streamlit.

This project supports:

Email-based OTP delivery

Secure OTP verification

Expiry handling

Attempt limits

AWS-native, serverless architecture

🚀 Architecture Overview Streamlit UI | | (HTTP POST) v API Gateway (REST API) | v AWS Lambda (Python) | +--> DynamoDB (OTP storage + TTL) | +--> Amazon SES (Email OTP)

🛠️ Tech Stack Component Technology Frontend UI Streamlit (Python) Backend API AWS Lambda (Python 3.11) API Layer Amazon API Gateway Database Amazon DynamoDB Email Service Amazon SES (Sandbox / Prod) Hosting AWS Serverless ✨ Features

✅ 6-digit OTP generation

✅ OTP expiry (15 minutes)

✅ Max attempt limit (6 tries)

✅ DynamoDB TTL auto-cleanup

✅ SES Sandbox-safe email sending

✅ Full error handling & validation

✅ Streamlit UI with graceful error display

📂 Project Structure otp-authentication/ │ ├── lambda_function.py # AWS Lambda backend ├── app.py # Streamlit UI ├── requirements.txt # Python dependencies └── README.md # Project documentation

⚙️ AWS Setup Guide 1️⃣ DynamoDB Table

Create a table named:

otp_users

Primary Key

Partition Key: email (String)

Enable TTL

TTL attribute: otp_expiry

2️⃣ Amazon SES

Verify sender email

(Sandbox mode) Verify receiver emails

Region must match Lambda (e.g. ap-southeast-2)

Ensure SES permissions are attached to Lambda role

3️⃣ IAM Role Permissions (Lambda)

Attach the following permissions:

{ "Effect": "Allow", "Action": [ "ses:SendEmail", "ses:SendRawEmail", "dynamodb:PutItem", "dynamodb:GetItem", "dynamodb:UpdateItem" ], "Resource": "*" }

4️⃣ API Gateway

Create REST API

Method: POST

Enable Lambda Proxy Integration

Deploy stage: prod

🧠 Lambda Environment Configuration

Ensure Lambda:

Runtime: Python 3.11

Region: Same as SES & DynamoDB

Timeout: 10s recommended

Memory: 128 MB (sufficient)

🧪 API Request Format Send OTP { "action": "send_otp", "email": "user@example.com" }

Verify OTP { "action": "verify_otp", "email": "user@example.com", "otp": "123456" }

🖥️ Running Streamlit UI Install dependencies pip install streamlit requests

Run the app streamlit run app.py

🔒 Security Notes

OTP stored securely in DynamoDB

OTP auto-expires via TTL

Attempts capped to prevent brute-force

SES Sandbox prevents spam abuse

No OTP logged or exposed in UI

📌 Known Limitations

SES Sandbox requires email verification

SMS OTP not included (email only)

No session/token system (OTP only)

🚧 Future Enhancements

🔐 JWT Authentication after OTP

📱 SMS OTP via SNS

🧑‍🤝‍🧑 User registration & login

🔄 Resend OTP with cooldown

📊 Admin dashboard & analytics

👨‍💻 Author

Deepak Mandloi Cloud & Data Engineer AWS | Python | Serverless | Streamlit

⭐ Support

If you found this useful:

⭐ Star the repo

🛠️ Fork and improve

🐛 Open issues for suggestions
