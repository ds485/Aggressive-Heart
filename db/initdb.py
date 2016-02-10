from pymongo import MongoClient

client = MongoClient()
db = input("DB name: ")
db = client[db]

user = input("init user: ")
password = input("init password: ")

env = {
    "mime_type": "application/x-asam.aoenvironment",
    "description": "desc",
    "application_model_type": "what is this"
}
user = {
    "mime_type": "application/x-asam.aouser",
    "name": user,
    "password": password
}
project_inst = {
    "mime_type": "application/x-asam.aotest.project",
    "name": "pro3",
}
mea_inst = {
    "mime_type": "application/x-asam.aomeasurement.mearesult",
    "name": "mea1"
}

result = db.AoEnvironment.insert(env)
result = db.AoUser.insert(user)
result = db.project.insert(project_inst)
result = db.mearesult.insert(mea_inst)
