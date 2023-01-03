data = [10, 6, 3, 4, 1, 0]
i_best = 0
j_best = 1
i_min = 0
for j in range(2, len(data)):
    if data[j - 1] < data[i_min]:
        i_min = j - 1
    if data[j] - data[i_min] > data[j_best] - data[i_best]:
        i_best, j_best = i_min, j
print(i_best, j_best)
print(data[i_best], data[j_best])