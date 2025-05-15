# 1
v_list = ["car", "scooter", "truck"]
v_list.append("bike") # append to add an element at the end of a list
print(v_list)


# 2
v_list = ["car", "scooter", "truck", "bike"]
v_list.remove("car") # remove used to remove an element from the list
print(v_list)


# 3
v_list = ["car", "scooter", "truck", "bike"]
if 'car' in v_list: # 'if' to give the condition and 'in' to check if element is in list or not 
    print("car is there in the list")
else:
    print("car is not in the list")


# 4
v_list = ["car", "scooter", "truck", "bike"]
rev_list = v_list[::-1] # rev_list - to store the reversed list and ::-1 - to reverse the string 
print(v_list) # this prints the original list
print(rev_list) # this prints the reversed list 


# 5
s_list = [5, 7, 6, 2]
sum1 = sum(s_list) # sum to add all the elements of the list and it is stored in 'sum1'
print(sum)