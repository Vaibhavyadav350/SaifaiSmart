from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://vaibhavyadav160404:ZSWkj5sBTeWBVOxu@saifaismart.dfdyr3y.mongodb.net/?retryWrites=true&w=majority&appName=SaifaiSmart"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
