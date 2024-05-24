from config import get_database

COLLECTION_NAME = 'players'

def get_by_name(name):
    db = get_database()
    players = db[COLLECTION_NAME]

    return players.find_one({ 'name': name })

def list_all():
    db = get_database()
    players = db[COLLECTION_NAME]

    return players.find({})

def create(name, team, position, height, weight, is_active):
    db = get_database()
    players = db[COLLECTION_NAME]

    player_exists = get_by_name(name)
    if player_exists != None:
        return 'Player already exists.'

    players.insert_one({
        'name': name,
        'team': team,
        'position': position,
        'height': int(height),
        'weight': int(weight),
        'is_active': is_active
    })

def update(name, team, position, height, weight, is_active):
    db = get_database()
    players = db[COLLECTION_NAME]

    player_update = get_by_name(name)
    if (player_update == None):
        return 'Player not found.'

    query = { '_id': player_update['_id'] }
    new_values = { "$set": {
        'name': name,
        'team': team,
        'position': position,
        'height': int(height),
        'weight': int(weight),
        'is_active': is_active
    }}
    players.update_one(query, new_values)

def delete(name):
    db = get_database()
    players = db[COLLECTION_NAME]

    player_delete = get_by_name(name)
    if (player_delete == None):
        return 'Player not found.'

    players.delete_one({ '_id': player_delete['_id'] })
