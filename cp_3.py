'''3. Print the date based on the entered day and year

Write a function that inputs two integers: the day number and the year. This function should generate a string that has the entire date with the date, month and year mentioned. Ensure that the function also considers leap years.

Example Test Case:
Inputs:  256, 2021
Output: “13 September, 2021”
'''

def cp3(days,year):
    dataset = [(31, "January"), (28, "February"), (31, "March"), (30, "April"),
               (31, "May"), (30, "June"), (31, "July"), (31, "August"),
               (30, "September"), (31, "October"), (30, "November"), (31, "December")]

    leap_year=(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if leap_year:
        dataset[1] = (29, "February")

    for daysM,month in dataset:
        if days <= daysM:
            return f"{days} {month}, {year}"
        days -= daysM
days=int(input("enter total days"))
year=int(input("enter year"))
print(cp3(days,year))



''' key concept used in calculating days -> day and month:
 we compare the given total days with total days in each and every month from the given dataset,
 if the given days in larger than days in month-> we subtract it with the number of days in that month and loop
 procedes to next month-> at last giving the req. days with month


 lets say we give total days as 29.
 so obviously 29 is less than 31 days in jan.

 so our date comes out to be 29 Jan

 if we give days as 71.
 71 is more than 31 days in jan->so we subtract 71 with 31->we get 40

 now we compare 40 with next month feb(28/29 days)->again 40 is more than 28(lets say)
 so, 40-28 -->12.

 we compare 12 with 31 in march, which is less.
 so our date comes out to be 12 march :)


 i found logic of this program a bit tricky compared with others, alas i did it
 '''
    
