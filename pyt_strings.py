# 1
st = ("Hello how are you") # string
a = len(st)  # only len() will give the length of string according to letters and spaces
b = len(st.split()) # len() with split() will give string length according to words and no spaces
print(a)
print(b)


# 2
st_1 = ("Hello!")
st_2 = ("my name is Ved")
st_3 = st_1 + "_" + st_2 # '+' operator is used to concatenate two strings
                         # " " is used to give space between the contents of two strings. ("-", "_")- can also be used as per requirement
print(st_3)


# 3
st = ("HELLO HOW ARE YOU?")
print(st[:1]) # first occurance


# 4
st = ("HELLO HOW ARE YOU?") # uppercase string
print(st.lower()) # print lowercase converted string by 'lower()'


# 5
st = ("wow") 
rev_st = st[::-1] # comparing a reversed string with the original string
if st == rev_st: # giving condition to check if both the strings are equal or not
    print("String is a Palindrom") # according to the condition satisfaction print statement is executed
else:
    print("String is not a palindrom")
