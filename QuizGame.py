print("Welcom to the Quiz Game")

play = input("Ready to Start?")

if play.lower() !="yes":
    quit()

print("Okey let's play :)")
score = 0

answer = input("In which type of computer, data are represented as discrete signals?  ")
if answer.lower() == "digital computer":
    print(' Correct ')
    score += 1
else:
    print("Incorrect")    


answer = input("What is the name of an application program that gathers user information and sends it to someone through the Internet?   ")
if answer.lower() == " spybot ":
    print(' Correct ')
    score += 1
else:
    print("Incorrect")  


answer = input("Which of the following is a network topology?   ")
if answer.lower() == " BUS ":
    print(' Correct ')
    score += 1
else:
    print("Incorrect")  


answer = input(" What is the most common tool used to restrict access to a computer system?  ")
if answer.lower() == " password ":
    print(' Correct ')
    score += 1
else:
    print("Incorrect")   

print("You Got " + str(score) +" questions correct")   
print("You Got " + str((score/4) * 100) + "%")

