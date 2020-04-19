# [ ] create, call and test the adding_report() function
# then PASTE THIS CODE into edX


def adding_report(report='T'):
    total = 0
    items = ''
    while True:
        ask = input('Enter an integer or "Q" to quit.')
        if ask.isdigit():
            total = total + int(ask)
            if report == 'A':
                items = items + ask + '\n'
        elif ask.upper().startswith('Q'):
            if report == 'A':
                print('Items\n' + items)
                print('Total\n' + str(total))
                break
            elif report == 'T':
                print('Total\n' + str(total))
                break
        else:
            print('Invalid input.')


while True:
    report_type = input('Enter "A" to list all items with total or "T" to print just the total.')
    if report_type.upper().startswith('A'):
        report_type = 'A'
        break
    elif report_type.upper().startswith('T'):
        report_type = 'T'
        break
    else:
        print('Invalid input.')

adding_report(report_type)