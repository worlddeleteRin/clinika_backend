from fastapi import FastAPI
from pymongo import MongoClient
from .secure import db_host, db_port, db_username, db_password, database_name


# db_host = ""
#db_port = ""
#db_username = ""
#db_password = ""
#database_name = ''

# db_client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://{}:{}@{}".format(db_username, db_password, db_host))
def setup_mongodb(app: FastAPI) -> None:
	db_client = MongoClient("mongodb://{}:{}@{}".format(db_username, db_password, db_host))
	app.mongodb_client = db_client
	app.mongodb = db_client[database_name]




