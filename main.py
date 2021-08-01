from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

from models import Product, Category
# import motor.motor_asyncio
from bson.objectid import ObjectId
from bson import json_util
import json



db_host = "192.168.1.145"
db_port = "27017"
db_username = "admin"
db_password = "343845"

db_client = MongoClient("mongodb://{}:{}@{}".format(db_username, db_password, db_host))
# db_client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://{}:{}@{}".format(db_username, db_password, db_host))


app = FastAPI()
# setting up app cors
app.add_middleware(
	CORSMiddleware,
	allow_origins = ['*'],
	allow_methods = ['*'],
	allow_headers = ['*'],
)

@app.get("/status")
def get_status():
	""" Get status of server """
	return {"status": "running"}

