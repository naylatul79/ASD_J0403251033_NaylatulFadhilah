#===================================================================================================
#Nama    : Naylatul Fadhilah
#NIM     : J0403251033
#Kelas   : TPL A1
#===================================================================================================

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