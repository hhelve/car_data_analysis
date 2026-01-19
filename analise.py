import xgboost as xgb
import pandas as pd
import sklearn
import numpy as np
from sklearn.metrics import mean_squared_error

df = pd.read_csv("carros_teste.csv")

y = np.log1p(df["preco"])
X = df.drop("preco", axis=1)

X = pd.get_dummies(X, columns=["modelo"])

train_columns = X.columns

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size=0.2
)

model = xgb.XGBRegressor(
    n_estimators=2500,
    learning_rate=0.02,
    objective="reg:squarederror",
    max_depth=2,
    min_child_weight=4,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="mae",
    random_state=42,
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(sklearn.metrics.mean_squared_error(y_test, y_pred))
mae = mean_squared_error(y_test, y_pred)
print(mae)
