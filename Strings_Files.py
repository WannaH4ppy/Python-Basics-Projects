#STRINGS


#Strings are case-sensitive
name = "Bartek"
print(name[1]) #prints second letter
print(name)
print(len(name)) #checks the length

#we include left side [2:...] and exclude right side [...:3]
#to calculate amount of letters we substract right from left 3 - 2 = 1 letter
print(name[-2]) #output 2 letter from the right -1,-2 [k,e]
print(name[:2]) #output string to it's 2 letters 0,1 [B,a]
print(name[1:-1]) #skips 1 and last letter from string skips [0] B & [5] k
print(name.lower())
print(name.upper())

#to clean a string with spaces at the end and beginning
dirty_string = "        to    many spacessss    " #
clean_string = dirty_string.strip()
print(clean_string)

name = name.replace("B","A") #replaces B with the A
print(name)

print("------------------------------------------------------------------")

if "B" in name:
    print("yes")

print("------------------------------------------------------------------")

test_string = "Bartek ma kota i elo"
if test_string.startswith("Bartek"):
    print("JD")
    
print("------------------------------------------------------------------")

if test_string.endswith("elo"):
    print("yes also")

print("------------------------------------------------------------------")

new_string = name + " " + test_string
print(new_string)

#fstring are very powerful tool, allows to insert
fstring = f"{name} is the best RA and: {test_string}"
print(fstring)

#split also is very powerful tool
sentence = "Bartek ma kota i elo"
amount_of_words = sentence.split()
print(amount_of_words)

print("------------------------------------------------------------------")

#FILES 

lines = [] #first we need to create an empty list, before we can append to it

#with is a Contex Manager, prevents from errors
with open("tekst.txt", encoding="UTF-8") as f:  #encoding (for polish letter)
    for line in f: #loads file line by line at the same time
        lines.append(line.strip()) #removes \n and spaces from the edges
    print(lines)
    
    
#mode w, write mode, it creates new file! It will overwirite existing one
with open("moje_notatki.txt", mode="w", encoding="UTF-8") as f:
    f.write("Zapisuję pierwszą linijkę!\n")
    f.write("A tu leci druga linijka.\n")


#mode a, creates new file OR allow to append at the end
with open("moje_notatki.txt", mode="a", encoding="UTF-8") as f:
    f.write("Zapisuję pierwszą linijkę!\n") 
    f.write("A tu leci druga linijka.\n")
    
print("------------------------------------------------------------------")

#in f.read() and f.readlines() we dont need an empty list like in caly_teskt[]
#mode r, is for read-only, it will output error if file dont exist

#takes whole file and saves as one
with open("moje_notatki.txt", mode="r", encoding="UTF-8") as f:
    caly_tekst = f.read()
    print(caly_tekst)
    
#takes whole file and outputs it as ready list
with open("moje_notatki.txt", mode="r", encoding="UTF-8") as f:
    caly_tekst = f.readlines()
    print(caly_tekst)
    

