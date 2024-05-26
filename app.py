from interface import players, teams, awards, games

def menu():
    print('|-- NBA DATABASE MANAGER --|')
    print('  1 - Players')
    print('  2 - Teams')
    print('  3 - Games')
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
                players.manage_players()
            case '2':
                teams.manage_teams()
            case '3':
                games.manage_games()
            case '4':
                awards.manage_awards()
            case _:
                print('Invalid option.\n')

if __name__ == "__main__":
    main()
