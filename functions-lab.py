# Challenges

# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
# For example:
# sum_to(6)  # returns 21
# sum_to(10) # returns 55
def sum_to(num):
    arr = range(1, num+1)
    sum = 0
    for n in arr:
        sum += n
    return sum
print(sum_to(6))
print(sum_to(10))

# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
# For example:
# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231
def largest(arr):
    largest = 0
    for num in arr:
        if num > largest:
            largest = num
    return largest
print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))  # returns 231

# Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
# For example:
# occurrences('fleep floop', 'e')   # returns 2
# occurrences('fleep floop', 'p')   # returns 2
# occurrences('fleep floop', 'ee')  # returns 1
# occurrences('fleep floop', 'fe')  # returns 0
def occurrences(str1, str2):
    count = 0
    while str2 in str1:
        count += 1
        idx = str1.index(str2)
        str1 = str1[idx+len(str2):]
    return count
print(occurrences('fleep floop', 'e'))
print(occurrences('fleep floop', 'p'))
print(occurrences('fleep floop', 'ee'))
print(occurrences('fleep floop', 'fe'))

# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).
# For example:
# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0
def product(*args):
    sum = 1
    for arg in args:
        sum *= arg
    return sum
print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))

# Bonus Challenge

# Write a function named steps_to_zero that accepts a non-negative integer as an argument, and returns the number of steps it took to reduce the integer to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
# For example:
# steps_to_zero(14) # returns 6
# Explanation:

# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.

def steps_to_zero(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
            steps += 1
        else:
            num -= 1
            steps += 1
    return steps
print(steps_to_zero(14))