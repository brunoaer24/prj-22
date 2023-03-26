import numpy as np
import pandas as pd
import sklearn 
from sklearn.metrics import mean_squared_error, r2_score


def  create_poly_model(
    data:pd.DataFrame,
    x_name:str,
    y_name:str,
    deg:int
):
    x = data[x_name].to_numpy()
    y = data[y_name].to_numpy()

    regressor = np.polyfit(x,y,deg)

    return regressor

def get_prediction(x,model):
    x = x.to_numpy()
    yn = np.poly1d(model)
    return yn(x)


def get_coef(model):
    return model

def get_r2(model,data,x_name,y_name):
    x=data[x_name].to_numpy()
    y=data[y_name]
    yn = np.poly1d(model)

    return r2_score(y,yn(x))

def get_label(coefs,deg,score):
    string = '+'.join([f'{round(coefs[-i+deg],2)} x^{i}' for i in range(deg,0,-1)])
    string =  f"y = {string} + {round(coefs[-1],2)}, r2 = {round(score,2)}" 
    return string
    


