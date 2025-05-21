# Greeting Program
# This program asks the user for their first and last name, then greets them.

# Get user's first name
first = input("Enter your first name: ")

# Get user's last name
last = input("Enter your last name: ")

# Check if both names are provided
if first.strip() == "" or last.strip() == "":
    print("Please enter both your first and last name.")
else:
    # Greet the user with their full name
    print(f"Hello, {first} {last}! Welcome to the Python program.")
# End of program