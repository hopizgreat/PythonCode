import random
player_1 = str(input("enter r, p, or s to play:"))
compu = random.randint(1, 3)
if compu == 1:
    compu_lett = "r"
elif compu == 2:
    compu_lett = "p"
else:
    comp_lett = "s"
print("compu_lett")

if player_1 == "r" and compu_lett == "s" or player_1 == "p" and compu_lett == "r" or player_1 == "s" and compu_lett == "p":
    print ("player_1 wins")
elif player_1 == "s" and compu_lett == "r" or player_1 == "r" and compu_lett == "p" or player_1 == "p" and compu_lett == "s":
    print ("computer wins")
elif player_1 == compu_lett:
    print("it's a draw")
else:
    print ("error")
    