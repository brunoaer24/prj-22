import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


def  create_linear_model(
    data:pd.DataFrame,
    x_name:str,
    y_name:str
):
    regressor = linear_model.LinearRegression()

    x = data[x_name].to_numpy().reshape(-1, 1)
    y = data[y_name].to_numpy()
    regressor.fit(x, y)
    return regressor

def get_prediction(x,model):
    x = x.to_numpy().reshape(-1, 1)
    y = model.predict(x)
    return y


def get_coef(model):
    a = model.coef_[0]
    b = model.intercept_
    return a,b

def get_r2(model,data,x_name,y_name):
    x=data[x_name].to_numpy().reshape(-1, 1)
    y=data[y_name]
    return model.score(x,y)
    


