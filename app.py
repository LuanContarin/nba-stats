from interface.players import manage_players

def menu():
    print('|-- NBA DATABASE MANAGER --|')
    print('  1 - Players')
    print('  2 - Teams')
    print('  3 - Statistics')
    print('  4 - Awards')
    print('  0 - Exit')

def main():
    while True:
        menu()
        option = input('Please select data to manage... ')

        match option:
            case '0':
                exit()
            case '1':
                manage_players()
            case _:
                print('Invalid option.\n')

if __name__ == "__main__":
    main()