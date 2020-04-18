# a function to find the sum of multiples of 3 and 5 below a given number
# this was my solution
def solution(number):
    a_num = 0
    total = 0
    num_list = []
    while number != 0:
        number = number - 1
        a_num = number
        if a_num % 3 == 0:
            num_list.append(a_num)
        elif a_num % 5 == 0:
            num_list.append(a_num)
        else:
            pass
    for ele in range(0, len(num_list)):
        total = total + num_list[ele]
    print(total)


# total = sum(num_list)
# print (total)

# this is someone else's solution which is apparently not optimal
# def solution(number):
#    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# and this is a more mathematical solution
# def solution(n):
#    # Trapezoidal rule
#    n -= 1  # not include n

#    # calculate how many terms of 3
#    t3 = n // 3
#    a3 = 3 * (1 + t3) * t3 / 2

#    # calculate how many terms of 5
#    t5 = n // 5
#    a5 = 5 * (1 + t5) * t5 / 2

#    # calculate how many terms of 15
#    t15 = n // 15
#    a15 = 15 * (1 + t15) * t15 / 2

#    return a3 + a5 - a15

while True:
    sol = input('Enter a number.')
    if sol.lower().startswith('e'):
        break

    else:
        solution(int(sol))