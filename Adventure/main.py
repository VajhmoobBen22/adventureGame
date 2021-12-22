import random

points = 250

combat = int(input("How much combat experience do you have out of 100?\n "))

if combat > 100 or combat < 0 or combat > points:
    print("You're a cheater, you're a loser you want to play an op character, thats cringe, you're bad, learn to play the game properly literally so bad. ")
    exit()
points = points - combat
print("You have " + str(points) + " skill points remaining")

magic = int(input("How intuned are you with your gifts?\n "))

if magic > 100 or magic < 0 or magic > points:
    print("You're a cheater, you're a loser you want to play an op character, thats cringe, you're bad, learn to play the game properly literally so bad.")
    exit()
points = points - magic
print("You have " + str(points) + " skill points remaining")

stealth = int(input("How profiecient are you in the art of stealth?\n "))

if stealth > 100 or stealth < 0 or stealth > points:
    print("You're a cheater, you're a loser you want to play an op character, thats cringe, you're bad, learn to play the game properly literally so bad.")
    exit()
points = points - stealth
print("You have " + str(points) + " skill points remaining")

intelligence = int(input("How intelligent are you?\n "))

if intelligence > 100 or intelligence < 0 or intelligence > points:
    print("You're a cheater, you're a loser you want to play an op character, thats cringe, you're bad, learn to play the game properly literally so bad.")
    exit()
points = points - intelligence
print("You have " + str(points) + " skill points remaining")

instincts = int(input("How much do you trust your self?\n "))
if instincts > 100 or instincts < 0 or instincts > points:
    print("You're a cheater, you're a loser you want to play an op character, thats cringe, you're bad, learn to play the game properly literally so bad.")
    exit()
points = points - instincts
print("You have " + str(points) + " skill points remaining")



print("You are at the gate, no one appears to be guarding it what do you do?")
print("1. Attempt to punch through")
print("2. Blast it with you're gift")
print("3. Look for alternative entrance")
print("4. Try to open the gate")
choice = input(">")

if choice == "1":
    roll = random.randrange(0, combat)
    if roll > 90:
        print("The sheer power of your fist shatter through the iron gate allowing you to pull it open but the sound has alerted a nearby guard.")

    else:
        print("You do or could not muster the strength to punch through but you have alerted a nearby guard.")

elif choice == "2":
    roll = random.randrange(0, combat)
    if roll > 90:
        print("The sheer power of your fist shatter through the iron gate allowing you to pull it open but the sound has alerted a nearby guard.")

    else:
        print("You do or could not muster the strength to punch through but you have alerted a nearby guard.")

elif choice == "3":
    roll = random.randrange(0, combat)
    if roll > 90:
        print("The sheer power of your fist shatter through the iron gate allowing you to pull it open but the sound has alerted a nearby guard.")

    else:
        print("You do or could not muster the strength to punch through but you have alerted a nearby guard.")

elif choice == "4":
    roll = random.randrange(0, combat)
    if roll > 90:
        print("The sheer power of your fist shatter through the iron gate allowing you to pull it open but the sound has alerted a nearby guard.")

    else:
        print("You do or could not muster the strength to punch through but you have alerted a nearby guard.")

else: 
    print("You have failed.")