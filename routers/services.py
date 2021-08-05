from fastapi import APIRouter, Request
from bson.json_util import loads, dumps
import json

import datetime
# https://fastapi.tiangolo.com/tutorial/bigger-applications/

router = APIRouter(
	prefix = "/services",
#	tags = ["comments"],
	# responses ? 
)

@router.get("/")
async def get_services(request: Request):
##	print('request is', request.app.mongodb)
	services = request.app.mongodb["services"].find({}).sort("view_rating", -1)
	services = json.loads(dumps(services))
#	print('comments are', comments)
	return {
		"status": "success",
		"services": services,
	}
