# python3

import random
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    def PolyHash(S,p,x):
        hash_1=0
        s=len(S)
        for i in range(s-1,-1,-1):
            hash_1 = (hash_1*x + ord(S[i]))%p
        return hash_1
    
    def PrecomputeHashes(T,P,p,x):
        diff = len(T)-P
        H=[0 for i in range(diff+1)]
        S=T[diff:]
        H[diff]=PolyHash(S,p,x)
        y=1
        for i in range(P):
            y=(y*x)%p
        for i in range(diff-1,-1,-1):
            H[i]=(x*H[i+1] + ord(T[i]) - (y* ord(T[i +P])))% p
        return H

    p = 1000000007
    x = 263
    result=[]
    pHash = PolyHash(pattern,p,x)
    H = PrecomputeHashes(text,len(pattern),p,x)
    diff=len(text)-len(pattern)+1
    for i in range(diff):
        if pHash != H[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

