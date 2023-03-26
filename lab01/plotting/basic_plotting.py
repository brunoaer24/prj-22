import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os
import seaborn as sns
from model.poly_model import create_poly_model,get_prediction,get_coef,get_r2,get_label

def basic_plot(
        data,
        x_name:str,
        y_names:list,
        deg:int=1
):
    

    data = data[[x_name,*y_names]]

    data = data.dropna()

    fig, ax = plt.subplots()
    y_name = '_'.join(y_names)
    for target in y_names:
        data = data.sort_values(by=x_name)
        x = data[x_name]
        y = data[target]

        plt.plot(
            x,
            y,
            '*',
            label= target
        )
        model = create_poly_model(data,x_name,y_name,deg=deg)
        # y = ax + b
        
        coefs = get_coef(model)

        y_predict = get_prediction(x,model)

        score = get_r2(model,data,x_name,y_name)

        label = get_label(coefs,deg,score)

        plt.plot(x,y_predict,'-',label=label)


    plt.title(f"{x_name} vs {y_name}")
    plt.grid(True)
    plt.xlabel(x_name)
    plt.ylabel(f"{y_name}".replace('[','').replace(']',''))
    plt.legend()

    #save
    path = 'data'
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    plt.savefig(f'data/{x_name}_vs_{y_name}.png')




def plot_correlation(
        data:pd.DataFrame,
) -> pd.DataFrame:
    def magnify():
        return [dict(selector="th",
                    props=[("font-size", "4pt")]),
                dict(selector="td",
                    props=[('padding', "0em 0em")]),
                dict(selector="th:hover",
                    props=[("font-size", "12pt")]),
                dict(selector="tr:hover td:hover",
                    props=[('max-width', '200px'),
                            ('font-size', '12pt')])
    ]

    cmap = cmap=sns.diverging_palette(5, 250, as_cmap=True)
    bigdf = data.corr()
    bigdf = bigdf.style.background_gradient(cmap, axis=1)\
        .set_properties(**{'max-width': '80px', 'font-size': '1pt'})\
        .set_caption("Correlation Matrix")\
        .format(precision=2)\
        .set_table_styles(magnify())
    
    return bigdf


