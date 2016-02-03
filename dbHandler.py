__author__ = 'ds'

from pymongo import MongoClient

db = None


def get_db():
    global db
    if db is not None:
        return db
    db = dbHandler().client
    return db


class dbHandler():
    def __init__(self):
        client = MongoClient('localhost', 27017)
        # TODO: some exception if db off
        self.client = client.ods
        # TODO: ods muss eignetlich aus der config gelesen werden