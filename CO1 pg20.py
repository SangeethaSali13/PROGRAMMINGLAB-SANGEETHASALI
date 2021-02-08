list = [1,4,7,8,9]
print( "Original list:",list)

for i  in list:
    if(i%2 == 0):
         list.remove(i)
print("list after removing Even numbers:",list)