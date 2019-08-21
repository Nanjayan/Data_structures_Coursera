# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Adding the element and its position in the stack
            opening_brackets_stack.append(i+1)
            opening_brackets_stack.append(next)
            

        if next in ")]}":
            # Checking whether the stack is empty ot not
            if(len(opening_brackets_stack)>0):
                # Getting the top element and checking its validity
                top_element = opening_brackets_stack.pop()
                top_element_pos = opening_brackets_stack.pop()
                valid = are_matching(top_element,next)
                #If not valid, returning the position of unmatched closed bracket
                if (valid==False):
                    return str(i+1)
            else:
                return str(i+1)
    
    #checking whether the stack is empty ot not
    length = len(opening_brackets_stack)
    #If not empty, returning the position of unmatched opening bracket
    #Otherwise returning success
    if(length):
        return str(opening_brackets_stack[0])
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print (mismatch)

if __name__ == "__main__":
    main()
