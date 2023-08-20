#Ordena manualmente tres stacks

import string
    
stack = [1,2,3]
stack2 = [5,4]
stack3 = []

stack3.append(stack.pop())
stack3.append(stack.pop())
stack3.append(stack.pop())
stack.append(stack2.pop())
stack2.append(stack3.pop())
stack.append(stack3.pop())
stack.append(stack2.pop())
stack2.append(stack3.pop())
stack3.append(stack.pop())


print (stack)
print (stack2)
print (stack3)