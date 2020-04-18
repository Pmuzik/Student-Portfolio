while True:
    n = input('How many years do you want to wait? (input a number)')
    if n.isnumeric():
        savings = 1000 * 1.15 ** int(n)
        print('Your savings have mature over '+ str(n) + ' years at a rate of 15%.')
        print('You have earned $'+str(savings)+'.')
        break

    else:
        print('Error: input is not number.')
