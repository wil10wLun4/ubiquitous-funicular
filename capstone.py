# make the function
def fizzbuzz():
    # make the range
    for x in range(1, 101):
        # check if x is devisable by 3 and 5
        if x % 3 == 0 and x % 5 == 0:
            # print out fizzbuzz
            print("fizzbuzz")
        # see if x is devisable by 3 but not 5
        elif x % 3 == 0 and x % 5 != 0:
            # print out fizz
            print("fizz")
        # see if x is devisable by 5 but not 3
        elif x % 3 != 0 and x % 5 == 0:
            # print out buzz
            print("buzz")
        # if not that
        else:
            # print the number
            print(x)
# empty line for it looking nice

# call the function
fizzbuzz()
# empty line at the end
