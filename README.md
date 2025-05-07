# 🏋️‍♂️ Program Builder Backend Service

This is a FastAPI-based backend service for generating personalized fitness programs using Anthropic Claude 3 and storing structured results in Firebase Firestore. The service integrates LangChain for AI prompt orchestration and is designed to work seamlessly with a frontend form-based UI.

---

## 🚀 What handled on the Server-Side

- 🔥 AI-powered fitness program generation using Claude 3 (via LangChain)
- 🧠 Prompt builder dynamically generates structured instructions from user inputs from the FE
- ☁️ Firebase Firestore integration to persist inputs and generated programs
- 🛠 PATCH support to update form fields and regenerate programs
- ✅ UUID-based `user_id` for safe program tracking
- 🔧 Modular FastAPI architecture for endpoints

---

## 📂 Folder Structure
<pre> 
program-builder-backend-service/
  ├── firebase/ # Firestore client setup 
  ├── models/ # Pydantic schemas for request/response 
  ├── routers/ # FastAPI API endpoints 
  ├── services/ # Business logic + Claude integration 
  ├── utils/ # Prompt builder for LangChain 
  ├── .env # Environment config 
  ├── main.py # FastAPI entry point 
  └── requirements.txt # Python dependencies 
</pre>

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/waseemjaved755/program-builder-backend-service.git
cd program-builder-backend-service
```
### 2. Create and Activate Virtual Environment
```bash
python3 -m venv venv
# macOS/Linux
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Setup Environment Variables
Create a .env file in the root directory and add your keys:
```bash
ANTHROPIC_MODEL=claude-3-5-sonnet-xxxx
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
FIREBASE_CREDENTIALS_PATH=firebase/firebase_service_account.json
```
🔐 Place your Firebase service account JSON inside the firebase/ folder

### 5. Run the Backend Server
```bash
uvicorn main:app --reload
```
### 6. Test API
Open your browser and go to:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 

### Result
<img width="1676" alt="Screenshot 2025-05-07 at 5 14 50 AM" src="https://github.com/user-attachments/assets/fda65f5d-9492-4869-8c85-08cf71952aa5" />

