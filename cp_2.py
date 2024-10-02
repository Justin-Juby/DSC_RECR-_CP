'''2.  Remove duplicates from array

Write a function that inputs an array. This function should return an array that has the elements in the same order, but with each element appearing only once. Assume the input array is already sorted.

Example Test Case: 
Input: [2,3,4,4,6,7,7]
Output: [2,3,4,6,7]
'''

def cp2(arr):
    output=[arr[0]]
    for i in arr[1:]:
        if i!=output[-1]:
            output.append(i)
    return output
    
arr=eval(input("enter the array(list)"))
print(cp2(arr))
        
'''
extras:
    what this approach does?

    we know, first element will always be unique in any array-> so we straight away store it in our output
    array.

    later we start our looping from 2nd element,and compare it with the last element of output array.
    this is because append always adds element to last->so we need to check only the last[-1 index] element.

    then we can return our output array, with unique values
    
'''
