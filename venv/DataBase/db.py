from pymongo import MongoClient


client = MongoClient()
db = client.users
users = db.users


def new_user(id, contents=[]):
    user = {
        'id': id,
        'contents': contents
    }
    users.insert_one(user)

def find_user(id):
    user = users.find_one({'id': id})
    return user

def get_contents(id):
    matirials = users.find_one({'id': id})['contents']
    return matirials

def update_contents(id, new_content):
    users.apdate_one({'id': id}, {"$set": {"contents": get_contents(id).append(new_content)}})