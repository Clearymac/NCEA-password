import pyperclip
import random
import csv

# All characters that can be used in the password
NUMS = "1234567890"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
SPECIAL = """!@#$%^&*()_-+={[}]|\:;"'?/>.<,~`"""

fnl_password = []
pass_min = []
pass_max = []

#funcion that stores the code for generating "regular" password
def regular():
    password = []
    # generate password size
    char_amount = random.randint(pass_min, pass_max)
    print("char_amount = {}".format(char_amount))
    # for loop uses generated length and generates each letter
    for length in range(char_amount):
        # to randomly decide which list to get a character from
        chse_list = random.randint(1, 4)

        # randomly gets char from specific list that was randomly chosen
        if chse_list == 1:
            ran_char = random.randint(0, 9)
            character = NUMS[ran_char]
        elif chse_list == 2:
            ran_char = random.randint(0, 25)
            character = UPPER[ran_char]
        elif chse_list == 3:
            ran_char = random.randint(0, 25)
            character = LOWER[ran_char]
        elif chse_list == 4:
            ran_char = random.randint(0, 31)
            character = SPECIAL[ran_char]

            # variable for temporarily storing the random char before adding it to "fnl_password"
        password.append(character)
        # lets program use 'fnl_password' outside func
        global fnl_password
        fnl_password = ''.join(str(e) for e in password)
    print(fnl_password)




def numbers():
    password = []
    # generate password size
    char_amount = random.randint(pass_min, pass_max)
    print("char_amount = {}".format(char_amount))
    # for loop uses generated length and generates each letter
    for length in range(char_amount):
        ran_char = random.randint(0, 9)
        character = NUMS[ran_char]

        password.append(character)
        # lets program use 'fnl_password' outside func
        global fnl_password
        fnl_password = ''.join(str(e) for e in password)
    print(fnl_password)


def letters():
    password = []
    # generate password size
    char_amount = random.randint(pass_min, pass_max)
    print("char_amount = {}".format(char_amount))
    # for loop uses generated length and generates each letter
    for length in range(char_amount):
        # to randomly decide which list to get a character from
        chse_list = random.randint(1, 2)
        if chse_list == 1:
            ran_char = random.randint(0, 25)
            character = UPPER[ran_char]
        elif chse_list == 2:
            ran_char = random.randint(0, 25)
            character = LOWER[ran_char]

            # variable for temporarily storing the random char before adding it to "fnl_password"
        password.append(character)
        # lets program use 'fnl_password' outside func
        global fnl_password
        fnl_password = ''.join(str(e) for e in password)
    print(fnl_password)


def special():
    password = []
    # generate password size
    char_amount = random.randint(pass_min, pass_max)
    print("char_amount = {}".format(char_amount))
    # for loop uses generated length and generates each letter
    for length in range(char_amount):
        ran_char = random.randint(0, 31)
        character = SPECIAL[ran_char]

        # variable for temporarily storing the random char before adding it to "fnl_password"
        password.append(character)
        # lets program use 'fnl_password' outside func
        global fnl_password
        fnl_password = ''.join(str(e) for e in password)
    print(fnl_password)


def uppercase():
    password = []
    # generate password size
    char_amount = random.randint(pass_min, pass_max)
    print("char_amount = {}".format(char_amount))
    # for loop uses generated length and generates each letter
    for length in range(char_amount):
        # to randomly decide which list to get a character from
        chse_list = random.randint(1, 3)

        # randomly gets char from specific list that was randomly chosen
        if chse_list == 1:
            ran_char = random.randint(0, 9)
            character = NUMS[ran_char]
        elif chse_list == 2:
            ran_char = random.randint(0, 25)
            character = UPPER[ran_char]
        elif chse_list == 3:
            ran_char = random.randint(0, 31)
            character = SPECIAL[ran_char]

        # variable for temporarily storing the random char before adding it to "fnl_password"
        password.append(character)
        # lets program use 'fnl_password' outside func
        global fnl_password
        fnl_password = ''.join(str(e) for e in password)
    print(fnl_password)


def lowercase():
    password = []
    # generate password size
    char_amount = random.randint(pass_min, pass_max)
    print("char_amount = {}".format(char_amount))
    # for loop uses generated length and generates each letter
    for length in range(char_amount):
        # to randomly decide which list to get a character from
        chse_list = random.randint(1, 3)

        # randomly gets char from specific list that was randomly chosen
        if chse_list == 1:
            ran_char = random.randint(0, 9)
            character = NUMS[ran_char]
        elif chse_list == 2:
            ran_char = random.randint(0, 25)
            character = LOWER[ran_char]
        elif chse_list == 3:
            ran_char = random.randint(0, 31)
            character = SPECIAL[ran_char]

        # variable for temporarily storing the random char before adding it to "fnl_password"
        password.append(character)
        # lets program use 'fnl_password' outside func
        global fnl_password
        fnl_password = ''.join(str(e) for e in password)
    print(fnl_password)



# info on types of passwords
regular_info = "'Regular' uses every main character on a standard US keyboard and randomly picks from any of these chars to make the password\n\n\n"
numbers_only_info = "Only uses numbers in the password and randomly chooses the numbers to be added to the password\n\n\n"
letter_only_info = "only use letter(upper and lower) in the password and randomly chooses the letter to be added to the password\n\n\n"
special_char_info = "only uses special characters on the standard US keyboard for the password... e.g. !@#$%^&*()\n\n\n"
uppercase_info = "similar to 'regular' but every letter will only be uppercase\n\n\n"
lowercase_info = "similar to 'regular' but every letter will only be uppercase\n\n\n"

# keeps requesting info in a loop till user wants to move on
info_screen = True
#intro user to the password generator and show options for type of password and possible info
print("Password Generator: \n\n\n\n\n")
while info_screen == True:

    print("""you have multiple options for the password you want generated...
    
    (1)regular ||| (2)Numbers only ||| (3) letters only ||| (4)Special Characters only ||| (5)Uppercase ||| (6)Lowercase
    For information on what these do, type the number next to the password type you would like to learn about...
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
        info_screen = False


# asks user to choose what password to generate then calls requested funtion to generate password
print("(1)regular ||| (2)Numbers only ||| (3) letters only ||| (4)Special Characters only ||| (5)Uppercase ||| (6)Lowercase (e)exit")
pass_choice = input("what password would you like to generate: ")

min_max = True
while min_max == True:
   max_high = "y"
   pass_min = int(input("minimum character amount: "))
   pass_max = int(input("maximum character amount: "))
   if pass_min < 0 or pass_min > pass_max:
       print("invalid min and max... please re-enter correctly\n\n")
   if pass_max > 30:
       max_high = input("{} is what you entered\n\nAre you sure you want to enter a max amount this high? (y)(n) : ".format(pass_max))

   if pass_min >= 0 and pass_min <= pass_max and max_high == "y":
       min_max = False




if pass_choice == "1":
    regular()
if pass_choice == "2":
    numbers()
if pass_choice == "3":
    letters()
if pass_choice == "4":
    special()
if pass_choice == "5":
    uppercase()
if pass_choice == "6":
    lowercase()
if pass_choice == "e":
    exit()

# asks user if they would like to save along with inputs for extra info to save
save = input("Would you like to save your password to a seperate CSV file (1)yes (2)no: ")
if save == "1":
    use = input("What is the password for? ")
    email = input("What is the attached email")


    # opens csv file and writes a new line for every request to save a password and extra information
    with open('Password_test.csv', 'a', newline='') as password_csv:
        csv_writer = csv.writer(password_csv, delimiter='\t')
        # saves use, email and password in row
        csv_writer.writerow(["Account: ", use, "Email: ", email, "Password: ", fnl_password])

elif save == "2":
    1
# copies password to PC clip board
pyperclip.copy(fnl_password)
print("The password has been copied to clipboard")