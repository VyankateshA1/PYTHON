print("*** WELCOME TO KON BNEGA KRODPATI ***")
#INPUT NAME
contestantName = input("* What is your Name:\n")
print("WELCOME TO KBC MR.",contestantName)
#LOCATION
contestantLocation = input("* Where you came from:")
#how you feel at kbc
contestantThought = input("* Are You Excited....")
#START THE GAME
print("*** LET'S START THE GAME ***")
#QUESTIONS
questions = ["Capital of India?","India's Natinal Bird?","Longest River In World?"]
#ANSWERS
answers = ["New Delhi","Peacock","Nile 6650km"]
#PRIZE MONEY
a = 1000
b = 2000
c = 4000
d = 8000
#ADD MONEY
money = 0000
#MATCH
answer1 = input(questions[0])
if answer1 == answers[0]:
    money += a
    print("\n Congratulation You have Won ",money , "Rupees")
else:
    money =0000 
    print("\n It's Wrong Answer You Loose ", a,"Rupees")
    
print("You Have",money,"Prize money")

## SECOND QUESTION ANS

answer2 = input(questions[1])
if answer2 == answers[1]:
    money += b
    print("\n Congratulation You have Won ",money , "Rupees")
else:
    money =money 
    print("\n It's Wrong Answer You Loose ", b,"Rupees")
    
print("You Have",money,"Prize money")

## THIRD QUESTION ANS


answer3 = input(questions[2])
if answer3 == answers[2]:
    money += c
    print("\n Congratulation You have Won ",money , "Rupees")
else:
    money =money 
    print("\n It's Wrong Answer You Loose ", c,"Rupees")
    
print("You Have",money,"Prize money")
