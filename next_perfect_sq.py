import math

#finds next perfect square number
#returns -1 if input is not perfect square
def find_next_perfect_sq(sq):

    first_sq = math.sqrt(sq)
    if first_sq % 1 == 0:
        next_sq = (int(first_sq)+1)**2
        return next_sq
    else:
        return -1


print(find_next_perfect_sq(121))

# alternative methods
#
#def find_next_square(sq):
#    root = sq ** 0.5
#    if root.is_integer():
#        return (root + 1)**2
#    return -1
#
#
#def find_next_square(sq):
#    x = sq**0.5
#    return -1 if x % 1 else (x+1)**2

while True:
    user_inputs_num = input('Enter a number or "q" to quit. \n>')
    if user_inputs_num.isdigit():
        print(find_next_perfect_sq(int(user_inputs_num)))
    elif user_inputs_num.lower() == 'q':
        break
    else:
        print('Invalid input')