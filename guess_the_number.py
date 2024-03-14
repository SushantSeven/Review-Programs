# @Author: sushant Das

# @Date: 2024-03-11 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Guess the random number game

import random

def guess_number(upper_bound):
    random_number = random.randint(1,upper_bound)
    ub = upper_bound
    lb = 1
    while True:
        number = int(input("Guess the number: "))
        if number == random_number:
            print(f"Congratulations You guessed it right! the number is {random_number}")
            return False
        else:
            print("Wrong guess!Try again")
            if number<random_number:
                print(f"Try in range {number} to {ub}") 
                lb = number
            else:
                print(f"Try in range {lb} to {number}")
                ub = number
        

if __name__=="__main__":
    upper_bound = int(input("Lower range is 1, Enter the upper range: "))
    guess_number(upper_bound)