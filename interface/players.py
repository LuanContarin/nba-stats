import crud.players as crud

#! IMPORTANT
# Just for convenience, the "name" of player was decided as a "id", so finding a player depends on it.

def get_player_by_name():
    name = input('Type the player\'s name: ')
    player = crud.get_by_name(name)

    print('Player found: ', player)

def list_players():
    players = crud.list_all()
    
    print('List of players:')
    for player in players:
        print(player)

def create_player():
    while True:
        name = input('Name: ')
        if name == '':
            print('Input invalid.\n')
            continue
        
        team = input('Team (3 char abbreviation): ')
        if team == '' or len(team) > 3:
            print('Input invalid.\n')
            continue
        
        position = input('Position (2 char abbreviation): ')
        if position == '' or len(position) > 2:
            print('Input invalid.\n')
            continue
        
        height = input('Height (cm): ')
        if not height.isdigit():
            print('Input invalid.\n')
            continue
        
        weight = input('Weight (Kg): ')
        if not weight.isdigit():
            print('Input invalid.\n')
            continue
        
        is_active = input('Is the player still active? (Y/n): ')
        is_active = False if is_active.lower() == 'n' else True
        
        error = crud.create(name, team, position, height, weight, is_active)
        if error != None:
            print(error)
            return
        
        print('Player created successfully.')
        return

def update_player():
    while True:
        name = input('Editing player\'s name: ')
        if name == '':
            print('Input invalid.\n')
            continue
        
        team = input('Team (3 char abbreviation): ')
        if team == '' or len(team) != 3:
            print('Input invalid.\n')
            continue
        
        position = input('Position (2 char abbreviation): ')
        if position == '' or len(position) > 2:
            print('Input invalid.\n')
            continue
        
        height = input('Height (cm): ')
        if not height.isdigit():
            print('Input invalid.\n')
            continue
        
        weight = input('Weight (Kg): ')
        if not weight.isdigit():
            print('Input invalid.\n')
            continue
        
        is_active = input('Is the player still active? (Y/n): ')
        is_active = False if is_active.lower() == 'n' else True
        
        error = crud.update(name, team, position, height, weight, is_active)
        if error != None:
            print(error)
            return
        
        print('Player updated successfully.\n')
        return

def delete_player():
    name = input('Type the player\'s name: ')
    
    error = crud.delete(name)
    if (error != None):
        print(error)
        return
    
    print('Player deleted successfully.\n')

def manage_players():
    while True:
        print()
        print('=========== Players ===========')
        print('  1 - Get by name')
        print('  2 - List all')
        print('  3 - Create new player')
        print('  4 - Update existing player')
        print('  5 - Delete player')
        print('  0 - Return')
        operation = input('Select the operation... ')

        match operation:
            case '0':
                break
            case '1':
                get_player_by_name()
            case '2':
                list_players()
            case '3':
                create_player()
            case '4':
                update_player()
            case '5':
                delete_player()
            case _:
                print('Invalid operation.\n')
