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


