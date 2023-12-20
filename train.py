import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('https://raw.githubusercontent.com/Nireplag/mushroom_edibility/main/mushrooms.csv')

# make all columns lowercase
df.columns = df.columns.str.replace(' ', '_').str.lower()
df.columns = df.columns.str.replace('-', '_').str.lower()

# split dataset into test and train

# test data will be 15% of the total

df_train, df_test = train_test_split(df,test_size=0.15, shuffle=True, random_state=7, stratify=df['class'])

x_train = df_train.drop(['class'], axis = 1)
y_train = df_train['class']

x_test = df_test.drop(['class'], axis = 1)
y_test = df_test['class']

# drop columns and transform y variable to int

x_train = x_train.drop(['veil_type'], axis = 1)
x_train = x_train.drop(['stalk_shape'], axis = 1)
x_train = x_train.drop(['gill_attachment'], axis = 1)

x_test = x_test.drop(['veil_type'], axis = 1)
x_test = x_test.drop(['stalk_shape'], axis = 1)
x_test = x_test.drop(['gill_attachment'], axis = 1)

y_train = (y_train == 'p').astype('int')
y_test = (y_test == 'p').astype('int')

# transform categorical data

dv = DictVectorizer(sparse=False)

x_train = dv.fit_transform(x_train.to_dict(orient='records'))
x_test = dv.transform(x_test.to_dict(orient='records')) 

# train model
solv = 'lbfgs'
C = 0.1
iter = 50

model = LogisticRegression(solver=solv, C=C, max_iter=iter, random_state=7)
model.fit(x_train, y_train)

# save model as pickle file
with open('model.bin', 'wb') as f_out:
    pickle.dump((dv,model), f_out)

print('Model was saved as model.bin')