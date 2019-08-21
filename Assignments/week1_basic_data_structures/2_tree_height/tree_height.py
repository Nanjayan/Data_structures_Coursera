# python3

import sys
import threading


def compute_height(n, parents):
    
    height_list = [0 for i in range(n)]
    max_height = 0
    for vertex in range(n):
        if height_list[vertex]!=0:
            continue
        height = 0
        val = vertex
        while val != -1:
            if height_list[val]!=0:
                height+=height_list[val]
                break
            height+=1
            val=parents[val]
        max_height = max(max_height,height)
        val = vertex
        while val != -1:
            if height_list[val]!=0:
                break
            height_list[val]=height
            height-=1
            val=parents[val]
    return max_height
        
        


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
