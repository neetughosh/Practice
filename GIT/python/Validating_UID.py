# Enter your code here. Read input from STDIN. Print output to STDOUT

# ABCXYZ company has up to  100 employees. 
# The company decides to create a unique identification number (UID) for each of its employees. 
# The company has assigned you the task of validating all the randomly generated UIDs.

# A valid UID must follow the rules below:

# It must contain at least  uppercase English alphabet characters.
# It must contain at least  digits ( 0-9 ).
# It should only contain alphanumeric characters ( a-z ,  A-Z  &  0-9 ).
# No character should repeat.
# There must be exactly  characters in a valid UID.
# Input Format

# The first line contains an integer , the number of test cases. 
# The next  lines contains an employee's UID.

# Output Format

# For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

# Sample Input

# 2
# B1CD102354
# B1CDEF2354
# Sample Output

# Invalid
# Valid


import re
n= int(input())

for i in range(n):
    
    status = "Valid"
    input_set = input()
    
    if not(len(set(re.findall("[a-z|A-Z|0-9]", input_set))) == 10 and len(re.findall("[A-Z]", input_set)) >= 2 and len(re.findall("[0-9]", input_set)) >= 3):
        status = "Invalid"
    print(status)  
    