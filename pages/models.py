from django.db import models
import pymongo 
# Create your models here.


connection = pymongo.MongoClient("mongodb://app:app@blu-shard-00-00-xttwj.mongodb.net:27017,blu-shard-00-01-xttwj.mongodb.net:27017,blu-shard-00-02-xttwj.mongodb.net:27017/test?ssl=true&replicaSet=Blu-shard-0&authSource=admin&retryWrites=true")
database = connection['testbd']
collection = database['members']
#data = {'KrishnaSri':'LokeshG','Sirisha':'LokeshB'}
#collection.insert_one(data)



def badella():
	return list(collection.find({}))
#collection.insert_one(data)