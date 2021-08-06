from fastapi import APIRouter, Request
from bson.json_util import loads, dumps
import json

import datetime
# https://fastapi.tiangolo.com/tutorial/bigger-applications/

router = APIRouter(
	prefix = "/stock",
#	tags = ["comments"],
	# responses ? 
)

@router.get("/")
async def get_stocks_list(request: Request):
##	print('request is', request.app.mongodb)
	stocks = request.app.mongodb["stocks"].find({}).sort("view_rating", -1)
	stocks = json.loads(dumps(stocks))
#	print('comments are', comments)
	return {
		"status": "success",
		"stocks": stocks,
	}

@router.get("/{slug}")
async def get_stocks_list(request: Request, slug: str):
##	print('request is', request.app.mongodb)
	current_stock = request.app.mongodb["stocks"].find({
		"slug": slug
	}).sort("view_rating", -1)
	current_stock = json.loads(dumps(current_stock))
	if len(current_stock) == 0:
		return {
			"status": "error",
			"current_stock": None,
		}
	# print('', comments)
	return {
		"status": "success",
		"current_stock": current_stock[0],
	}
