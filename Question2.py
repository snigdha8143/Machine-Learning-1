dog = dict()                                          # Created a dog dictionary
dog["name"] = "MOMO"                       # Giving name of the dog
dog["color"] = "white"                                # Giving color of the dog
dog["breed"] = " chow chow"                  # Giving Breed of the dog
dog["legs"] = 4                                     # Giving no of legs of the dog
dog["age"] = 3                                       # Giving age of the dog
print(dog)                                            # Displaying the dog dictionary

student = dict()                                                # Creating a student dictionary
student["first_name"] = "SRI SNIGDHA"                                 # Giving firstname to the student dictionary
student["last_name"] = "MADISETTY"                                  # Giving lastname to the student dictionary
student["gender"] = "Female"                                      # Giving gender to the student dictionary
student["age"] = 22                                            # Giving age to the student dictionary
student["marital status"] = "Single"                            # Giving marital status to the student dictionary
student["skills"] = ["C", "Python"]                     # Giving skills to the student dictionary
student["country"] = "INDIA"                                      # Giving country to the student dictionary
student["city"] = "KHAMMAM"                               # Giving city to the student dictionary
student["address"] = "Gandhichowk khammam 507003"        # Giving address to the student dictionary
print(student)                                                  # Displaying student dictionary
len_1 = len(student)                                             # Finding the length of the student dictionary
print(len_1)                                                     # Length of the student dictionary
print(student["skills"])                                        # skills in the list format
print(type(student["skills"]))                                  # Displaying the type of the student skills
student["skills"].extend(["Machine Learning", "DBMS"])    # Modifying the skills values of the student dictionary
print(student["skills"])                                        # Displaying the skills of the student dictionary
print(student.keys())                                           # Displaying the student dictionary keys as a list
print(student.values())                                         # Displaying the student dictionary values as a list