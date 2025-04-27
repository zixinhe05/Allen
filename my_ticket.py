import random

while True:
    # Choose a random number from the range 1 to 10
    number = random.randint(1, 10)
    
    # Print the chosen number
    print(f"Chosen number: {number}")
    
    # Compare the chosen number with 5
    if number == 5:
        print("The number is 5! Stopping...")
        break  # Stop the loop if the number is 5
