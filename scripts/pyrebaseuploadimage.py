import pyrebase
import uuid
from uuid import getnode as get_mac
import getpass
import datetime
import os

config = {
    "apiKey":"",
    "authDomain":"",
    "databaseURL": "",
    "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()

is_session=False

uid_str = uuid.uuid5(uuid.NAMESPACE_DNS,'python.org')
session = str(uid_str)+"PI"+str(uuid.uuid4())

mac_addr = get_mac()
pi_username = getpass.getuser()
name = str(mac_addr)+pi_username

storage_path = "pi-images/"+name+"/"+session+"/"

db.child("users").child(name)

data = {"created_date_time":str(datetime.datetime.now()),
        "image_url":"https:google.com/images"}

def pushData(data):
    db.child(session).push(data)
    
def setData(data):
    db.child(session).set(data)

def updateData(data):
    db.child(session).update(data)

def removeData():
    db.child(session).remove()

def uploadImage():
    file=os.path.basename('image1.jpg')
    storage.child(storage_path+"image1.jpg").put(file)
    image_url= storage.child(storage_path+"image1.jpg").get_url(1)
    print(image_url)
    data = {"created_date_time":str(datetime.datetime.now()),
        "image_url":image_url}
    pushData(data)


uploadImage()
