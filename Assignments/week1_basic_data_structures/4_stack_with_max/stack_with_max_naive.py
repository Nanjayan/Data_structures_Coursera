#python3
import sys



class StackWithMax():
    def __init__(self):
        self.__stack = []
        

    def Push(self, a):
        self.__stack.append(a)
        

    def Pop(self):
        assert(len(self.__stack))
        return self.__stack.pop()
        

    def Max(self):
        pass


if __name__ == '__main__':
    stack = StackWithMax()

    #Create a new list for storing max values
    max=[]

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
            val=int(query[1])
            #Add only the max values in the stack
            if len(max)==0 :
                max.append(val)
            elif val>= max[-1]:
                max.append(val)

        elif query[0] == "pop":
            cur = stack.Pop()
            #if the max value is popped, remove from max stack
            if cur == max[-1]:
                max.pop()
        elif query[0] == "max":
            #Print the top element of max stack
            print(max[-1])
                
        else:
            assert(0)
