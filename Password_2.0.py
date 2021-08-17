import pyperclip
import random
import csv


password = []

use = input("What is the password for? ")
email = input("What email is attached? ")
extra = input("is there any more info to add? ")

# Character list
CHAR_LIST = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};:',<.>|`~"""

# generate password size
char_amount = random.randint(8, 20)
print("char_amount = {}".format(char_amount))


# letter variables (make this ugly shi better)

# or loop uses generated length and generates each letter
for length in range(char_amount):

    # generates random number for getting character
    ran_char = random.randint(0, 89)
    bruh = CHAR_LIST[ran_char]
# var for temporarily storing random char from char list before being stored in individual vars
    password.append(bruh)

str1 = ''.join(str(e) for e in password)

with open('Password_sheet.csv', 'a', newline='') as password_csv:
    csv_writer = csv.writer(password_csv, delimiter='\t')

    csv_writer.writerow(["Account: " , use, "Email: ", email, "Password: " , str1])
print(str1)
pyperclip.copy(str1)
