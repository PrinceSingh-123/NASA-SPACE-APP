import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

train_df = pd.read_csv('data.csv')

# print(train_df.info)

predictors = train_df[['BF1']]
target = train_df['BGSM']

X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.3)

lr = LinearRegression()

lr.fit(X_train, y_train)


y_pred = lr.predict(X_test)

_preds_df = pd.DataFrame(dict(observed=y_test, predicted=y_pred))

_preds_df.head()

print('Score: {}'.format(lr.score(X_test, y_test)))

print('MSE: {}'.format(mean_squared_error(y_test, y_pred)))