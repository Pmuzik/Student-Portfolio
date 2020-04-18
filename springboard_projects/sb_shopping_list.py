'''
This code is a review of bools, loops, adding to lists,
and the use of "for i in list print (i)"
'''
shopping_list = [] #initializes shopping_list with an empty list
while True:
    need_to_buy = input('What do you need to buy?(enter "e" to end)')
    if need_to_buy.lower() != 'e':
        shopping_list.append(need_to_buy) #adds input to list
        
    else:
        print("Here's your list:")
        for i in shopping_list: #prints each item in the list individually
            print (i) 
        break

