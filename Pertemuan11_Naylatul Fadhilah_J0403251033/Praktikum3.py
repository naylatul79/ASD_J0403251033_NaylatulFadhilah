#===================================================================================================
#Nama    : Naylatul Fadhilah
#NIM     : J0403251033
#Kelas   : TPL A1
#===================================================================================================

# ============================================================
# PRAKTIKUM 3 - Konversi Matrix ke List
# ============================================================

matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

V = len(matrix)

adj = [[] for _ in range(V)]

# Konversi matrix ke adjacency list
for i in range(V):
    for j in range(V):

        if matrix[i][j] == 1:
            adj[i].append(j)

print("Adjacency Matrix to Adjacency List Representation:")

for i in range(V):

    print(f"{i}:", end=" ")

    for j in adj[i]:
        print(j, end=" ")

    print()
