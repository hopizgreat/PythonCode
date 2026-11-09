import time

# Function: countdown
# Purpose: Count down from a given number of seconds to zero.
# Parameter: seconds_remaining - number of seconds to count down.
# Return: No value returned.
def countdown(seconds_remaining):
    while seconds_remaining > 0:
        print(seconds_remaining)
        seconds_remaining -= 1
        time.sleep(1)
    print("BLAST OFF!")

# Main Program
# Ask the user for the number of seconds.
print("How many seconds to count down? Enter an integer:")
seconds = input()

# Repeat until the user enters a non-negative integer.
while not seconds.isdigit():
    print("That wasn't an integer! Enter an integer:")
    seconds = input()

# Convert the input to an integer.
seconds = int(seconds)

# Call the countdown function and pass seconds as an argument.
countdown(seconds)
