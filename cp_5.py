'''
5. Design your own Stack
Design your own stack! The stack should have three functions: push(int), pop() and peek().
You are only allowed to use Arrays or Linked Lists.

'''


stack=[]
def push(stack):
    while True:
        num=int(input("enter number to push into the stack"))
        stack.append(num)
        choice=input("do you want to push more elements?(y/n)")
        if choice.lower()=='n':
            break
    return stack

def pop1(stack):
    while len(stack):
        print(stack.pop())
    else:
        print("stack empty")
    

def peek(stack):
    if len(stack)==0:
        print("Stack empty")
    else:
        return stack[-1]
print(push(stack))
while True:
    a=input("do you want to pop elements?(y/n)")
    if a.lower()=='n':
        break
    print(pop1(stack))
        
print("the top value of stack is",peek(stack))
