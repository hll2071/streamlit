import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("secret.json")
firebase_admin.initialize_app(cred)
# Import database module.
from firebase_admin import db

# Get a database reference to our posts
ref = db.reference(url = 'https://test-33630-default-rtdb.firebaseio.com/')
ref.update({"hi":1234})
ref = db.reference('key',url = 'https://test-33630-default-rtdb.firebaseio.com/')
# Read the data at the posts reference (this is a blocking operation)
print(ref.get())