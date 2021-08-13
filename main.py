py -m pip install "SomeProject"
import random
import csv
import pyperclip as pc

password = ""

use = input("What is the password for? ")
email = input("What email is attached? ")
extra = input("is there any more info to add? ")

# Character list
CHAR_LIST = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};:',<.>|`~"""

#generate password size
char_amount = random.randint(8, 20)
print("char_amount = ", char_amount)


#letter variables (make this ugly shi better)
bruh1 = ""
bruh2 = ""
bruh3 = ""
bruh4 = ""
bruh5 = ""
bruh6 = ""
bruh7 = ""
bruh8 = ""
bruh9 = ""
bruh10 = ""
bruh11 = ""
bruh12 = ""
bruh13 = ""
bruh14 = ""
bruh15 = ""
bruh16 = ""
bruh17 = ""
bruh18 = ""
bruh19 = ""
bruh20 = ""
bruh21 = ""

#for loop uses generated length and generates each letter
for length in range(char_amount):

    #generates random number for getting character
    ran_char = random.randint(0,89)

#var for temporarily storing random char from char list before being stored in individual vars
    bruh = CHAR_LIST[ran_char]
    
    if length == 0:
        bruh1 = (bruh)

    elif length == 1:
        bruh2 = (bruh)

    elif length == 2:
        bruh3 = (bruh)

    elif length == 3:
        bruh4 = (bruh)

    elif length == 4:
        bruh5 = (bruh)

    elif length == 5:
        bruh6 = (bruh)

    elif length == 6:
        bruh7 = (bruh)

    elif length == 7:
        bruh8 = (bruh)

    elif length == 8:
        bruh9 = (bruh)

    elif length == 9:
        bruh10 = (bruh)
        
    elif length == 10:
        bruh11 = (bruh)
        
    elif length == 11:
        bruh12 = (bruh)
        
    elif length == 12:
        bruh13 = (bruh)
        
    elif length == 13:
        bruh14 = (bruh)

    elif length == 14:
        bruh15 = (bruh)

    elif length == 15:
        bruh16 == (bruh)

    elif length == 16:
        bruh17 == (bruh)

    elif length == 17:
        bruh18 == (bruh)

    elif length == 18:
        bruh19 = (bruh)

    elif length == 19:
        bruh20 = (bruh)

    elif length == 20:
        bruh21 == (bruh)

password = (bruh1 + bruh2 + bruh3 + bruh4 + bruh5 + bruh6 + bruh7 + bruh8 + bruh9 + bruh10 + bruh11 + bruh12 + bruh13 + bruh14 + bruh15 + bruh16 + bruh17 + bruh18 + bruh19 + bruh20 + bruh21)
print(password)


with open('Password_sheet.csv', 'a', newline='') as password_csv:
    csv_writer = csv.writer(password_csv, delimiter='\t')

    csv_writer.writerow(["Account: " , use, "Email: ", email, "Password: " , password])

pc.copy(password)
