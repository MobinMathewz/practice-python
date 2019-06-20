s = "Python is an awesome language!"

#Length of the string
print("Length of s = %d" % len(s))

#first occurance of "a"
print("The first occurance of the letter a = %d" % s.index("a"))

#number of a's
print("a  occurs %d times" % s.count("a"))

#slicings the strings into bits
#start to 5
print("The first  five characters are '%s'" % s[:5])

#5 to 10
print ("The next five characters are '%s'" % s[5:10])

#just character s
print("The 8th character is '%s'" % s[8])

print("The characters with odd index are '%s'" % s[1::2]) #(0-based indexing)

#5th-from-last to end
print("The last five characters are '%s'" % s[-5:])

#convert everything to uppercase
print("String in uppercase: '%s'" % s.upper())

#convert everything to lowercase
print("String in lowercase: '%s'" % s.lower())

#check how a string starts
if s.startswith("Python"):
    print("String starts with 'Python'. Good!")

#check how string ends
if s.endswith("age!"):
    print("String ends with 'age!'. Good!")

#split the string into separate strings
#each containing only a word
print("Split the words of the string: %s" % s.split(" "))