from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Debugging step: Verify import
print("pymongo imported successfully")

uri = "mongodb+srv://arinateo:L0ALSGbGWNL4tEdb@arpad.s4edj.mongodb.net/?retryWrites=true&w=majority&appName=Arpad"

# Create a new client and connect to the server
try:
    client = MongoClient(uri, server_api=ServerApi('1'))
    print("MongoClient instantiated successfully")
    db = client.Blogging 
    blogs_collection = db["blogs"]
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"An error occurred: {e}")
    