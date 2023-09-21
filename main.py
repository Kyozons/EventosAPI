from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from routes.route import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(router)


# uri = "mongodb+srv://bustoslatorre:M0ng0dbp4ss@eventos.vxuigv2.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
# client = MongoClient(uri)
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pnged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
