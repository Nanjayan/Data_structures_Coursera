#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  
  def tree_inorder(results,index):
      if index==-1 :
        return
      tree_inorder(results,tree[index][1])
      results.append(tree[index][0])
      tree_inorder(results,tree[index][2])
  
  def in_order(tree):
    results=[]
    tree_inorder(results,0)  
    return results
  if tree:
    if tree[0][1]!=-1 or tree[0][2]!=-1 :
      v = in_order(tree)   
      sort_list=sorted(v)
      if sort_list==v:
        return True
      else:
        return False
    else:
      return True

  else:
    return True
  

 


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
