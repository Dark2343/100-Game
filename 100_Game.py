# Date: 25/2/2022
# This is The 100 Game
# The premise of the game is: 2 players take turns choosing a number between 1 and 10
# Each number chosen is added to the total score
# Whoever can make the score reach 100 first is the winner

score = 0

while score != 100:

    # Player 1
    too_high = False
    while not too_high:

        # This is to check if the input is valid
        valid_input = False
        while not valid_input:
            try:
                player_1 = int(input("Player 1, Enter a number from 1 to 10\n"))
                if player_1 > 10 or player_1 < 1:
                    print("Invalid number\n")
                else:
                    score += player_1
                    valid_input = True
            except ValueError:
                print("Invalid, input must be numbers only\n")

            # This is to make sure the score doesn't go over 100
            if score > 100:
                print("Invalid")
                score -= player_1
            else:
                print(f'Current score is: ({score})\n')
                too_high = True

    # This is for the player who reaches 100 first
    if score == 100:
        print("Player 1 is the winner")
        break

    # Player 2
    too_high = False
    while not too_high:

        # This is to check if the input is valid
        valid_input = False
        while not valid_input:
            try:
                player_2 = int(input("Player 2, Enter a number from 1 to 10\n"))
                if player_2 > 10 or player_2 < 1:
                    print("Invalid number\n")
                else:
                    score += player_2
                    valid_input = True
            except ValueError:
                print("Invalid, input must be numbers only\n")

            # This is to make sure the score doesn't go over 100
            if score > 100:
                print("Invalid")
                score -= player_2
            else:
                print(f'Current score is: ({score})\n')
                too_high = True

    # This is for the player who reaches 100 first
    if score == 100:
        print("Player 2 is the winner")
        break
