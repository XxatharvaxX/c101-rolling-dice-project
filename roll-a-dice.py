import random

response = "y"

while response=="y":
    number = random.randint(1,6)
    if(number==1):
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        response = input("Enter y to roll the dice or n to exit: ")
    elif(number==2):
        print("[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")
        response = input("Enter y to roll the dice or n to exit: ")
    elif(number==3):
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        response = input("Enter y to roll the dice or n to exit: ")
    elif(number==4):
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter y to roll the dice or n to exit: ")
    elif(number==5):
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter y to roll the dice or n to exit: ")
    elif(number==6):
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
        response = input("Enter y to roll the dice or n to exit: ")

if response == "n":
    input("\n\nPress enter to exit")