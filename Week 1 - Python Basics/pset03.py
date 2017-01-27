# Problem 3

# (15/15 points)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if
# s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we
# suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and
# cleared your head.

# Paste your code into this box 
s = "azcbobobegghakl"

# Initialize theMatch to hold first character of s
bestMatch = s[0]

# Initialize testString to first character of s
testString = s[0]

# We are going to start at s[1] since we
# initialized value of testString to s[0]
for i in range (1, len(s)):
    # print "s[i]: " + s[i]
    # print "bestMatch: " + bestMatch
    if s[i] >= s[i-1]:
        testString = testString + s[i]       
    else:
        testString = s[i]
    if len(testString) > len(bestMatch):
        # if true, set bestMatch to value of testString
        bestMatch = testString
               
print ("Longest substring in alphabetical order is: " + bestMatch)


