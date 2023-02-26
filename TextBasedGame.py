#Ian Viguera Rivera

def show_instructions():
    print('Escape House Text Game')
    print('Collect 5 keys to escape and avoid the lurking ghost.')
    print('Move commands: go East, go West, go South or go North')
    print('Add to inventory: find Key')

def show_note():
    print('Journal log #17:')
    print('Found the Red Key, set it beside the nightstand in the Bedroom.')
    print('I spotted the Blue Key by the Guess Room.')
    print('Dropped the Yellow Key in the Bathroom.')
    print('The green Key is in the Kitchen beside the lettuce, Ghost has a sense of humor.')
    print('I guess the Purple Key might be in the Garage.')
    print('Saw the Ghost last in the study. Got to be careful.')


def main():
    rooms = {
        'Bedroom': {'West': 'Guess room'},
        'Guess Room': {'West': 'Bathroom', 'South': 'Living Room', 'East': 'Bedroom'},
        'Bathroom': {'East': 'Guess room'},
        'Study': {'West': 'Living room', 'South': 'Kitchen'},
        'Living Room': {'West': 'Main entrance', 'South': 'Garage', 'East': 'Study', 'North': 'Guess Room'},
        'Kitchen': {'West': 'Garage', 'North': 'Study'},
        'Garage': {'East': 'Kitchen', 'North': 'Living room'},
        'Main Entrance': {'East': 'Living room'}
    }
    current_room = 'Bedroom'
    command = ''
    items = ['Red Key', 'Blue Key', 'Yellow Key', 'Green Key', 'Purple Key']
    stored_items = []
    found_keys = ''

    # Game Parameter
    while command != 'Exit':
        possible_moves = rooms[current_room].keys()
        print('You are in the ', current_room)
        print('Possible Moves: ', *possible_moves)

        command = input('Choose Your Move: ')
        direct_command = command.split(' ')
        direct_command = direct_command[1]

        print('You Chose: ', direct_command)
        print('')

        if direct_command in possible_moves:
            if direct_command in possible_moves:
                # Moving from Guess Room
                if current_room == 'Bedroom' and direct_command == 'West':
                    current_room = 'Guess Room'
                    continue
                elif current_room == 'Guess Room' and direct_command == 'South':
                    current_room = 'Living Room'
                    continue
                elif current_room == 'Guess Room' and direct_command == 'West':
                    current_room = 'Bathroom'
                elif current_room == 'Guess Room' and direct_command == 'East':
                    current_room = 'Bedroom'

                    # Moving from Bathroom
                if current_room == 'Bathroom' and direct_command == 'East':
                    current_room = 'Guess Room'

                    # Moving from Living Room
                if current_room == 'Living Room' and direct_command == 'West':
                    current_room = 'Main Entrance'
                elif current_room == 'Living Room' and direct_command == 'East':
                    current_room = 'Study'
                elif current_room == 'Living Room' and direct_command == 'North':
                    current_room = 'Guess Room'
                elif current_room == 'Living Room' and direct_command == 'South':
                    current_room = 'Garage'

                    # Moving from Garage
                if current_room == 'Garage' and direct_command == 'North':
                    current_room = 'Living Room'
                elif current_room == 'Garage' and direct_command == 'East':
                    current_room = 'Kitchen'

                    # Moving from Kitchen
                if current_room == 'Kitchen' and direct_command == 'North':
                    current_room = 'Study'
                elif current_room == 'Kitchen' and direct_command == 'West':
                    current_room = 'Garage'

                    # Game Objective
                if current_room == 'Main Entrance':
                    stored_items = set(stored_items)
                    items = set(items)
                    if direct_command == 'East':
                        current_room = 'Living Room'
                    if stored_items == items:
                        print('Congratulations!')
                        print('You Escaped the haunted house!')
                        print('Thanks for playing!')
                        print('')
                        print('Play Again?')
                        pa = input('Y/N: ')
                        print('')
                        if pa == 'Y':
                            return main_menu()

                        elif pa == 'N':
                            command = 'Exit'
                    else:
                        print('Keys Missing!')
                        print('Go Back!')
                        print('')
                elif current_room == 'Main Entrance' and direct_command == 'East':
                    current_room = 'Living Room'

                    # Game ending room
                if current_room == 'Study':
                    print('You Were Captured by the Ghost!')
                    print('Game Over!')
                    print('')
                    print('Play Again?')
                    pa = input('Y/N: ')
                    if pa == 'Y':
                        print('')
                        return main_menu()
                    elif pa == 'N':
                        command = 'Exit'
        elif direct_command not in possible_moves:
            if direct_command != 'Key':
                print('Invalid Move')
                print('')

        # Storing inventory
        if direct_command == 'Key' and current_room == 'Living Room':
            print('No Key Here!')
            print('')
        elif direct_command == 'Key':

            for found_keys in items:
                if current_room == 'Bedroom':
                    found_keys = 'Red Key'
                if current_room == 'Guess Room':
                    found_keys = 'Blue Key'
                if current_room == 'Bathroom':
                    found_keys = 'Yellow Key'
                if current_room == 'Kitchen':
                    found_keys = 'Green Key'
                if current_room == 'Garage':
                    found_keys = 'Purple Key'
            if found_keys in stored_items:
                if found_keys == found_keys:
                    del stored_items[-1]
                    print('Key Already Searched')
                    print('')

            stored_items.append(found_keys)
            print('You found the ', found_keys)
            print('Inventory: ', stored_items)
            print('')

def main_menu():
    print('Welcome to Escape House Text Game!')
    print('Type Start: To start game')
    print('Type Instructions: To show Instructions')
    print('Type Note: To read hint note')
    user_input = input()

    # Start Function
    if user_input == 'Start':
        print('')
        main()

    # Instructions Function
    elif user_input == 'Instructions':
        print('')
        show_instructions()
        print('')
        b = input('Type B for back ')
        if b == 'B':
            print('')
            return main_menu()
    # Note Function
    elif user_input == 'Note':
        print('')
        show_note()
        print('')
        b = input('Type B for back ')
        if b == 'B':
            print('')
            return main_menu()
main_menu()