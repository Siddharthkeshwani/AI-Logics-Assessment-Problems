# Problem 3

def addingTwoNumbers(l1, l2):
    carry = 0
    result = []

    i, j = 0, 0
    while i < len(l1) or j < len(l2) or carry:
        x = l1[i] if i < len(l1) else 0
        y = l2[j] if j < len(l2) else 0

        total = x + y + carry
        result.append(total % 10)
        carry = total // 10

        i += 1
        j += 1

    return result

n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

ans = addingTwoNumbers(l1, l2)
print(*ans)
