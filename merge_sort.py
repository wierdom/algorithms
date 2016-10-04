import sys
from random import randint

def merge_sort(a, i, j):
    if i == j: return
    k = (i + j) // 2
    merge_sort(a, i, k)
    merge_sort(a, k + 1, j)
    b = []
    p1 = i
    p2 = k + 1
    while p1 <= k and p2 <= j:
        if a[p1] < a[p2]:
            b.append(a[p1])
            p1 += 1
        else:
            b.append(a[p2])
            p2 += 1
    (p1, p2) = (p1, k) if p1 <= k else (p2, j)
    while p1 <= p2:
        b.append(a[p1])
        p1 += 1
    a[i:j+1] = b
    return

def main():
    a = list(range(10))
    for i, v in enumerate(a):
        a[i] = (randint(0, 10)) % 10
    #a.reverse()
    print(a)
    merge_sort(a, 0, len(a) - 1)
    print(a)

if __name__ == "__main__":
    main()
