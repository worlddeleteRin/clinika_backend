from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from typing import List
from utils import as_obj_id

class Category(BaseModel):
	id: str = None
	slug: str
	name: str
	parent_id: str = None
	ancestors: List = []
	def save(self, db_client):
		to_save = self.dict()
		if self.parent_id:
			to_save['parent_id'] = as_obj_id(self.parent_id)
		del to_save['id']
		result = db_client["catalogue"]["categories"].insert_one(to_save)
		self.id = str(result.inserted_id)
	def build_ancestors(self, collection):
		if not self.parent_id:
			print('dont have parent id')
			return None
		parent = collection.find_one(
		{"_id": as_obj_id(self.parent_id)},
		)
		print('parent is', parent)
		parent_ancestors = parent.pop('ancestors')
		ancestors = [ parent ] + parent_ancestors
		collection.update(
			{ "_id": as_obj_id(self.id)},
			{"$set": { 'ancestors': ancestors } }
		)

class PydanticObjectId(ObjectId):
	@classmethod
	def __get_validators__(cls):
		yield cls.validate
	@classmethod
	def validate(cls,v):
		if not isinstance(v, ObjectId):
			raise TypeError('ObjectId required')
		return str(v)

class MongoModel(BaseModel):
	class Config:
		allow_population_by_field_name = True
		arbitrary_types_allowed = True
		json_encoders  = {
			PydanticObjectId: str,
		}

class Product(BaseModel):
	id: str = Field(None)
# 	id: PydanticObjectId = Field(alias="_id")
	sku: str
	name: str
	description: str
	price: float
	imgsrc: List = []
	attributes: List = []
	def delete(self, collection):
		delete_status = collection.deleteOne( {"_id": ObjectId(self.id) })
		return delete_status


