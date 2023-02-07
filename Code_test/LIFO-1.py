

s = "{(([]))[]}"

def isValid(s):
    stack = []
    for p in s:
        print("stack is : {0}".format(stack))
        if p == "(" :
            stack.append(")")
        elif p == "{" :
            stack.append("}")
        elif p == "[" :
            stack.append("]")
        elif not stack or stack.pop() != p :
            return False
        
    return not stack

print(isValid(s))