import datetime
from config import get_database

COLLECTION_NAME = 'awards'

def get_by_abbr_year(abbr, year):
    db = get_database()
    awards = db[COLLECTION_NAME]

    return awards.find_one({ 'abbr': abbr, 'year': year })

def list_all():
    db = get_database()
    awards = db[COLLECTION_NAME]

    return awards.find({})

def create(abbr, year, recipient):
    db = get_database()
    awards = db[COLLECTION_NAME]

    award_exists = get_by_abbr_year(abbr, year)
    if award_exists != None:
        return 'Award already exists.'

    awards.insert_one({
        'abbr': abbr,
        'year': year,
        'recipient': recipient,
        'date_added': datetime.datetime.now(),
        'last_updated': datetime.datetime.now()
    })

def update(abbr, year, recipient):
    db = get_database()
    awards = db[COLLECTION_NAME]

    award_update = get_by_abbr_year(abbr, year)
    if (award_update == None):
        return 'Award not found.'

    query = { '_id': award_update['_id'] }
    new_values = { "$set": {
        'recipient': recipient,
        'last_updated': datetime.datetime.now()
    }}
    awards.update_one(query, new_values)

def delete(abbr, year):
    db = get_database()
    awards = db[COLLECTION_NAME]

    award_delete = get_by_abbr_year(abbr, year)
    if (award_delete == None):
        return 'Award not found.'

    awards.delete_one({ '_id': award_delete['_id'] })
