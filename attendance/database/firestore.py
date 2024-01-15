import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("./env/firebase_attendance_key.json")
app = firebase_admin.initialize_app(cred)
database = firestore.client()
