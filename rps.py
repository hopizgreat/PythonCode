import random
def generate_random():
    compu = random.randint(1, 3)
    if compu == 1:
        compu_lett = "r"
    elif compu == 2:
        compu_lett = "p"
    else:
        compu_lett = "s"
    return compu_lett

#main code starts here
player_1 = str(input("enter r (rock), p (paper), or s (scissor) to play:"))

while player_1 == "r" or player_1 == "p" or player_1 == "s":
    compu_lett = generate_random()
    if player_1 == "r" and compu_lett == "s" or player_1 == "p" and compu_lett == "r" or player_1 == "s" and compu_lett == "p":
        print ("player_1 wins")
    elif player_1 == compu_lett:
        print("it's a draw")
    else:
        print ("computer wins")
    player_1 = str(input("enter r (rock), p (paper), or s (scissor) to play:"))
else:
    print ("Game over!")
generate_random()