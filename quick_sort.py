import sys
from random import randint

def quick_sort(a, lo, hi):
    """Recursive quicksort with end pivot"""
    if lo >= hi: return
    pivot = a[hi]
    index = mid = lo
    while index < hi:
        if a[index] < pivot:
            a[index], a[mid] = a[mid], a[index]
            mid += 1
        index += 1
    a[mid], a[hi] = a[hi], a[mid] # move pivot to middle
    quick_sort(a, lo, mid - 1)
    quick_sort(a, mid + 1, hi)
    return

def main():
    a = list(range(10))
    for i, v in enumerate(a):
        a[i] = (randint(0, 10)) % 10
    #a.reverse()
    print(a)
    quick_sort(a, 0, len(a) - 1)
    print(a)

if __name__ == "__main__":
    main()
