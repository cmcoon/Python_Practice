import math


# Bubble Sort, simple but not the most efficient
def bubble_sort(list):
    # First loop goes through list up to last number
    for i in range(0, len(list)-1):
        # List is succesivy sorting so go one less space each time
        for j in range(0, ((len(list)-1) - i)):
            # Swap elements if preceding term is larger
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp

    return list


# Linear Search
# Return the index of integer x in list with first index being 0, no result = -1
def linear_search(x, list):
    for i in list:
        if i == x:
            return list.index(i)

    # returns 0 if not found
    return -1


# Binary search, requires ordered list and returns index of integer x in list
def binary_search(x, list):
    i = 0
    j = len(list) - 1

    while i < j:
        m = math.floor((i + j) / 2)
        if x > list[m]:
            i = m + 1
        else:
            j = m

    if x == list[i]:
        location = i
    else:
        location = 0

    return location


# Finding max element in a finite sequence
def max_num(numlist):
    max = numlist[0]
    #For optimal efficiency would want to start for loop on numlist[1]
    for num in numlist:
        if num > max:
            max = num

    return max


# Recursive algorithm for computing nx where n is > 0 and x is an integer, using just addition
# Useless
def recursive_multiply(n, x):
    if n == 1:
        return x
    else:
        return x + recursive_multiply((n-1), x)


# Recursive algorithm to compute n^2 when n is a non-negative integer, using the fact that (n+1)^2 = n^2 + 2n + 1
# Dont really get this one
def recursive_square(n):
    if n == 0:
        return 0
    else:
        return (recursive_square((n-1)) + (2*(n-1) + 1))


# Lets look at some nested loops
def loop_nest():
    count = 0

    #for(i = 0; i < 5; i++)
    for i in range(0,5):
        for j in range(0, 6):
            count += 1
            print(i, j, count)


# Create, populate, ad return a 2D list, not as straightfoward as java
def populate2dList(matrix):
    start = 1

    #This is strange syntax
    w, h = 10, 10;
    matrix = [[0 for x in range(w)] for y in range(h)]

    for i in range(0,10):
        for j in range (0, 10):
            matrix[i][j] = start
            start += 1

    return matrix


# Euclidean algorithm for finding greatest common divisor
# Method returns and prints stuff, but dont neccesarily need to assign return value when calling
def euclidean(a, b):
    print('\nLets compute the greatest commond divisor of ' + str(a) + ' and ' + str(b) + ' using the Euclidean algorithm\n')
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a

    # Succesivly divide a by a%b until remainder is zero, this quotient is gcd
    while y != 0:
        #String formatting syntax "{: flags ie .2f}".format(NUMBER)
        if (x % y) != 0:
            print(str(x) + ' = ' + str(y) + ' * ' + str(math.floor(x / y)) + ' + ' + str(x % y))
        else:
            print(str(x) + ' = ' + str(y) + ' * ' + str(math.floor(x / y)))

        r = x % y
        x = y
        y = r

    print('\nGreatest common divisor of ' + str(a) + ' and ' + str(b) + ' is ' + str(x) + ' as there is no remainder left')

    return x


# Euclidean algorithm solved recursively
# Makes outputting data difficult so just do that outside function
def euclidean_recursive(a, b):
    #print('\nLets compute the greates commond divisor of ' + str(a) + ' and ' + str(b) + ' using the Euclidean algorithm\n')
    if a < b:
        x = a
        y = b
    else:
        x = b
        y = a

    if x == 0:
        return y
    else:
        # floor function works better math.floor and math.ceiling are part of math library
        print(str(y) + ' = ' + str(x) + ' * ' + str(math.floor(y / x)) + ' + ' + str(y % x))
        return euclidean_recursive(y % x, x)
        #print('\nGreatest common divisor of ' + str(a) + ' and ' + str(b) + ' is ' + str(x) + ' as there is no remainder left')


# Use bubble_sort to sort unordered list min to max
list_sort = [3, 2, 4, 1, 5]
print('\nUnsorted List = ' + str(list_sort))
list_sort = bubble_sort(list_sort)
print('Sorted List = ' + str(list_sort) + '\n')

# Search an unordered list  for a number, print index, using linear_search
# No such element returns -1
list_search = [1, 55, 76, 3, 77, 6, 23, 66, 90, 0, 2, 43]
print('Search this unordered list: ' + str(list_search))
print('Number 4 not in list index = ' + str(linear_search(4, list_search)))
print('Index of number 76 searched in list = ' + str(linear_search(76, list_search)) + '\n')

# Search an ordered list using binary_search, return index of element
list_ordered = [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16, 18, 19, 20, 22]
print('Ordered list for binary search: ' + str(list_ordered))
print('Index of number 10 in list = ' + str(binary_search(10, list_ordered)) + '\n')

# Order list and then find index of num
print('Unordered list: ' + str(list_search))
print('Ordered list using bubble sort: ' + str(bubble_sort(list_search)))
print('Index of number 3 using binary search = ' + str(binary_search(3, bubble_sort(list_search))) + '\n')

# Find the max number in a list
numlistmain = [4, 6, 2, 10, 2, 4, 7, 8, 1, 10]
print('Find max in thsi list: ' + str(numlistmain))
print('Max num is: ' + str(max_num(numlistmain)) + '\n')

# 5 squared just using addition, pretty useless but recursive
print('5 squared = ' + str(recursive_square(5)))

# 3 times 5 using just addition, aso useless but also recursive
print('3 times 5 = ' + str(recursive_multiply(3, 5)) + '\n')

# No need to declare empty list, printing 2d list default is ugly
list = populate2dList(list)
print('This is default printing for a 2D array (ugly): ' + str(list))

# String formatting is just so fun, lets print out a nice 2D array(list) using a format better than default print
print('Lets try something prettier: ')
for i in range(0,10):
    print()
    for j in range(0, 10):
        if list[i][j] < 11:
            print(str(list[i][j]) + '  ', end='')
        else:
            print(str(list[i][j]) + ' ', end='')
print('\n')

# Just looking at a nested for loop
print('This just demonstrates two nested loops. Column 1 = outer loop. Column 2 = inner loop. Column 3 = total runs.\n')
loop_nest()
print()

# Demonstrate usage of Euclidean Algorithm, recursively so less word and interaction
print('Use the euclidean algorith to calculate greatest common divisor of 414 and 662 \n')
print(str(euclidean_recursive(414, 662)))

# Without recursion the Euclidean Algorithm becomes easier to interact with output, multiple test cases
euclidean(414, 662)
euclidean(662, 414)
euclidean(662, 662)
euclidean(-12, -24)
euclidean(0, 0)
