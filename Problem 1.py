# Problem 1

n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Sort by start time
intervals.sort(key=lambda x: x[0])

merged = []
for start, end in intervals:
    if not merged or merged[-1][1] < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

# Print result
for s, e in merged:
    print(s, e)
