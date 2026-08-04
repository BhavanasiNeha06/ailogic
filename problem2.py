
n = int(input())
arr = list(map(int,input().split()))
k = int(input())
max_len = 0
best_start = 1
for i in range(n):
    min_val = arr[i]
    max_val = arr[i]
    for j in range(i, n):
        if arr[j] < min_val:
            min_val = arr[j]
        if arr[j] > max_val:
            max_val = arr[j]
            
        if max_val - min_val <= k:
            curr_len = j - i + 1
            if curr_len > max_len:
                max_len = curr_len
                best_start = i + 1
        else:
            break

print(f"{max_len} {best_start}")

