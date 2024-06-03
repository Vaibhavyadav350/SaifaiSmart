# myapp/mongo_connector.py

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://vaibhavyadav160404:ZSWkj5sBTeWBVOxu@saifaismart.dfdyr3y.mongodb.net/?retryWrites=true&w=majority&appName=SaifaiSmart"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
