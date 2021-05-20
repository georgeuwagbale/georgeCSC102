array1 = [
    [11,12,5,2],
    [15,6,10],
    [10,8,12,5],
    [12,15,8,6]
    ]
def display(Array1):
    for a in Array1:
        for b in a:
            print(b, end=" ")
        print("")
        
display(array1)
#ACCESSING VALUES IN A TWO DIMENSIONAL ARRAY

print(array1[1])
print(array1[1][2])

#UPDATING VALUES IN A TWO DIMENSIONAL ARRAY
array1[0] = [1,2,3,4]
print(array1)
print()

array1[0][1] = 5
print(array1)
print()

array1.insert(3,[3,53,7,9])
display(array1)

#DELETING THE VALUES IN A TWO DIMENSIONAL ARRAY

del array1[3]

display(array1)
