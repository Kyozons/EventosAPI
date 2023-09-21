from pymongo import MongoClient

client = MongoClient("mongodb+srv://bustoslatorre:M0ng0dbp4ss@eventos.vxuigv2.mongodb.net/?retryWrites=true&w=majority") 

db = client.eventos_kultur

collection_name = db["eventos_collection"]
