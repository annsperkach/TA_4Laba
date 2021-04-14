def QuickSort(A,p,r):               #the procedure of quick sort
    count = 0
    if p < r:
        q, CountTemp = ClassicPartition(A, p, r)
        count += CountTemp
        count += QuickSort(A, p, q-1)
        count += QuickSort(A, q+1, r)
    return count

def ClassicPartition(A, p, r):        #the procedure of classic partition
    x = A[r]
    i = p-1
    counter = 0
    for j in range(p, r):
        counter += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1, counter

def MedianQuickSort(A, p, r):       #the procedure of improved quick sort by the mediana
    count = 0
    if p<r:
        q, CountTemp = MedianPartition(A, p, r)
        count += CountTemp
        count += MedianQuickSort(A, p, q-1)
        count += MedianQuickSort(A, q+1, r)
    return count

def MedianPartition(A, p, r):         #the procedure of improved partition by the mediana
    if len(A[p:r]) > 3:
        mid = ((p + r) // 2)
        middle = A[mid]
        if A[p] < middle < A[r] or A[r] < middle < A[p]:
            x = middle
        elif middle < A[p] < A[r] or A[r] < A[p] < middle:
            x = A[p]
        else:
            x = A[r]
        index = A.index(x)
        A[r], A[index] = A[index], A[r]
    x = A[r]
    i = p - 1
    counter = 0
    for j in range(p, r):
        counter += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1, counter

def ThreePivotPartition(A, left, right):         #the procedure of three pivots partition
    counter = 0
    a = left +2
    b = left +2
    c = right -1
    d = right -1
    p = A[left]
    q = A[left+1]
    r = A[right]

    while b<=c:
        while A[b]<q and b<=c:
            counter +=1
            if A[b]<p:
                A[a], A[b] = A[b], A[a]
                a +=1
            b+=1
        while A[c]>q and b<=c:
            counter +=1
            if A[c]>r:
                A[c], A[d] = A[d], A[c]
                d -=1
            c -=1
        if b<=c:
           if A[b] > r:
                if A[c] < p:
                    A[b], A[a] = A[a], A[b]
                    A[a], A[c] = A[c], A[a]
                    a +=1
                else:
                    A[b], A[c] = A[c], A[b]
                A[c],A[d]=A[d],A[c]
                b +=1
                c -=1
                d -=1
           else:
              if A[c]<p:
                    A[b], A[a] = A[a], A[b]
                    A[a], A[c] = A[c], A[a]
                    a +=1
              else:
                    A[b], A[c] = A[c], A[b]
              b +=1
              c -=1
        a -=1
        b -=1
        c +=1
        d +=1
        A[left +1], A[a] = A[a], A[left +1]
        A[a], A[b] = A[b], A[a]
        a -=1
        A[left], A[a] = A[a], A[left]
        A[right], A[d]=A[d], A[right]
        return c, counter

def ThreePivotQuickSort(A, p, r):         #the procedure of quick sort by the three pivots
    count =0
    threepivots= [A[p], A[p+1], A[r]]
    for k in range (0,2):
        if threepivots[k+1] < threepivots[k]:
            threepivots[k],threepivots[k+1]=threepivots[k+1],threepivots[k]
    A[p]=threepivots[0];
    A[p+1]=threepivots[1];
    A[r]=threepivots[2];
    if p < r and r - p > 3:
        q, CountTemp = ThreePivotPartition(A, p, r)
        count += CountTemp
        count += ThreePivotQuickSort(A, p, q-1)
        count += ThreePivotQuickSort(A, q+1, r)
    return count

def main():                      #our main
    file = open("input.txt")
    read = file.read()
    file.close()
    A = []
    A = list(map(int, read.splitlines()))
    n = A[0]
    del A[0]
    A2 = A
    A3 = A

    counter1 = QuickSort(A, 0, n - 1)
    counter2 = MedianQuickSort(A2, 0, n - 1)
    counter3 = ThreePivotQuickSort(A3, 0, n-1)

    result = [counter1, counter2, counter3]
    FileResult = open('is01_sperkach_04_output.txt', 'w')
    for i in range(0, 3):
        FileResult.write(str(result[i]) + " ")
main()
