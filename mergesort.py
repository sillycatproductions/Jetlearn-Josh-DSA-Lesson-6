a = [345,567,213,98,546,23,908,8,1]
def merge(a):
    if len(a) > 1:
        mid = len(a) // 2
        l = a[:mid]
        r = a[mid:]
        merge(l)
        merge(r)
        # i = left - left
        # j = left - right
        # k = merged
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            a[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            a[k] = r[j]
            j += 1
            k += 1

def printlist(a):
    for i in range(len(a)):
        print(a[i], end = ' ')
    print()

print('Unsorted: ', a)
merge(a)
print('Sorted: ')
printlist(a)
