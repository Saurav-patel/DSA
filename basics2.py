# =========================
#  1. Tuple (Pair) & Unpacking
# =========================
p = (1,2)
a,b = p
print(a)
print(b)


# =========================
#  2. Nested Tuples (Tuple of Pairs)
# =========================
pair = ((1,2) , (3,4) , (5,6))
#for i in pair:
    #print(i[0],i[1])


# =========================
#  3. List Basics (Vector Equivalent)
# =========================
arr = [5, 10, 15, 20, 25]

#print(arr[0])  # Output: 5

arr[2] = 30
#print(arr)


# =========================
#  4. List of Tuples (Array of Pairs)
# =========================
arr1 = [(1, 2), (3, 4), (5, 6)]

#print(arr1[1][0])

#for i,j in arr1:
    #print("i =", i, "j =", j)

#for i in arr1:
    #print("i =", i[0] , "j=",i[1])


# =========================
#  5. List Operations 
# =========================
print(arr1.pop())
print(arr1)

arr1.append( (7, 8))  # append adds the element at the end of the list

arr1.insert(1 , (9,10)) # insert adds element at index
arr1.remove((3,4)) # remove deletes first occurrence
arr1.pop(2) # pop removes element at index


#print(arr1)

#print(arr1.sort())


# =========================
#  6. Sorting & Length
# =========================
arr2 = [3, 1, 4, 1, 5, 9]
arr2.sort()
# print(arr2)
# print(len(arr2))
# print(arr1)
# print(len(arr1))


# =========================
#  7. Dynamic List Creation
# =========================
empty_arr = []
empty_arr.append(1)
empty_arr.append(2)
empty_arr.insert(1,(5,6))
#print(empty_arr)


# =========================
#  8. 2D Array (Matrix Creation & Input)
# =========================
# rows = int(input("Enter the rows of the array: "))
# columns = int(input("Enter the columns of the array: "))
# dynamic_arr = [[0 for j in range(columns)] for i in range(rows)]
# for i in range(rows):
#     for j in range(columns):
#         dynamic_arr[i][j] = int(input(f"Enter element at position ({i}, {j}): "))

# dynamic_arr1 = [[0] * columns for _ in range(rows)]
# print(dynamic_arr1)

# for i in range(rows):
#     for j in range(columns):
#         dynamic_arr1[i][j] = int(input(f"Enter element at position ({i}, {j}): "))


# =========================
#  9. Matrix Traversal & Printing
# =========================
# for i in range(rows):
#     for j in range(columns):
#         print(dynamic_arr1[i][j], end=" ")
#     print()


# =========================
#  10. Reference vs Copy (VERY IMPORTANT)
# =========================
arr3 = [1, 2, 3, 4, 5]

arr4 = arr3
arr4.append(6)
# print(arr3)
# print(arr4)

arr5 = arr3.copy()
arr5.append(7)
# print(arr3)
# print(arr5)


# =========================
#  11. Matrix Traversal (Row-wise + Element-wise)
# =========================
# arr6 = [[1,2,3], [4,5,6], [7,8,9]]

# for i in arr6:
#     print("i =", i)
#     for j in i:
#         print(" j =", j , end=" ")
#     print()



arr7 = []
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
for i in range(rows):
    row=[]
    for j in range(columns):
        val = int(input(f"Enter element at position {i} {j} :"))
        row.append(val)
    arr7.append(row)


for i in range(rows):
    for j in range(columns):
        print(arr7[i][j] , end=" ")
    print()