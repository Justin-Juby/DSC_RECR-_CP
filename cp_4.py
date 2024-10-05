'''4. The bottle shipping problem

A company manufactures packing cartons in four sizes: small, medium, large and xl. These cartons can hold 6 bottles, 12 bottles, 24 bottles and 48 bottles respectively.

Write a function that inputs the number of bottles to be shipped by the company. The function should print the break-up of the number of cartons used in descending order of capacity.

Example Test Case:
Input: 140
Output: 2 xl, 1 large, 1 medium, 1 small
'''

def cp4(bottles):
    
    xl = bottles // 48
    bottles %= 48  

    large = bottles // 24
    bottles %= 24  

    medium = bottles // 12
    bottles %= 12  

    small = bottles // 6
    bottles %= 6

    EXTRAS = bottles
    return f"{xl} xl, {large} large, {medium} medium, {small} small {EXTRAS} extra"


bottles=int(input("enter number of bottles to be shipped"))
print(cp4(bottles))


''' concept used here:

 first we divide the bottles into large container--> thereby updating the bottle to remaining bottle left using rem%
 operation and we continue the process.

 '''

    
