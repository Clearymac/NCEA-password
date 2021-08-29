import pyperclip
import random
import csv

# info on types of passwords
regular_info = "'Regular' uses every main character on a standard US keyboard and randomly picks from any of these chars to make the password\n\n\n"
numbers_only_info = "Only uses numbers in the password and randomly chooses the numbers to be added to the password\n\n\n"
letter_only_info = "only use letter(upper and lower) in the password and randomly chooses the letter to be added to the password\n\n\n"
special_char_info = "only uses special characters on the standard US keyboard for the password... e.g. !@#$%^&*()\n\n\n"
uppercase_info = "similar to 'regular' but every letter will only be uppercase\n\n\n"
lowercase_info = "similar to 'regular' but every letter will only be uppercase\n\n\n"


bruh = True
#intro user to the password generator and show options for type of password and possible info
print("Password Generator: \n\n\n\n\n")
while bruh == True:

    print("""you have multiple options for the password you want generated...
    (1)regular ||| (2)Numbers only ||| (3) letters only ||| (4)Special Characters only ||| (5)Uppercase ||| (6)Lowercase
    For information on what these do type the number next to the password type you would like to learn about...
    if wanting to continue press 'e' """)
    # input for if user would like to learn about what a specific password type does
    pswrd_info = input("...")

    # displays password type info on user request
    if pswrd_info == "1":
        print(regular_info)
    elif pswrd_info ==  "2":
        print(numbers_only_info)
    elif pswrd_info == "3":
        print(letter_only_info)
    elif pswrd_info == "4":
        print(special_char_info)
    elif pswrd_info == "5":
        print(uppercase_info)
    elif pswrd_info == "6":
        print(lowercase_info)
    elif pswrd_info == "e":
        print("...")
        bruh = False