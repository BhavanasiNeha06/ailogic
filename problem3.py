n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))

result = []
carry = 0
i = 0
j = 0

while i < n or j < m or carry:
    total = carry
    if i < n:
        total += first[i]
        i += 1
    if j < m:
        total += second[j]
        j += 1

    result.append(str(total % 10))
    carry = total // 10

print(" ".join(result))
