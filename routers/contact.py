from fastapi import APIRouter, Request
from bson.json_util import loads, dumps
from pydantic import BaseModel, Field

import json

import datetime
# https://fastapi.tiangolo.com/tutorial/bigger-applications/

router = APIRouter(
#	prefix = "/comments",
#	tags = ["comments"],
	# responses ? 
)

class ContactInfo(BaseModel):
	name: str
	phone: str
	phone_mask: str

@router.post('/contact_request')
async def contact_request(contact_info: ContactInfo, request: Request):
#	contact_info = await request.json()
#	contact = ContactInfo(**contact_info)
	print('contact info is', contact_info)
	return {
		"status": "success",
	}

