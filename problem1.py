n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])
merged = []
for interval in arr:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

for interval in merged:
    print(interval[0], interval[1])
