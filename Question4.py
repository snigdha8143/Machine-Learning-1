it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}    # Created a set of it companies
A = {19, 22, 24, 20, 25, 26}                                                              # allocated set of numbers to a
B = {19, 22, 20, 25, 26, 24, 28, 27}                                                      # allocated set of numbers to b
age = [22, 19, 24, 25, 26, 24, 25, 24]                                                    # created a set of ages
len1 = len(it_companies)                                                 # for  finding the lenght of companies set
print(len1)                                                              # Print the lenghth of it_companies set
it_companies.add("Twitter")                                              # Append twitter to it_companies set
print(it_companies)                                                      # Printing the it_companies
it_companies1 = {"TCS", "Accenture", "Infosys", "Deloitte", "Wipro", "Cap Gemini"}    # Creating various it_companies1 set
it_companies.update(it_companies1)                               # Inserting various it_companies1 set to it_companies
print(it_companies)                                                             # Printing it_companies after insertion
it_companies.remove("Accenture")                                                # deducting single company from it_companies
print(it_companies)                                                             # Printing after deduction

print(A.union(B))                                              # combine A and B
print(A.intersection(B))                                       # to find A intersection B
print(A.issubset(B))                                           # to find A is subset of B
print(A.isdisjoint(B))                                         # Finding whether A and B are disjoint sets
print(A.union(B))                                              # combine A with B
print(B.union(A))                                              # combine B with A
print(A.symmetric_difference(B))                               # to find the symmetric difference between A and B
A.clear()                                                      # Deleting the whole set A
print(A)                                                       # verify whether it is deleted or not
B.clear()                                                      # Deleting the whole set B
print(B)                                                       # verify whether it is deleted or not
ageset = set(age)                                              # Changing the list to set
print(ageset)                                                  # Printing the changed set
listlen = len(age)                                             # Find the length of the list
print(listlen)                                                 # Print the length of the list
setlen = len(ageset)                                           # Find the length of the set
print(setlen)                                                  # Print the length of the set

# length of the set is less than the length of the list since in set duplicate elements will be removed