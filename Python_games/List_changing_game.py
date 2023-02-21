# A python game to change the list acording to user input
# Basics
# DISPLAY
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


# ASKING FOR USER INPUT
def user_choice():
    # Variables

    # Initial

    choice = 'WRONG'
    acceptable_range = range(1, 10)
    within_range = False

    # Two conditions to check

    # Digit or within_range==False
    while choice.isdigit() == False or within_range == False:
        choice = input('Enter a number between(1-10): ')
        # Digit Check
        if choice.isdigit() == False:
            print('Sorry! that was not a digit')
        # Range Check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry! you are out of acceptable range(0-10)')
                within_range = False
    print(int(choice))


# Short Game
def display_game(game_list):
    print('Here is the current list')
    print(game_list)


def position_choice():
    choice = 'wrong'
    while choice not in ['0', '1', '2']:
        choice = input('Pick a position (0,1,2): ')
        if choice not in ['0', '1', '2']:
            print('sorry! Invalid choice!')
    return int(choice)


def replacement_choice(game_list, position):
    user_placement = input('Type a string to place at position: ')
    game_list[position] = user_placement
    return game_list


def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y', 'N']:
        choice = input('Keep Playing? (Y or N): ')
        if choice not in ['Y', 'N']:
            print('sorry! I dont understand, please choose Y or N ')
    if choice =='Y':
        return True
    else:
        return False


game_on = True
game_list = [0, 1, 2]
while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()