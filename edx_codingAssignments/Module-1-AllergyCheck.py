# Create Allergy check code
# then PASTE THIS CODE into edX

# [ ] get input for input_test variable


# [ ] print "True" message if "dairy" is in the input or False message if not


# [ ] print True message if "nuts" is in the input or False if not


# [ ] Challenge: Check if "seafood" is in the input - print message


# [ ] Challenge: Check if "chocolate" is in the input - print message

input_test = input("Enter some things you have eaten in the last 24 hrs: ")
print(input_test,'contains dairy is','dairy'.lower() in input_test.lower())
print(input_test,'contains nuts is','nuts'.lower() in input_test.lower())
print(input_test,'contains seafood is','seafood'.lower() in input_test.lower())
print(input_test,'contains chocolate is','chocolate'.lower() in input_test.lower())