# [ ] create, call and test fishstore() function
# then PASTE THIS CODE into edX
def fishstore(fish_name, fish_price):
    return fish_name + ' costs $' + fish_price + '.'

user_fish = input('What fish do you want to sell? ')
user_price = input('Set your price [no symbols please]: ')
print(fishstore(user_fish, user_price))