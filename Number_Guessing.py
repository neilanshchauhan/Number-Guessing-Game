import random

logo = """
 $$$$$$\                                                  $$\     $$\                                                         $$\                           
$$  __$$\                                                 $$ |    $$ |                                                        $$ |                          
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\       $$$$$$\   $$$$$$$\   $$$$$$\        $$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      \_$$  _|  $$  __$$\ $$  __$$\       $$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\          $$ |    $$ |  $$ |$$$$$$$$ |      $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\         $$ |$$\ $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |        \$$$$  |$$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \______/  \______/  \_______|\_______/ \_______/          \____/ \__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      
                                                                                                                                                        
"""


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# print(random_no)
def game(life):
    random_no = random.randint(1,100)

    # for _ in range(life):    (Method_2 for Looping)
    while life:
        
        guess = int(input("Make a guess: "))
        if guess > random_no:
            print("Too High")
            life -= 1
        elif guess < random_no:
            print("Too low")
            life -= 1
        elif guess == random_no:
            print(f"You got it! The answer was {random_no} ")
            break
        if life == False:
            print("You've ran out of guesses. You Lose!!!")
            print(f"The number was {random_no}")

        
        

if difficulty == 'easy':
    
    print(f"You have 10 attempts remaining to guess the number.")
    game(10)

if difficulty == 'hard':
    
    print(f"You have 5 attempts remaining to guess the number.")
    game(5)
    