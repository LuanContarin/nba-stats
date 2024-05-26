import datetime
from config import get_database

COLLECTION_NAME = 'games'

def get_by_date_home_team(date, home_team):
    db = get_database()
    games = db[COLLECTION_NAME]

    return games.find_one({ 'date': date, 'home_team': home_team })

def list_all():
    db = get_database()
    games = db[COLLECTION_NAME]

    return games.find({})

def create(date, home_team, home_team_points, away_team, away_team_points):
    db = get_database()
    games = db[COLLECTION_NAME]

    game_exists = get_by_date_home_team(date, home_team)
    if game_exists != None:
        return 'Game already exists.'

    games.insert_one({
        'date': date,
        'home_team': home_team,
        'home_team_points': int(home_team_points),
        'away_team': away_team,
        'away_team_points': int(away_team_points),
        'date_added': datetime.datetime.now(),
        'last_updated': datetime.datetime.now()
    })

def update(date, home_team, home_team_points, away_team, away_team_points):
    db = get_database()
    games = db[COLLECTION_NAME]

    game_update = get_by_date_home_team(date, home_team)
    if (game_update == None):
        return 'Game not found.'

    query = { '_id': game_update['_id'] }
    new_values = { "$set": {
        'home_team_points': int(home_team_points),
        'away_team': away_team,
        'away_team_points': int(away_team_points),
        'last_updated': datetime.datetime.now()
    }}
    games.update_one(query, new_values)

def delete(date, home_team):
    db = get_database()
    games = db[COLLECTION_NAME]

    game_delete = get_by_date_home_team(date, home_team)
    if (game_delete == None):
        return 'Game not found.'

    games.delete_one({ '_id': game_delete['_id'] })
