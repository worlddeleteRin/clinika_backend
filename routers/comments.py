from fastapi import APIRouter, Request
from bson.json_util import loads, dumps
import json

import datetime
# https://fastapi.tiangolo.com/tutorial/bigger-applications/

router = APIRouter(
	prefix = "/comments",
#	tags = ["comments"],
	# responses ? 
)

@router.get("/")
async def get_comments(request: Request):
##	print('request is', request.app.mongodb)
	comments = request.app.mongodb["comments"].find({}).sort("created_at", -1).limit(10)
	comments = json.loads(dumps(comments))
#	print('comments are', comments)
	return {
		"status": "success",
		"comments": comments,
	}
# /comments/
@router.post("/")
async def create_comment(request: Request):
	json = await request.json()
	print('request is', json)
	json = json["comment"]
	comment = {
		"name": json["name"],
		"content": json["content"],
		"created_at": int(datetime.datetime.now().timestamp())
	}
	print('comment is', comment)
	# inseting new comment to db
	request.app.mongodb["comments"].insert_one(comment)
	return {
		"status": "success",
	}

