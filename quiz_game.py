#Family Feud by Andy H 20220606

score = 0

class player1:
    def __init__(self, score):
        self.score = score

class player2:
    def __init__(self, score):
        self.score = score


print('Welcome to Family Feud Quiz Edition! Are you ready to play? ')
play = input().lower()

if play != "yes":
    exit()
#ctrl + [ = delete indentation

#Question 1

answer = input("Why might someone ride their bike to work? ")
if answer.lower() in ("no car","no transport"):
    print ("You said,",answer,"and the survey said",answer, "is 46 points.")
    score += 46
elif answer.lower() in ("exercise", "fitness", "staying fit"):
    print ("You said,",answer,"and the survey said",answer, "is 23 points.")
    score += 23
elif answer.lower() in ("gas","save gas"):
    print ("You said,",answer,"and the survey said",answer, "is 20 points.")
    score += 20
elif answer.lower() in ('pollution','less polution', 'less c02 emmissions','global warming','environment'):
    print ("You said,",answer,"and the survey said",answer, "is 7 points.")
    score += 7
else: 
    print ("You said,",answer,"and the survey said",answer, "is 0 points.")
    score += 0

#Question 2

answer2 = input("Name the qualities of a bad boss: ")
if answer2.lower() in ("micromanager","micromanagement"):
    print ("You said,",answer2,"and the survey said",answer2, "is 29 points.")
    score += 29
elif answer2.lower() in ("incompetent", "doesn't know what their doing", "lost", "can't do their job properly"):
    print ("You said,",answer2,"and the survey said",answer2, "is 24 points.")
    score += 24
elif answer2.lower() in ("angry","anger","mad","short temper", "no patience", "impatient","anger management"):
    print ("You said,",answer2,"and the survey said",answer2, "is 20 points.")
    score += 20
elif answer2.lower() in ('irresponsible','no responsibility','careless'):
    print ("You said,",answer2,"and the survey said",answer2, "is 14 points.")
    score += 14
else: 
    print ("You said,",answer2,"and the survey said",answer2, "is 0 points.")
    score += 0

#Question 3

answer = input("Other than illness, name an acceptable excuse for missing work: ")
if answer.lower() in ("funeral","death in the family"):
    print ("You said,",answer,"and the survey said",answer, "is 61 points.")
    score += 61
elif answer.lower() in ("car brokedown", "car accident", "car trouble", "public transport bad", "bus came late", "late bus", "traffic","bad traffic"):
    print ("You said,",answer,"and the survey said",answer, "is 30 points.")
    score += 30
elif answer.lower() in ("family emergency","emergency"):
    print ("You said,",answer,"and the survey said",answer,"is 6 points.")
    score += 6
else: 
    print ("You said,",answer,"and the survey said",answer, "is 0 points.")
    score += 0
    print ("And that concludes your round of Family Feud Quiz Edition, your score is", str(score),".")



play2 = input("Player 2, are you ready to play? ")
if play2.lower() != "yes":
    exit()
else: 
    questions()









# if (p1score>p2score):
#     print("Player 1 is the winner. CONGRATULATIONS PLAYER 1!")
# elif (p1score<p2score):
#     print("Player 2 is the winner. CONGRATULATIONS PLAYER 2!")
# else: 
#     print("Both players have tied. CONGRATULATIONS TO THE BOTH OF YOU!")

# print("Thank you for playing. We hope to see you at our next one!")


