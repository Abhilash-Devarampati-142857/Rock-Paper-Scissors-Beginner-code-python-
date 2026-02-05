#Welcome to the code fot Rock Paper Scissors!
#Here we import random module which is the foundation for this code
import random
print("Welcome to Rock Paper Scissors!")
#Here we inform the user about the looping of the output till the user wins
print("This game goes on till you win.")
a=input("Do you want to play(Yes/No)?:")
#Here we inform the user about input being only of lowercase
print("From here on , it is requested that all your inputs given must be LOWERCASE!")
#Here we take the three moves of the game as a list
b=["rock","paper","scissors"]
#Here we use the imported random module to choose between every possible move
c=random.choice(b)
#Here before starting the loop,we take number of attempts taken to win(i) as 0
i=0
#Here we use whie loop to ensure the continuation of the code till the user wins
while True:
    if a=="yes" or a=="YES" or a=="Yes":
        print("Rock")
        print("Paper")
        print("Scissors")
        print("Shoot!")
        d=input("Enter your choice(rock,paper,scissors):")
        print("The computer's choice is:",c)
        #The number of attempts needed to win will increase proportionally  with the number of losses
        if (d=="rock" and c=="paper") or (d=="paper" and c=="scissors") or (d=="scisscors" and c=="rock"):
            print(c,"beats",d,". Computer wins. Try again.")
            i+=1
        #The code ends with the broken loop,which is a result of the user winning
        elif (d=="scissors" and c=="paper") or (d=="paper" and c=="rock") or (d=="rock" and c=="scissors"):
            print(d,"beats",c,". You win. Congratulations!")
            if i==0:
                print("You won in your first attempt.")
            else:
                print("You won in",i+1,"attempts.")
            break
        #The code takes a safety measure of the situation when the user input and the computer input match
        elif d==c:
            print("Oops. Seems like you and computer think the same. Please Try Again.")
        else:
            print("Invalid input. Please Try Again.")
    #The code will break if the user doesn't want to play the game
    else:
        print("Maybe Next Time!")
        break
#This code has been created,coded and edited by Abhilash Devarampati
