Input = input("Input:")
stack=[]
def isValid(Input):
    for sym in Input:
        if sym in ["(", "{", "["]:  
            stack.append(sym) 
        else:     
            current = stack.pop() 
            if current == "[": 
                if sym != "]": 
                    return False
            if current == "{": 
                if sym != "}": 
                    return False
            if current == "(": 
                if sym != ")": 
                    return False
  
    if stack: 
        return False
    return True
print(f'Output:{isValid(Input)}')