# [ ] create, call and test the str_analysis() function
# then PASTE THIS CODE into edX
def string_analysis(a_string):
    if a_string.isdigit():
        if int(a_string) >= 99:
            print(a_string + ' is a pretty big number.')
        elif int(a_string) < 99:
            print(a_string + ' is a rather small number.')
    elif a_string.isalpha():
        print('"' + a_string + '"' + ' is all alphabetical characters.')
    else:
        print('"' + a_string + '"' + ' is neither all digits or all alphabetical characters.')


user_in = ''

while user_in == '':
    user_in = input('Enter a word or an integer.')

string_analysis(user_in)
