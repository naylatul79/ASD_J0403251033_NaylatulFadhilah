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

