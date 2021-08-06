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

# /services/
# return all services list
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

# /services/some-service-slug
# return single service by slug
@router.get("/{slug}")
async def get_services(request: Request, slug: str):
	current_service = request.app.mongodb["services"].find_one({
		"slug": slug
	})
	print('current is', current_service)
	if not current_service:
		return {
			"status": "error",
			"current_service": None,
		}
	current_service = json.loads(dumps(current_service))
	return {
		"status": "success",
		"current_service": current_service,
	}
