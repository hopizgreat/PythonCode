# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix

#quoatation was missing
print("Welcome to the Debugging Lab!")

name = input("Enter your name: ")
print("Hello " + name + "!" + " Let's calculate your test scores.")
#removed the quoatation on one of the numbers
scores = [85, 90, 78, 88, 92]

total = 0
#semicolon was missing
for score in scores:
    total = total + score

average = total / len(scores)
print("Your average score is:", average)

highest = 0
for s in scores:
    if s > highest:
        highest = s
#can't contantenate str with numbers with +, so I used f
print(f"Your highest score was: {highest}")