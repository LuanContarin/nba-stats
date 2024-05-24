import datetime
from config import get_database

COLLECTION_NAME = 'teams'

def get_by_abbr(abbr):
    db = get_database()
    teams = db[COLLECTION_NAME]

    return teams.find_one({ 'abbr': abbr })

def list_all():
    db = get_database()
    teams = db[COLLECTION_NAME]

    return teams.find({})

def create(abbr, full_name, city, conference):
    db = get_database()
    teams = db[COLLECTION_NAME]

    team_exists = get_by_abbr(abbr)
    if team_exists != None:
        return 'Team already exists.'

    teams.insert_one({
        'abbr': abbr,
        'full_name': full_name,
        'city': city,
        'conference': conference,
        'date_added': datetime.datetime.now(),
        'last_updated': datetime.datetime.now()
    })

def update(abbr, full_name, city, conference):
    db = get_database()
    teams = db[COLLECTION_NAME]

    team_update = get_by_abbr(abbr)
    if (team_update == None):
        return 'Team not found.'

    query = { '_id': team_update['_id'] }
    new_values = { "$set": {
        'full_name': full_name,
        'city': city,
        'conference': conference,
        'last_updated': datetime.datetime.now()
    }}
    teams.update_one(query, new_values)

def delete(abbr):
    db = get_database()
    teams = db[COLLECTION_NAME]

    team_delete = get_by_abbr(abbr)
    if (team_delete == None):
        return 'Team not found.'

    teams.delete_one({ '_id': team_delete['_id'] })
