#inserting, it means that we iterate through each element in 
#list (in worst-case sceanrio), linear operation as shown below
#in inserting there is also resizing of the list allocation memory
#but it's more expensive as it must go through each element again
 
list_of = [1,2,3,4,5,6,7,8]
list_of.insert(9,2)
print(list_of) 
 

 
#append, it appends item at the end of the list, we can say that
#it is a constant time operation so it's more efficient
 
list_of.append(5)
print(list_of)
 
#we can have a list of 0 elements, after adding 1 element size,
#of the list dont change. After adding another it will increase its
#size to 4,8,16,25,35,46... so it don't need to do it everytime
#this is called list resize
 
 
#extend, ability to insert a list into another list, extend
#make a series of appends to a new list until it append all
 
list_of2 = [5,6]
list_of.extend(list_of2)
print(list_of)
 
