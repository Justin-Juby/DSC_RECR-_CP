'''1. Arrange words in a string in the order of their length

Write a function that inputs a string. The function should return the string sorted in ascending order of the length of the words.

Example Test Case:
Input: "This is a cool sentence"
Output: "a is this cool sentence"

'''

#starting of program:)

def str1(S):
    a=S.split()     
    output=''
    b=tuple(a)      
    c= sorted(b, key=len)    
    for i in c:
        output+=i           
        output+=' '         
    return output            

s=str(input("Enter string"))
print(str(s))

'''
extras:
    why did i chose this approach?

    well before coming to this, i had tried another way...using for loop directly into variable a,
     but later on i wasn't getting clear cut output.

     thought of, is there any other built in thing which arranges in acsending order ? - yes, thought of tuple
     and did this approach!
'''

