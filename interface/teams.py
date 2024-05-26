import crud.teams as crud

#! IMPORTANT
# Just for convenience, the "abbreviation" of team was decided as a "id", so finding a team depends on it.

CONFERENCES = { '1': 'West', '2': 'East' }

def get_team_by_abbr():
    abbr = input('Type the team ID (3 char abbreviation): ')
    team = crud.get_by_abbr(abbr)

    print('Team found: ', team)

def list_teams():
    teams = crud.list_all()
    
    print('List of teams:')
    for team in teams:
        print(team)

def create_team():
    while True:
        abbr = input('Team ID (3 char abbreviation): ')
        if abbr == '' or len(abbr) != 3:
            print('Input invalid.\n')
            continue
        
        full_name = input('Full name: ')
        if full_name == '':
            print('Input invalid.\n')
            continue
        
        city = input('City: ')
        if city == '':
            print('Input invalid.\n')
            continue
        
        conference = input('Select conference (1 - West, 2 - East): ')
        if not CONFERENCES.get(conference):
            print('Input invalid.\n')
            continue
        
        error = crud.create(abbr, full_name, city, CONFERENCES.get(conference))
        if error != None:
            print(error)
            return
        
        print('Team created successfully.')
        return

def update_team():
    while True:
        abbr = input('Editing team\'s ID (3 char abbreviation): ')
        if abbr == '' or len(abbr) != 3:
            print('Input invalid.\n')
            continue
        
        full_name = input('Full name: ')
        if full_name == '':
            print('Input invalid.\n')
            continue
        
        city = input('City: ')
        if city == '':
            print('Input invalid.\n')
            continue
            
        conference = input('Select conference (1 - West, 2 - East): ')
        if not CONFERENCES.get(conference):
            print('Input invalid.\n')
            continue
            
        error = crud.update(abbr, full_name, city, CONFERENCES.get(conference))
        if error != None:
            print(error)
            return
            
        print('Team updated successfully.')
        return

def delete_team():
    abbr = input('Type the team\'s ID (3 char abbreviation): ')
    
    error = crud.delete(abbr)
    if (error != None):
        print(error)
        return
    
    print('Team deleted successfully.\n')

def manage_teams():
    while True:
        print()
        print('=========== Teams ===========')
        print('  1 - Get by id (abbr)')
        print('  2 - List all')
        print('  3 - Create new team')
        print('  4 - Update existing team')
        print('  5 - Delete team')
        print('  0 - Return')
        operation = input('Select the operation... ')

        match operation:
            case '0':
                break
            case '1':
                get_team_by_abbr()
            case '2':
                list_teams()
            case '3':
                create_team()
            case '4':
                update_team()
            case '5':
                delete_team()
            case _:
                print('Invalid operation.\n')
