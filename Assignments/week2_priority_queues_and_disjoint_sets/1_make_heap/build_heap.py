# python3

import math

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following advanced implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a binary heap
    
    # implement a binary heap tree for faster implementation

    swaps=[]
    def siftdown(i,n,H):
        minindex=i
        l=2*i+1
        if l<n and H[l]<H[minindex]:
            minindex=l
        r=2*i+2
        if r<n and H[r]<H[minindex]:
            minindex=r
        if i != minindex:
            swaps.append((i,minindex))
            temp=H[i]
            H[i]=H[minindex]
            H[minindex]=temp
            siftdown(minindex,n,H)
        
    
    
    n=len(data)
    for i in range(math.floor((n-1)/2),-1,-1):
        siftdown(i,n,data)

    return swaps



def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
