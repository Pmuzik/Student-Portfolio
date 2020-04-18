'''
text = input("Please enter a message:")
shift = int(input("How many spaces to shift?:"))
for char in text:
    print(char,ord(char),ord(char)+shift,chr(ord(char)+shift))
'''

def cipher(msg, key):
    output = ""
    for char in msg:
        output += chr(ord(char)+key)
    print(output)

text = input("Please enter a message:")
shift = int(input("How many spaces to shift?:"))

cipher(text,shift)

'''
#my current caesar cipher script
def encode(key):
    if key.isdigit():
        return int(key)
    else:
        print("Please enter only digits.")
        exit()

def cipher(msg, key):
    output = ""
    for char in msg:
        output += chr(ord(char)+key)
    print(output)

text = input("Please enter a message:")
shift = encode(input("How many spaces do you want to shift?:"))

cipher(text,shift)
'''
