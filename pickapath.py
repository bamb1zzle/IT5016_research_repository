#Pick A Path Story - "Escape the Thieves!" By Andy H 20220606

#intro 
print ("************************************************\nWelcome to the game, Escape the Thieves!\n************************************************\nIn this game you are playing a hotel guest who has just entered her best friends apartment to have dinner.\nOnce entering the apartment unannounced as always, you walk into the hall to see her body on the floor soaked in a pool of blood with a group of individuals dressed in all black putting her valuables into their bags. They spot you and proceed to chase you out of the apartment. You enter your apartment a few doors down and lock the door but they are quick on your tail and are trying to break the door as we speak!\nWhat do you do?")

#StartingOptions
print("1. Open the door to the thieves, telling them you will pretend you didn't see anything and hope they spare your life.")
print("2. Go down the hall further away from the door.")

do= int(input(""))

if do == 1:
    print("The murders are not so merciful and decide to kill you. \n ***GAME OVER***")
    exit()

elif do == 2:
    print("You make your way down the hall and the robbers are seconds away from bursting your front door open. You meet two doors at the end of the hall. Which door do you enter?")
    print("1. Your bedroom door that has a window open to the fire escape.")
    print("2. Your bathroom door that has the most sturdiest door in the apartment but no escape.")

    do =int(input(""))
    if do == 1:
        print("You enter your room but the robbers had just caught a glimpse of you whilst bursting open the door and proceed to run down the hall to chase you.")
        print("Do you:\n1. Hide in your closet that looks too small to hide anything and hope they don't bother checking. \n2. Open your bedroom window and hop out to the fire escape.")
        
        do = int(input(""))
        if do == 1: 
            print("You run into your master closet and hide in the closet amongst your dresses. The thieves enter into your bedroom and proceed to go into your closet and find you quickly. You are now dead. \n ***GAME OVER***")
        else:
            print("You hop onto the fire escape. Do you go UP or DOWN the escape?")

            do = str(input(""))
            if do.lower() == "up": 
                print("You proceed to run up the stairs all the way to the roof.")
                print("The robbers have now caught up to you on the roof. There is no escape. You die. \n ***GAME OVER***")
            else:
                print("You go down the fire escape but due to the old age of the building the ladder to the ground of the fire escape doesn't extend and you are caught by the robbers and disposed of in the garbage bins. \n***GAME OVER*** ")
    
    else:
        print("You enter your bathroom and call the police to alert them what has happened. Although the locked door is sturdy, you know it wont be long until they break the door and the police are still 15 minutes away. What do you do?")
        print("1. Grab the gun you hide in the tank of your toilet. \n2. Sit in the corner of your bathroom against the wall and wonder where your life went wrong.")

        do = int(input(""))
        if do == 1:
            print("As the thieves finally open the door after continuous barrage of kicks and body slams they are surprised to see you with a weapon. You shoot one of them but end up being tackled by the rest and die.\n***GAME OVER***")
        else: 
            print("While sitting against the corner of the bathroom and reflecting on your life you notice that theres a weak layer against the wall. You begin to probe the wall and notice two bricks that can be fully indented and pushed into the wall. Which brick do you press into? LEFT or RIGHT?")  
            
            do = str(input(""))
            if do.lower() ==("left"):
                print("You open a trap door beneath you that gives you enough space to hide in. You hop into the space and leave the thieves flabbergasted as to how you have escaped.")
                print("The police have arrived and the thieves are captured. You survive.\n***YOU WIN***")
            else:
                print("This brick turns on a hidden speaker system in the bathroom that plays jazz music. The thieves enter and dance on your body. \n***GAME OVER***")