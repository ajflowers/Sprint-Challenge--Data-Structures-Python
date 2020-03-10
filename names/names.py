import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# class NameSearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         if value < self.value:
#             if self.left:
#                 self.left.insert(value)
#             else:
#                 self.left = NameSearchTree(value)                
#         else:
#             if self.right:
#                 self.right.insert(value)    
#             else:
#                 self.right = NameSearchTree(value)
                
                    
#     def contains(self, value):
#         if value == self.value:
#             return True
#         elif value < self.value and self.left:
#             return self.left.contains(value)
#         elif value > self.value and self.right:
#             return self.right.contains(value)
#         else:
#             return False


# name_tree = NameSearchTree("names to search")

# for name_1 in names_1:
#     name_tree.insert(name_1)

# for name_2 in names_2:
#     if name_tree.contains(name_2):
#         duplicates.append(name_2)



##### STRETCH #####
# 
# NAMES IN ARRAYS ONLY

# class NodeSearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         if names_1[value] < names_1[self.value]:
#             if self.left:
#                 self.left.insert(value)
#             else:
#                 self.left = NodeSearchTree(value)                
#         else:
#             if self.right:
#                 self.right.insert(value)    
#             else:
#                 self.right = NodeSearchTree(value)

#     def contains_from_2(self, value):
#         if names_2[value] == names_1[self.value]:
#             return True
#         elif names_2[value] < names_1[self.value] and self.left:
#             return self.left.contains_from_2(value)
#         elif names_2[value] > names_1[self.value] and self.right:
#             return self.right.contains_from_2(value)
#         else:
#             return False

# node_tree = NodeSearchTree(0)
# for i in range(1, len(names_1)):
#     node_tree.insert(i)

# for j in range(len(names_2)):
#     if node_tree.contains_from_2(j):
#         duplicates.append(names_2[j])


##### DICTIONARIES #####

# name_table = {}
# for name_1 in names_1:
#     name_table.update({name_1: True})
# for name_2 in names_2:
#     if name_table.get(name_2):
#         duplicates.append(name_2)


##### SETS #####

set_1 = set(names_1)
set_2 = set(names_2)

duplicates = list(set_1.intersection(set_2))



# duplicates = list(set(names_1).intersection(set(names_2)))


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
