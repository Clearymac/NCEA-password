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


for length in range(char_amount):

    #generates random number for getting character
    ran_char = random.randint(0,89)

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

password = (bruh1 + bruh2 + bruh3 + bruh4 + bruh5)
print(password)
