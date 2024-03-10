# File:CS112_A1_T2_2_20230195
# Purpose:The first player to achieve a sum of 15 using numbers they choose from 1 to 9 wins
# Author:Samuel Samy Hakim
# ID:20230195
def valid(x, y):  # Function to validate players number input
    y = input("Enter a number player {}: ".format(x))
    while not y.isnumeric() or int(y) in picked_nums:
        print("please choose a valid number")
        print("Avaiable numbres is ", ava_numbers)
        y = input("Enter a number player {}: ".format(x))
    return y


# Welcome Massage
print("Welcome to the Number scrabble Game")
print("--------------------------")
print("Game Rule")
print("-----------------------")
print("There is a list of numbers between 1 and 9. Each player takes turns picking a number from the list."
      "Once a number has been picked,it cannot be picked again. "
      "If a player has picked three numbers that add up to 15,"
      "that player wins the game.However, if all the numbers are used and no player gets exactly 15, the game is a "
      "draw.")
print("-----------------------")
# Game starts Here
while True:
    choose = input("Would you like to play? (y/n) ")
    if choose.lower() == "y":  # If players choose to play
        sum_1 = 0
        sum_2 = 0
        num_1 = 0
        num_2 = 0
        ava_numbers = [1,2,3,4,5,6,7,8,9]
        picked_nums = []
        while True:
            # Player 1's turn
            x = 1
            print("Avaiable numbres are " ,ava_numbers)
            num_1 = int(valid(x, num_1))
            if num_1 in ava_numbers:
                ava_numbers.remove(num_1)
            if num_1 >= 1 and num_1 <= 9:
                sum_1 += num_1
                picked_nums.append(num_1)
                print("Picked numbers are ",picked_nums)
            if num_1 < 1 or num_1 > 9:
                print("Invalid")
                continue
            if sum_1 == 15:
                print("Player 1 wins!")
                break
            if len(picked_nums) == 9: # Draw condition
                print("Draw!")
                break
            # Player 2's Turn
            x = 2
            while True:
                print("Available numbers are ", ava_numbers)
                num_2 = int(valid(x, num_2))
                if num_2 >= 1 and num_2 <= 9:
                    sum_2 += num_2
                    picked_nums.append(num_2)
                    print("Picked numbers are ",picked_nums)
                    if num_2 in ava_numbers:
                        ava_numbers.remove(num_2)
                    break
                if num_2 < 1 or num_2 > 9:
                    print("Invalid")
                    continue
            if sum_2 == 15:
                print("Player 2 wins!")
                break
    elif choose.lower() == "n":  # If players choose not to play
        print("Thanks for playing!")
        break
    else:
        print("choose y or n")
        continue
