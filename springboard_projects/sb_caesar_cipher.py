'''''
Note
ord() returns the Unicode code point of the character--an integer.
chr() returns the character of the associated with an input integer.
'''''

#FUNCTIONS
#defines the Caesar Cipher encryption function
def cipher(msg, key):
    output = ""
    for char in msg:
        output += chr(ord(char)+key)
    print(output)
#defines decryption function
def decrypt(msg, key):
    output = ""
    for char in msg:
        output += chr(ord(char) - key)
    print(output)
#creates the menu
def menu():
    menu = input('-[e]ncrypt\n-[d]ecrypt\n-[q]uit\n>')
    #encrytion
    if menu.lower().startswith('e'):
        text = input("Please enter a message:\n>")
        shift = input("How many spaces do you want to shift?\n>")
        if shift.isdigit() == False:
            print('Please enter a digit')
            while shift.isdigit() == False:
                shift = input("How many spaces do you want to shift?\n>")
            cipher(text, int(shift))
        else:
            cipher(text, int(shift))
    #decryption
    elif menu.lower().startswith('d'):
        text = input("Please enter an encoded message:\n>")
        shift = input("Please enter the key:\n>")
        if shift.isdigit() == False:
            print('Please enter a digit')
            while shift.isdigit == False:
                shift = input("Please enter the key:\n>")
            decrypt(text,int(shift))
        else:
            decrypt(text,int(shift))
    #exit program
    elif menu.lower().startswith('q'):
        exit()
    else:
        print('Command not recognized.')



'''''
#This is where I started originally.

#main loop of the program
#collects input and makes sure the key is a number
while True:
    start = input('Execute Caesar Cipher? [y/n]\n>')
    if start.lower().startswith('y'):

        text = input("Please enter a message:\n>")
        shift = input("How many spaces do you want to shift?\n>")
        if shift.isdigit() == False:
            print('Please enter a digit')
            while shift.isdigit() == False:
                shift = input("How many spaces do you want to shift?\n>")
            cipher(text,int(shift))
        else:
            cipher(text,int(shift))

    elif start.lower().startswith('n'):
        exit()
'''''
#this is where the main program starts
while True:
    start = input('Execute Caesar Cipher? [y/n]\n>')
    if start.lower().startswith('y'):
        while True:
            menu()
    elif start.lower().startswith('n'):
        exit()
    else:
        print('Command not recognized.')