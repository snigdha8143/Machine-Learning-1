import pandas as pd

data = {'first_column': ['1', '2', '3', '6', '6', '7', '10', '11'],
        'second_column': ['o', 'o', 'x', 'x', 'x', 'o', 'o', 'o'],

        }

df = pd.DataFrame(data)

print(df)
df.head(5)
x = df.loc[:,["first_column"]]
y = df.loc[:,["second_column"]]
#importing required libraries
from sklearn.neighbors import KNeighborsClassifier

#using KNN classifier with neighbors = 3
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(x_train, y_train)
y_test = knn.predict(x_test)
#accuracy
acc_knn = round(knn.score(x_test, y_test) * 100, 2)
#Displaying the accuracy
print("KNN accuracy is:",acc_knn)
#importing required libraries
from sklearn.metrics import classification_report
print(classification_report(x_test,y_test))