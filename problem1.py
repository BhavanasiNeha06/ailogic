n = int(input())
intervals = []
for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])
intervals.sort()
merged = []
for current in intervals:
    if len(merged) == 0:
        merged.append(current)
    else:
        last = merged[-1]
        if current[0] <= last[1]:
            if current[1] > last[1]:
                last[1] = current[1]
        else:
            merged.append(current)
for interval in merged:
    print(interval[0], interval[1])
