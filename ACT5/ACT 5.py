# Define sets A, B, and C
A = {'a', 'b', 'c', 'd', 'g', 'f'}
B = {'l', 'm', 'o', 'h', 'c', 'b'}
C = {'h', 'c', 'd', 'f', 'j', 'i' , 'k'}


# How many elements are there in set A and B
num_A = len(A)
num_B = len(B)
print("Number of elements in A:", num_A)
print("Number of elements in B:", num_B)

#b. How many elements are there in B that is not part of A and C

num_b_not_AC = len(B - A - C)
print("Number of elements in B that is not part of A and C:", num_b_not_AC)

#c. Show the following using set operations
print("i.  ", sorted(list(C - A)))
print("ii. ", sorted(list(A.intersection(C))))
print("iii.", sorted(list((B.intersection(A)).union(C.intersection(B)))))
print("iv. ", sorted(list((A.intersection(C)) - B)))
print("v.  ", sorted(list(B.intersection(A & C))))
print("vi. ", sorted(list(B - (A.union(C)))))
