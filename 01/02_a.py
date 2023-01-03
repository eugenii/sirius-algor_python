N, K = [int(i) for i in input().split()]
data = [int(i) for i in  input().split()]
i_best = 0
j_best = K + 1
i_max = 0
for j in range(K + 2, N):
    if data[j - K - 1] > data[i_max]:
        i_max = j - K - 1
    if data[i_max] + data[j] > data[i_best] + data[j_best]:
        i_best, j_best = i_max, j
print(i_best + 1, j_best + 1)