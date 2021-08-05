from fastapi import FastAPI
from pymongo import MongoClient


db_host = "192.168.1.110"
db_port = "27017"
db_username = "admin"
db_password = "343845"
database_name = 'miraclinic'

# db_client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://{}:{}@{}".format(db_username, db_password, db_host))
def setup_mongodb(app: FastAPI) -> None:
	db_client = MongoClient("mongodb://{}:{}@{}".format(db_username, db_password, db_host))
	app.mongodb_client = db_client
	app.mongodb = db_client[database_name]




