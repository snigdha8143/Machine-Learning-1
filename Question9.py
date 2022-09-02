weights_in_lbs = list()                     # Student weights list
N = int(input("Enter number of students "))      # Initializing the number of students from user
for i in range(N):                              # Running a for loop
    studentweights = float(input("Enter the weight of Student of student " + str(i+1)+ " in lbs: "))     # Asking the user to enter weights in lbs
    weights_in_lbs.append(studentweights*0.453592)                                      # Converting weights from lbs into kgs and appending them to the list
# Converting weight list to list with 2 decimal places
weights_in_kgs = ['%.2f' % elem for elem in weights_in_lbs]
# Displaying the weights in kgs with 2 decimal places
print("Weights of Students in kgs: \n\t\t\t\t\t\t\t" +str(weights_in_kgs))