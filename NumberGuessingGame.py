import random


class NumberGuessingGame:
    random_number = random.randint(0, 9)
    print(random_number)
    print('Welcome to the Number Guessing game!')

    def __init__(self, rounds: int):
        self.rounds = rounds

    def guesses(self):
        user_input = 0
        try_number = 0
        while try_number < self.rounds:
            default2 = True
            while default2:
                try:
                    user_input = int(input('Guess a number between 0 and 9: '))
                    default2 = False
                except ValueError:
                    print('Please enter a value.')
            if user_input != self.random_number:
                print("That's wrong! Try again!")
                try_number += 1
                default2 = True
            else:
                print(f"That's correct!! You guessed it in round {try_number + 1}")
                break
        else:
            print('Sorry! You lost!')
