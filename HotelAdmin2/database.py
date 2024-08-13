import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

class Database:
    def __init__(self):
        cred = credentials.Certificate("key.json")


        default_app = firebase_admin.initialize_app(cred, {
            'databaseURL' :  "https://console.firebase.google.com/u/0/project/fir-practice-c156a/database/fir-practice-c156a-default-rtdb/data/~2F"
            })


        self.ref = db.reference("/")


    def pull(self):
# Pull latest data from firebase and store in file called firebase_data.json

        self.data = self.ref.get()

        if not isinstance(self.data,dict):
            self.data = self.data.val()

        with open("firebase_data.json", "w") as f:
            json.dump(self.data,f, indent = 4)

    def removeCustomer(self, id):
        with open("firebase_data.json", "r") as f:
            data = json.load(f)
            del data[id]

        with open("firebase_data.json", "w") as f:
            json.dump(data, f, indent = 4)


