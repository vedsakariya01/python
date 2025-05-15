# 1
set_1 = {"orange", "apple", "mango", "banana"}
set_1.add("cherry") # 'add' is used to add element in set(it adds elements on random index)
print(set_1)


# 2
set_1 = {"orange", "apple", "mango", "banana", "cherry"}
set_1.remove("banana") # 'remove' removes the specified element from the set
print(set_1)


# 3
set_1 = {"orange", "apple", "mango", "banana", "cherry"}
if "mango" in set_1: # 'if' statement is to give the condition and 'in' to check if the condition is true or not 
    print("Yes it is present")
else:
    print("It's not present")


# 4
set_1 = {"orange", "apple", "mango"}
set_2 = {"mango", "banana", "cherry"} # both the set have mango so intersection will be there
inter = set_1.intersection(set_2) # to store the result of the intersection 'inter' variable is used  
                                  # instead of intersection '&' operator can also be used
print(inter)


# 5
set_1 = {"orange", "apple", "mango"}
set_2 = {"mango", "banana", "cherry"} # union is used to join both the sets (same elements of the sets will only print once)
uni = set_1.union(set_2) # to store the result of the union 'uni' variable is used  
                         # instead of union '|' operator can also be used
print(uni)