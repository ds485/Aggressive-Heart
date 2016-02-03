__author__ = 'ds'

from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.ods

collection1 = db.ods
collection2 = db.app
appelm = db.ApplicationElement

print db.collection_names()

dope = collection1.find()
blub = collection2.find()

env = appelm.find_one({"mime_type": "application/x-asam.aoenvironment"})

print env