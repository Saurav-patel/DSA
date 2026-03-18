p = (1,2)
a,b = p
print(a)
print(b)

pair = ((1,2) , (3,4) , (5,6))
#for i in pair:
    #print(i[0],i[1])



arr = [5, 10, 15, 20, 25]

#print(arr[0])  # Output: 5

arr[2] = 30
#print(arr)  

arr1 = [(1, 2), (3, 4), (5, 6)]

#print(arr1[1][0])

#for i,j in arr1:
    #print("i =", i, "j =", j)

#for i in arr1:
    #print("i =", i[0] , "j=",i[1])

print(arr1.pop())
print(arr1)
arr1.append( (7, 8))  #append adds the element at the end of the list
#print(arr1)

arr1.insert(1 , (9,10)) #insert adds the element at the specified index and shifts the rest of the elements to the right
arr1.remove((3,4)) #remove removes the first occurrence of the specified element from the list
arr1.pop(2) #pop removes the element at the specified index and returns it. If no index is specified, it removes and returns the last element of the list

#print(arr1)

#print(arr1.sort())

arr2 = [3, 1, 4, 1, 5, 9]
arr2.sort()
# print(arr2)
# print(len(arr2))
# print(arr1)
# print(len(arr1))

empty_arr = []
empty_arr.append(1)
empty_arr.append(2)
empty_arr.insert(1,(5,6))
#print(empty_arr)

rows = int(input("Enter the rows of the array: "))
columns = int(input("Enter the columns of the array: "))
# dynamic_arr = [[0 for j in range(columns)] for i in range(rows)]
# for i in range(rows):
#     for j in range(columns):
#         dynamic_arr[i][j] = int(input(f"Enter element at position ({i}, {j}): "))

dynamic_arr1 = [[0] * columns for _ in range(rows)]
print(dynamic_arr1)

for i in range(rows):
    for j in range(columns):
        dynamic_arr1[i][j] = int(input(f"Enter element at position ({i}, {j}): "))


for i in range(rows):
    for j in range(columns):
        print(dynamic_arr1[i][j], end=" ")
    print()
#print("The 2D array is:")
# for i ,j in dynamic_arr:
#     print(i , j)
# for i , j in dynamic_arr:
#     print(i , j)

# for i in range(rows):
#     for j in range(columns):
#         print(dynamic_arr[i][j], end=" ")
#     print()

# for i in dynamic_arr:
#     print(i)


arr3 = [1, 2, 3, 4, 5]
arr4 = arr3
arr4.append(6)
# print(arr3)  # Output: [1, 2, 3, 4 , 5, 6]
# print(arr4)  # Output: [1, 2, 3, 4 , 5, 6]

arr5 = arr3.copy()
arr5.append(7)
# print(arr3)  # Output: [1, 2, 3, 4 , 5, 6]
# print(arr5)  # Output: [1, 2, 3, 4 , 5, 6, 7]