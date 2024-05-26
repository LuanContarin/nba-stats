import crud.games as crud
import datetime

#! IMPORTANT
# Just for convenience, the "date"+"home_team" of game was decided as a "id", so finding a game depends on it.

def parse_date(date_str):
    try:
        date_parsed = datetime.datetime.strptime(date_str, '%d/%m/%Y')
        return date_parsed
    except:
        return False

def is_date_valid(date_str):
    return bool(parse_date(date_str))

def is_date_in_future(date):
    return date > datetime.datetime.now()

def get_game_by_date_home_team():
    while True:
        date = input('Type the game\'s date (dd/MM/yyyy): ')
        if not is_date_valid(date):
            print('Input invalid.\n')
            continue

        home_team = input('Type the game\'s home team ID (3 char abbreviation): ')
        if home_team == '' or len(home_team) != 3:
            print('Input invalid.\n')
            continue

        game = crud.get_by_date_home_team(parse_date(date), home_team)
        print('Game found: ', game)
        return

def list_games():
    games = crud.list_all()
    
    print('List of games:')
    for game in games:
        print(game)

def create_game():
    while True:
        date = input('Game date (dd/MM/yyyy): ')
        if not is_date_valid(date) or is_date_in_future(parse_date(date)):
            print('Input invalid.\n')
            continue

        home_team = input('Home team ID (3 char abbreviation): ')
        if home_team == '' or len(home_team) != 3:
            print('Input invalid.\n')
            continue

        home_team_points = input('Home team points: ')
        if not home_team_points.isdigit():
            print('Input invalid.\n')
            continue

        away_team = input('Away team ID (3 char abbreviation): ')
        if away_team == '' or len(away_team) != 3:
            print('Input invalid.\n')
            continue

        away_team_points = input('Away team points: ')
        if not away_team_points.isdigit():
            print('Input invalid.\n')
            continue
        
        error = crud.create(parse_date(date), home_team, home_team_points, away_team, away_team_points)
        if error != None:
            print(error)
            return
        
        print('Game created successfully.')
        return

def update_game():
    while True:
        date = input('Type the game\'s date (dd/MM/yyyy): ')
        if not is_date_valid(date):
            print('Input invalid.\n')
            continue

        home_team = input('Type the game\'s home team ID (3 char abbreviation): ')
        if home_team == '' or len(home_team) != 3:
            print('Input invalid.\n')
            continue

        home_team_points = input('Home team points: ')
        if not home_team_points.isdigit():
            print('Input invalid.\n')
            continue

        away_team = input('Away team ID (3 char abbreviation): ')
        if away_team == '' or len(away_team) != 3:
            print('Input invalid.\n')
            continue

        away_team_points = input('Away team points: ')
        if not away_team_points.isdigit():
            print('Input invalid.\n')
            continue
        
        error = crud.update(parse_date(date), home_team, home_team_points, away_team, away_team_points)
        if error != None:
            print(error)
            return
        
        print('Game updated successfully.\n')
        return

def delete_game():
    while True:
        date = input('Type the game\'s date (dd/MM/yyyy): ')
        if not is_date_valid(date):
            print('Input invalid.\n')
            continue

        home_team = input('Type the game\'s home team ID (3 char abbreviation): ')
        if home_team == '' or len(home_team) != 3:
            print('Input invalid.\n')
            continue

        error = crud.delete(parse_date(date), home_team)
        if (error != None):
            print(error)
            return

        print('Game deleted successfully.\n')
        return

def manage_games():
    while True:
        print()
        print('=========== Games ===========')
        print('  1 - Get by date and home team')
        print('  2 - List all')
        print('  3 - Create new game')
        print('  4 - Update existing game')
        print('  5 - Delete game')
        print('  0 - Return')
        operation = input('Select the operation... ')

        match operation:
            case '0':
                break
            case '1':
                get_game_by_date_home_team()
            case '2':
                list_games()
            case '3':
                create_game()
            case '4':
                update_game()
            case '5':
                delete_game()
            case _:
                print('Invalid operation.\n')
