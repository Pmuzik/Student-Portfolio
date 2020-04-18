#formula for calculating the standard deviation of a given set of numbers
'''
collect data points from the user
store data in a list (values)
find mean (m)
    find sum of the list and divide by number of values in list
find variance (v)
    for each value in list subtract m and then square
    add each squared value to a new list (sq_values)
    find sum of items in sq_values and then dived by number of items in list
find standard deviation (d)
    square root of v v**(1/2)
'''

#Step 1 - collect they array as a list
#There is probably an easier and more efficient way to do this,
# i.e. input all the values at once and sort into a list
def collect_data():
    data_set = []
    while True:
        user_in = input('[A]dd value, [C]ontinue, or [E]xit\n>')
        if user_in.lower() == 'a':
            a_value = input('Enter a number.\n>')
            data_set.append(int(a_value))

        elif user_in.lower() == 'c':
            return data_set
            break

        elif user_in == 'e':
            exit()

#Step 2 - find the arithmetic mean of the array
#simply add up and divide by length of the array
def find_mean(array):
    total = 0
    for i in array:
        total = total + i
    return total/len(array)

#Step 3 - use the mean to find the variance of the array
#For each value subtract the mean and square the result and then add up each squared value
#then divide by length of the array
def variance(mean, array):
    sq_total = 0
    for i in array:
        sq_total = sq_total + (i - mean)**2
    return sq_total/len(array)

#Step 4 find the square root of the variance to find the standard deviation
def std_deviation(variance):
    return variance**(1/2)

#program starts here
while True:
    d = collect_data()
    m = find_mean(d)
    v = variance(m, d)
    print('The standard deviation of ' + str(d) + ' is ' + str(std_deviation(v)))
