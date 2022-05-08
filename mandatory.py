import random

print("\nThis is a prediction simulator\n")

x = "y"
toss_List=["Head","Tail"]

while x=="y":
  toss = random.randint(0, 1)
  toss_choice=random.randint(0,1)

  toss=toss_List[toss_choice]
    
  if toss == "Head":
    print("\nHead\n No Prediction\n")
    
  elif toss == "Tail":
    print("\nTail\n You will be redirected for prediction through dice number\n")

    
    print("Now the dice will be Thrown\n")
    number = random.randint(1,6)
    
    if number == 1:
      print("-------")
      print("|     |")
      print("|  X  |")
      print("|     |")
      print("-------\n")

      print("number '1'\n You Have a good day ahead\n")


    elif number == 2:
      print("-------")
      print("|X    |")
      print("|     |")
      print("|    X|")
      print("-------\n")

      print("number '2'\n Your days are going to get better\n")


    elif number == 3:
      print("-------")
      print("|X    |")
      print("|  X  |")
      print("|    X|")
      print("-------\n")

      print("number '3'\n You have got a tough day ahead\n")


    elif number == 4:
      print("-------")
      print("|X   X|")
      print("|     |")
      print("|X   X|")
      print("-------\n")

      print("number '4'\n Your luck is going to give you another opportunity\n")


    elif number == 5:
      print("-------")
      print("|X   X|")
      print("|  X  |")
      print("|X   X|")
      print("-------\n")

      print("number '5'\n You are going to have a worst day this week\n")


    elif number == 6:
      print("-------")
      print("|X   X|")
      print("|X   X|")
      print("|X   X|")
      print("-------\n")

      print("number '6'\n You have got a good day ahead\n")


  x = input("Press 'y' to run the simulator again: ")
