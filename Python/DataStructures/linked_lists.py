#In linked list every object is contained in a separated object called
#node, node store 2 informations (individual item of the data and 
# reference to the next node)

#first node is head, last is tail (doesnt point to anything, thats
# how we know it's the end of the list)

#singly linked list - stores info about the next node only
#doubly linked list - stores info about the previous and next node

class Node: 
    data = None
    next_node = None