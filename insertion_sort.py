import sys

try:
    x = sys.argv[1]
except:
    x = [5, 2, 4, 6, 1, 3]

lst = []
for i in x:
    lst.append(int(i))

#################################################################################
# Insertion sort algorithm increasing order / Time Complexity (O(n**2))
for j in range(1, len(lst)):
    key = lst[j]
    i = j - 1
    while i >= 0 and lst[i] > key:
        lst[i+1] = lst[i]
        i -= 1
    lst[i+1] = key
#################################################################################


print(lst)


#################################################################################
# Insertion sort algorithm decreasing order / Time Complexity (O(n**2))
for j in range(1, len(lst)):
    key = lst[j]
    i = j - 1
    while i >= 0 and lst[i] < key:
        lst[i+1] = lst[i]
        i -= 1
    lst[i+1] = key
#################################################################################

print(lst)

