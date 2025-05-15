# 1
dic = {"fname" : "ved", "lname" : "sakariya"} 
dic["mname"] = "D" # adds the given key-value in dictionaries
print(dic)


# 2
dic = {"fname": "ved", "mname": "D", "lname": "sakariya"}
dic.pop("lname") # removes the specified key-value
dic.popitem() # removes the last element
print(dic)


# 3
dic = {"fname": "ved", "mname": "D", "lname": "sakariya"}
if "mname" in dic: # searches for the specified key with the help of if statement
    print("Key is present")
else:
    print("Key is not present")


# 4
dic = {"fname": "ved", "mname": "D", "lname": "sakariya"}
a = dic.get("fname") # gives the value of specified key
print(a)


# 5
dic = {"fname": "ved", "mname": "D", "lname": "sakariya"}
a = dic.keys() # returns all the keys
print(a)