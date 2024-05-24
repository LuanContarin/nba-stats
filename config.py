import pymongo

CONNECTION_STRING = 'mongodb://localhost:27017/'
DB_NAME = 'nba'

def get_database():
    client = pymongo.MongoClient(CONNECTION_STRING)
    return client[DB_NAME]