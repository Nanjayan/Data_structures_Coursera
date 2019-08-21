# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    
    # A new recursive method to do that
    def tree_inorder(self,index):
      
      if self.left[index]!=-1 :
        tree_inorder(self,self.left[index])
      self.result.append(self.key[index])
      if self.right[index]!=-1:
        tree_inorder(self,self.right[index])
    
    tree_inorder(self,0) 

    return self.result

  def preOrder(self):
    self.result = []
    
    # A new recursive method to do that
    def tree_preorder(self,index):
      
      self.result.append(self.key[index])
      if self.left[index]!=-1 :
        tree_preorder(self,self.left[index])
      if self.right[index]!=-1:
        tree_preorder(self,self.right[index])
    
    tree_preorder(self,0) 
                
    return self.result

  def postOrder(self):
    self.result = []
    # A new recursive method to do that

    def tree_postorder(self,index):
      
      if self.left[index]!=-1 :
        tree_postorder(self,self.left[index])
      
      if self.right[index]!=-1:
        tree_postorder(self,self.right[index])
      self.result.append(self.key[index])
    
    tree_postorder(self,0) 
               
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
