from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import pickle

df = pd.read_csv('insurance.csv')

df = df.drop('region', axis='columns')

onehot = pd.get_dummies(df)
data = onehot

data = data.drop('sex_male', axis='columns')
data = data.drop('smoker_yes', axis='columns')

columns_titles = ['age', 'sex_female', 'bmi',
                  'children', 'smoker_no', 'expenses']
data = data.reindex(columns=columns_titles)
data.head()

# Create independant (X) and dependant (y) variables
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Data divided into a training and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# This class will identify the best features with highest p-values to determine the dependant variable
regressor = LinearRegression()
regressor.fit(X_train, y_train)

np.set_printoptions(precision=2)

# user_input = [[19,"female",27.1,0,"no"]]

# if user_input[0][1] == "female" or user_input[0][1] == "Female":
#     user_input[0][1]= 1
# else:
#     user_input[0][1] = 0

# if user_input[0][4] == "no" or user_input[0][1] == "No":
#     user_input[0][4]= 1
# else:
#     user_input[0][4] = 0

# # get prediction for new input
# output = regressor.predict(user_input)

pickle.dump(regressor, open('model.pkl', 'wb'))
