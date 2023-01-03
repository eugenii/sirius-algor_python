count = int(input())
data = [int(i) for i in input().split()]
i_b = 0
j_b = 1
i_min = 0
for j in range(2, count):
    if data[j - 1] < data[i_min]:
        i_min = j - 1
        # print(data[i_min])
    if data[j] / data[i_min] > data[j_b] / data[i_b]:
        i_b, j_b = i_min, j
if data[j_b] / data[i_b] <= 1:
    print(0, 0)
else:
    print(i_b + 1, j_b + 1)
