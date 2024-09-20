#This is a simple Python-based password generator that creates a randomized, secure password based on user preferences. Users can specify the number of letters, symbols, and numbers in the password, and the program will generate a random combination of these characters.

## Features

- Customizable password length: Choose how many letters, symbols, and numbers you want in your password.
- Randomly generated: Uses Python's `random.choice()` to ensure randomization of characters.
- Easy to use: Prompts guide users through the password generation process.

## How It Works

1. The program will ask the user for the number of letters, symbols, and numbers to include in the password.
2. It will then randomly select letters, numbers, and symbols from predefined lists.
3. The final password is a combination of all these randomly chosen characters, shuffled for additional security.
4. The generated password is then displayed on the screen.

### Example Usage

```bash
Welcome to the PyPassword Generator!
How many letters would you like in your password?
10
How many symbols would you like?
4
How many numbers would you like?
3

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for letter in range(1, nr_letters +1):
 password += random.choice(letters)

for number in range(1, nr_numbers +1):
  password += random.choice(numbers)

for symbol in range(1, nr_symbols +1):
  password += random.choice(symbols)

print(password)
random.shuffle(password)
print(password)

password_final = ""
for char in password:
  password_final += char



print(f"Your password is = {password_final}")
