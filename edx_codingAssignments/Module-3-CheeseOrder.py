# [ ] create, call and test
# then PASTE THIS CODE into edX

def cheese_order(amount, price=2.15, min_cheese=.25, max_cheese=100):
    if int(amount) < .25:
        print('Your order is below the minimum amount.')
    elif int(amount) > 100:
        print('Your order exceeds our current stock.')
    else:
        final_order = round((int(amount) * price), 2)
        print(str(amount) + ' lbs costs $' + str(final_order))


order_amount = input('Enter cheese order weight (numeric value): ')

cheese_order(order_amount)