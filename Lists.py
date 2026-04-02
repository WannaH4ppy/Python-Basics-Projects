#LISTS

#old
grades = [2,3,4,5,33,21,5,3,2,3,5,6]
for i in range(len(grades)): print("Ocena to: ", grades[i]) #each time we call a position in list so function need to
                                                            #go to the list, search for position, take value and output it
                                                            #number on locker in other words
print("------------------------------------------------------------------")
#new
grades = [2,3,4,5,33,21,5,3,2,3,5,6]
for i in grades: print("Ocena to: ", i) #here function call directly to content of "locker" and outputs it
                                        #this is better as we are only interested in data, not the position of data
print("------------------------------------------------------------------")
#enumerate()          
grades = [2,3,4,5,33,21,5,3,2,3,5,6]                                #this way we can eat & have a cookie, i acts in old way iterating through
for i, ocena in enumerate(grades): print(i, "ocena to: ", ocena)    #grades and list position, while ocena gives the content of "locker"

print("------------------------------------------------------------------")
#incrementing values in list:

for i in grades:        #this won't increment any element in list
    i+=1                #as we dont refer to the content of "storage"
print(grades)           #we just temporarly change the value
    
#proper way of incrementing 
for i, x in enumerate(grades):      #here x is just a temporary object which dont do nothing in this case
    grades[i] += 1                  #because we refer only to position of "locker" and add +1 to it
print(grades)

print("------------------------------------------------------------------")

#lists additional functions:

grades.append(5) #appends at the end 5
grades.extend([1,2,3,4,5]) #extend a list of []
grades.insert(5, 1) #inserts numer in particular position (position, object)

print(grades)

grades.remove(5) #removes first element that it will find
grades.pop() #removes last item form list 
grades.sort() #sorts from lowest to highest 
print(grades) 
grades = sorted(grades, reverse=True) #same as sort() but it has more options, like reverse
print(grades)

if 129 in grades: #now it is much simpler to search thorugh list
    print("Yup")
else:
    print("Nope")
    
print("------------------------------------------------------------------")

grades_all = [[1,2,3],[5,3,2,1,5],[2,4,6,2],[1,6,6]]

for i in grades_all:
    for j in i: 
        print(j, end=" ")
    print()
    
grades_2 = grades_all #here we only point to the same address in memory of computer
grades_2[0][0]=123 #changing first element in first array would cause change of two arrays
print(grades_2)     #grades_2 and grades_all are the same in memory!!! house address
print(grades_all)
    
from copy import deepcopy #here we import specific function  from copy
import copy #here we import whole copy module

grades_2 = deepcopy(grades_all) #here we create a new list by deepcopying
grades_2[0][0] = 252 #value here will actually change
print(grades_2)

grades_3 = grades_all.copy() #here it again would be same output only because it's not deepcopy
grades_3[0][0] = 788        #grades_3 and grades_all would output same result
print(grades_3)
print(grades_all)





