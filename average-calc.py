#average calculator, calculates the average of a given array
num_list = []
num_sum = 0
num_avg = 0

while True:

    num_get = input('Enter a number or "e" to end.')
    if num_get.isdigit():
        num_list.append(int(num_get))
    elif num_get.lower() == 'e':
        for i in range(0,len(num_list)):
            num_sum = num_sum + num_list[i]
            num_avg = num_sum/len(num_list)
        break
    else:
        print('Not a number, try again.')
print('The average of the array is ' + str(num_avg))