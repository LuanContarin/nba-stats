import crud.awards as crud

#! IMPORTANT
# Just for convenience, the "abbreviation"+"year" of award was decided as a "id", so finding an award depends on it.

def get_award_by_abbr_year():
    while True:
        abbr = input('Type the award\'s ID (3 char abbreviation): ')
        if abbr == '' or len(abbr) > 3:
            print('Input invalid.\n')
            continue

        year = input('Type the award\'s year: ')
        if not year.isdigit():
            print('Input invalid.\n')
            continue

        award = crud.get_by_abbr_year(abbr, year)
        print('Award found: ', award)
        return

def list_awards():
    awards = crud.list_all()
    
    print('List of awards:')
    for award in awards:
        print(award)

def create_award():
    while True:
        abbr = input('Award ID (3 char abbreviation): ')
        if abbr == '' or len(abbr) > 3:
            print('Input invalid.\n')
            continue

        year = input('Award year: ')
        if not year.isdigit():
            print('Input invalid.\n')
            continue

        player_name = input('Player name: ')
        if player_name == '':
            print('Input invalid.\n')
            continue
        
        error = crud.create(abbr, year, player_name)
        if error != None:
            print(error)
            return
        
        print('Award created successfully.')
        return

def update_award():
    while True:
        abbr = input('Type the award\'s ID (3 char abbreviation): ')
        if abbr == '' or len(abbr) > 3:
            print('Input invalid.\n')
            continue

        year = input('Type the award\'s year: ')
        if not year.isdigit():
            print('Input invalid.\n')
            continue

        player_name = input('New Player name: ')
        if player_name == '':
            print('Input invalid.\n')
            continue
        
        error = crud.update(abbr, year, player_name)
        if error != None:
            print(error)
            return
        
        print('Award updated successfully.\n')
        return

def delete_award():
    while True:
        abbr = input('Type the award\'s ID (3 char abbreviation): ')
        if abbr == '' or len(abbr) > 3:
            print('Input invalid.\n')
            continue

        year = input('Type the award\'s year: ')
        if not year.isdigit():
            print('Input invalid.\n')
            continue

        error = crud.delete(abbr, year)
        if (error != None):
            print(error)
            return

        print('Award deleted successfully.\n')
        return

def manage_awards():
    while True:
        print()
        print('=========== Awards ===========')
        print('  1 - Get by id (abbr) and year')
        print('  2 - List all')
        print('  3 - Create new award')
        print('  4 - Update existing award')
        print('  5 - Delete award')
        print('  0 - Return')
        operation = input('Select the operation... ')

        match operation:
            case '0':
                break
            case '1':
                get_award_by_abbr_year()
            case '2':
                list_awards()
            case '3':
                create_award()
            case '4':
                update_award()
            case '5':
                delete_award()
            case _:
                print('Invalid operation.\n')
