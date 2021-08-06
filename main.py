import uvicorn
from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware

# from models import Product, Category
# import motor.motor_asyncio
from bson.objectid import ObjectId
from bson import json_util
import json

# routes importing
from routers import comments, contact, services, staff_members, stock
# eof routes importing

# import database
from database import setup_mongodb

# include all necessary routes
app = FastAPI()
app.include_router(comments.router)
app.include_router(contact.router)
app.include_router(services.router)
app.include_router(staff_members.router)
app.include_router(stock.router)

@app.on_event('startup')
async def startup_db_client():
	setup_mongodb(app)
	print('now app is', app)
	print('app mongo db is', app.mongodb)
@app.on_event('shutdown')
async def shutdown_db_client():
	app.mongodb_client.close()



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


if __name__ == "__main__":
	uvicorn.run(
		"main:app",
		host='0.0.0.0',
		reload=True,
		port=8000,
	)
