# Import random function

import random
'''
# Single Dice rolls
D2Result = random.randint(1,2)
D4Result = random.randint(1,4)
D6Result = random.randint(1,6)
D8Result = random.randint(1,8)
D10Result = random.randint(1,10)
D12Result = random.randint(1,12)
D20Result = random.randint(1,20)

print ("D2 is",D2Result)
print ("D4 is",D4Result)
print ("D8 is",D8Result)
print ("D10 is",D10Result)
print ("D12 is",D12Result)
print ("D20 is",D20Result)

 Multiple dice roll#s - no choice

print ("Now for multiple dice!")

numofdice = input("How many dice would you like to roll? ")

D20ResultMulti = []

for i in range(int(numofdice)):
    D20ResultMulti.append(random.randint(1,20))

print (D20ResultMulti)
'''

# Multiple dice rolls - choice of dice

dicetype = input("What type of dice would you like to roll, D2, D4, D6, D8, D10, D12, D20? ")
#input validation
#dicetype - provided response
#dicetype - check valid Dice type

#dicetype - check case and convert to uppercase

dicetypemax = int(dicetype.replace('D',''))



dicenum = input("How many dice would you like to roll of type " + dicetype + "?")


#dicenum - provided response
#dicenum - check is a integer

#dicenum - check value isnt too big


# set list variable for answers

diceresults = []



match dicetype:
    case "D2":
        print("You would like to roll ",dicetype," ", dicenum, " times" )
        for i in range(int(dicenum)):
            diceresults.append(random.randint(1,dicetypemax))
    case "D4":
        print("You would like to roll ",dicetype," ", dicenum, " times" )
        for i in range(int(dicenum)):
            diceresults.append(random.randint(1,dicetypemax))        
    case "D6":
        print("You would like to roll ",dicetype," ", dicenum, " times" )
        for i in range(int(dicenum)):
            diceresults.append(random.randint(1,dicetypemax))
    case "D8":
        print("You would like to roll ",dicetype," ", dicenum, " times" )
        for i in range(int(dicenum)):
            diceresults.append(random.randint(1,dicetypemax))
    case "D10":
        print("You would like to roll ",dicetype," ", dicenum, " times" )
        for i in range(int(dicenum)):
            diceresults.append(random.randint(1,dicetypemax))
    case "D12":
        print("You would like to roll ",dicetype," ", dicenum, " times" )
        for i in range(int(dicenum)):
            diceresults.append(random.randint(1,dicetypemax))
    case "D20":
        print("You would like to roll ",dicetype," ", dicenum, " times" )
        for i in range(int(dicenum)):
            diceresults.append(random.randint(1,dicetypemax))

print (diceresults)



