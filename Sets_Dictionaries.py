#SETS

#they provide us with the uniqe values, notice {}
grades = [4,2,3,4,5,6,1,2,3,4,6,4,3,2,1,2,5,3]
grades_marka = [1,2,2,1,2,3,1,2,3,4,1]
grades_arka = [4,5,6,5,4,1,3,4,5,6,6,6,5,4]

#this will provide us with the uniqe grades of both of them
marek_set = set(grades_marka)
arek_set = set(grades_arka)
print(marek_set)
print(arek_set)

print("Difference: ", marek_set - arek_set) #difference
print("Intersection: ", marek_set & arek_set) #intersection
#below we can specify the grades that marek dont have (5,6)
print(arek_set.difference(marek_set)) 
#and the other way around (2)
print(marek_set.difference(arek_set))

#set command is similar to list, we can add()/discard() etc.
grades_markaA = set(grades_marka)
grades_markaA.add(5)
print("To jest set Marka:", grades_markaA)

#we can change sets to lists, notice []
grades = list(set(grades))
print(grades)


#DICTIONARIES


dictionary = {}
dictionary["mariusz"] = [1,2,3,4,5,6,1,2,3]
dictionary["bartek"] = [1,3,4,2,1,5,2,3,2]
print(dictionary)

#here we list only the keys
for k in dictionary: 
    print(k, end= " ")
    print()

#here we list keys + values
for k,v in dictionary.items():
    print(f"{k} ma oceny: {v}") #diff way to show it

#here we list only values
for v in dictionary.values():
    print(v, end=" ")
    print()
