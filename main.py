import random

password = ""

# Character list
CHAR_LIST = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};:',<.>|`~"""

#password size
char_amount = random.randint(8, 20)

bruh1 = ""
bruh2 = ""
bruh3 = ""
bruh4 = ""
bruh5 = ""

for length in range(char_amount):

    #generates random number for getting character
    ran_char = random.randint(0,89)

    bruh = CHAR_LIST[ran_char]
    if length == 0:
        bruh1 = (bruh)

    elif length == 1:
        bruh2 = (bruh)

    if length == 2:
        bruh3 = (bruh)

    elif length == 3:
        bruh4 = (bruh)

    elif length == 4:
        bruh5 = (bruh)

password = (bruh1 + bruh2 + bruh3 + bruh4 + bruh5)
print(password)
