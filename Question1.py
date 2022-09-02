ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]   # Student ages as given in problem
print(ages)                                       # Displaying the ages
ages.sort()                                       # performing sort operation on ages
print(ages)                                       # Displaying the ages after sorting (sorting order)
x = min(ages)                                     # Finding the minimum age from the list and storing it in a variable "x"
y = max(ages)                                     # Finding the maximum age from the list and storing it in a variable "y"
print(x)                                          # Displaying the minimum age (value stored in x)
print(y)                                          #  Displaying the maximum age (value stored in y)
ages.append(x)                                    # Adding the minimum value (value of x) to the list
print(ages)                                       # Displaying ages list
ages.append(y)                                    # Adding the maximum value (value of y) to the list
print(ages)                                       # Displaying ages list
z = len(ages)                                     # Finding the length of the  ages list
print(z)                                          # Displaying the length
p = (z-1)//2                                      # Performing the floor division
print(p)                                          # Displaying the value of floor division (value stored in p)
median_x = (ages[p] + ages[p+1])/2                 # Performing the median
print(median_x)                                    # Displaying median
sum_1 = sum(ages)                                  # Performing sum for the addition of ages
print(sum_1)                                       # Displaying the sum of ages
avg = sum_1/z                                      # Performing  the average
print(avg)                                        # Displaying average
range_1 = y-x                                      # Finding the range
print(range_1)                                     # Displaying range