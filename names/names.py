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
class NameSearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = NameSearchTree(value)                
        else:
            if self.right:
                self.right.insert(value)    
            else:
                self.right = NameSearchTree(value)
                
                    
    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left:
            return self.left.contains(value)
        elif value > self.value and self.right:
            return self.right.contains(value)
        else:
            return False


name_tree = NameSearchTree("names to search")

for name_1 in names_1:
    name_tree.insert(name_1)

for name_2 in names_2:
    if name_tree.contains(name_2):
        duplicates.append(name_2)

        




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
