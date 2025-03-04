M = [[1, 2, 3, 99], [4, 5, 6, 88], [7, 8, 9, 77]]

print([[row[i] for row in M] for i in range(len(M[0]))])