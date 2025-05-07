import firebase_admin
from firebase_admin import credentials, firestore
import os

cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "firebase/program-builder-task-firebase-adminsdk-fbsvc-be6dc90456.json")
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()
