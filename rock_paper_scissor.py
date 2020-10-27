import random

while True:
    comp_lists = ['Rock', 'Paper', 'Scissor']
    user = input("WELCOME, please choose an option:").capitalize()
    if user in comp_lists:
        pass
    else:
        print("wrong input")
        continue
    comp = random.choice(comp_lists)


    print(f"you choose {user}")
    print(f"computer choose {comp} \n")

    if user == "Rock" and comp == "Scissor":
        print("YOU WIN")
    elif user == "Rock" and comp == "Paper":
        print("COMPUTER WINS")
    elif user == "Rock" and comp == "Rock":
        print("IT\'S A DRAW")
        
    if user == "Paper" and comp == "Rock":
        print("YOU WIN")
    elif user == "Paper" and comp == "Scissor":
        print("COMPUTER WINS")
    elif user == "Paper" and comp == "Paper":
        print("IT\'S A DRAW")
        
    if user == "Scissor" and comp == "Paper":
        print("YOU WIN")
    elif user == "Scissor" and comp == "Rock":
        print("COMPUTER WINS")
    elif user == "Scissor" and comp == "Scissor":
        print("IT\'S A DRAW")

    repeat = input("Do you want to continue?(Y/N)").capitalize()

    if "Y" in repeat:
        continue
    else:
        exit()
    

    
    
    
