from fastapi import APIRouter, Request
from bson.json_util import loads, dumps
import json

import datetime
# https://fastapi.tiangolo.com/tutorial/bigger-applications/

router = APIRouter(
	prefix = "/staff_members",
#	tags = ["comments"],
	# responses ? 
)

@router.get("/")
async def get_staff_members(request: Request):
##	print('request is', request.app.mongodb)
	staff_members = request.app.mongodb["staff_members"].find({}).sort("view_rating", -1)
	staff_members = json.loads(dumps(staff_members))
#	print('comments are', comments)
	return {
		"status": "success",
		"staff_members": staff_members,
	}
