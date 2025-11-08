import numpy as np


B = np.arange(1, 13).reshape(3, 4)
# B = np.arange(1, 13)
print("B is:\n", B)

subset1 = B[2:9]
print("\nSubset of B from index 2 to 8 is:\n", subset1)

subset2 = B[1:3, 2:4]
print("\nSubset of B from rows 1 to 2 and columns 2 to 4 is:\n", subset2)

subset3 = B[:, 1]
print("\nSubset of B with all rows and column 1 is:\n", subset3)

subset4 = B[1:3, 2:4]
subset4 = subset4[subset4 > 9]
print("\nSubset of B from rows 1 to 2 and columns 2 to 4 with values greater than 9 is:\n", subset4)

mask = B > 6
print("\nMask is:\n", mask)

filtered = B[B > 6]
filtered = B[mask]
print("\nFiltered values are:\n", filtered)

B[B > 6] = 0
print("\nB is:\n", B)

subset = B[(B > 3) & (B < 9)]
print("\nSubset of B where values are between 3 and 9 is:\n", subset)

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 4, 6, 8, 10, 12])
np.corrcoef(x, y)
print("\nCorrelation coefficient between x and y is:\n", np.corrcoef(x, y))

m = np.array([[1, 2, 3, 4, 5, 6], [8, 7, 6, 5, 4, 3]])
print("\nm is:\n", m)


# B = np.arange(1, 13).reshape(3, 4)
# print("\nB is:\n", B)
# C = np.arange(1, 13)
# print("\nC is:\n", C)
# Dlist = [i for i in range(1, 13)]
# print("\nDlist is:\n", Dlist)

# print("\nDlist > 6 is:\n", [x for x in Dlist if x > 6])

# E = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print("\nE is:\n", E)

# B.sum(axis=0)   # sum down each column → [15 18 21 24]
# B.sum(axis=1)   # sum across each row  → [10 26 42]
# print("\nSum down each column:\n", B.sum(axis=0))
# print("\nSum across each row:\n", B.sum(axis=1))