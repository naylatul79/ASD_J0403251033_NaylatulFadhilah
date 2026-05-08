#===================================================================================================
#Nama    : Naylatul Fadhilah
#NIM     : J0403251033
#Kelas   : TPL A1
#===================================================================================================

# ============================================================
# PRAKTIKUM 1 - Membuat Adjacency Matrix
# ============================================================

# Fungsi untuk membuat adjacency matrix
def createGraph(V, edges):

    # Membuat matrix ukuran V x V berisi 0
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Mengisi hubungan antar node berdasarkan edge
    for it in edges:
        u = it[0]   # node asal
        v = it[1]   # node tujuan

        mat[u][v] = 1  # memberi nilai 1 jika terhubung

        # karena graph undirected, maka hubungan dua arah
        mat[v][u] = 1

    return mat


if __name__ == "__main__":

    V = 4  # jumlah vertex/node

    # daftar edge (hubungan antar node)
    edges = [[0, 1], [0, 2], [1, 2], [1, 3]]

    # Membuat adjacency matrix
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:")

    # Menampilkan isi matrix
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()

# ============================================================
# PRAKTIKUM 2 - Membuat Adjacency List
# ============================================================

def createGraph(V, edges):

    adj = [[] for _ in range(V)]

    # Add each edge to the adjacency list
    for it in edges:

        u = it[0]
        v = it[1]

        adj[u].append(v)

        # since the graph is undirected
        adj[v].append(u)

    return adj


if __name__ == "__main__":

    V = 4

    # List of edges (u, v)
    edges = [[0, 1], [0, 2], [1, 2], [1, 3]]

    # Build the graph using edges
    adj = createGraph(V, edges)

    print("Adjacency List Representation:")

    for i in range(V):

        # Print the vertex
        print(f"{i}:", end=" ")

        for j in adj[i]:

            # Print its adjacent
            print(j, end=" ")

        print()

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


# ============================================================
# PRAKTIKUM 4 - Studi Kasus Dunia Nyata
# Digit akhir NIM = 3, maka studi kasus: Jaringan Komputer
# ============================================================
# ============================================================
# PRAKTIKUM 4 - Studi Kasus Dunia Nyata
# Digit akhir NIM = 3, maka studi kasus: Jaringan Komputer
# ============================================================

nodes = ["Router1", "Switch1", "Server", "PC1", "PC2"]

edges = [
    ("Router1", "Switch1"),
    ("Router1", "Server"),
    ("Switch1", "PC1"),
    ("Switch1", "PC2"),
    ("Server", "PC1"),
    ("Server", "PC2")
]

graph = {node: [] for node in nodes}
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

index = {node: i for i, node in enumerate(nodes)}
matrix = [[0 for _ in nodes] for _ in nodes]

for u, v in edges:
    matrix[index[u]][index[v]] = 1
    matrix[index[v]][index[u]] = 1

print("Nama node/perangkat:", nodes)

print("\nHubungan antar node/edge:")
for edge in edges:
    print(f"{edge[0]} -- {edge[1]}")

print("\nAdjacency List:")
for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")

print("\nAdjacency Matrix:")
print("Urutan node:", nodes)
for row in matrix:
    print(row)