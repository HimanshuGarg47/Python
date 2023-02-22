class SparseTable:
    def __init__(self, arr):
        
        n = len(arr)
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1
        self.table = [[0 for i in range(self.log[n] + 1)] for j in range(n)]
        for i in range(n):
            self.table[i][0] = arr[i]
        for j in range(1, self.log[n] + 1):
            for i in range(0, n - (1 << j) + 1):
                self.table[i][j] = min(self.table[i][j - 1], self.table[i + (1 << (j - 1))][j - 1])

        print(self.table)
        print(self.log)

    def query(self, l, r):
        k = self.log[r - l + 1]
        return min(self.table[l][k], self.table[r - (1 << k) + 1][k])

st = SparseTable([1, 3, 2, 5, 4, 6, 8, 7])