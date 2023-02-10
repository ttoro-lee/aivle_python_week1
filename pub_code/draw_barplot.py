import pandas as pd
import numpy as np
import scipy.stats as spst
import matplotlib.pyplot as plt
import seaborn as sns

def draw_barplot(x:str, y:str, data:pd.DataFrame):

    sns.barplot(x=x, y=y, data=data)
    plt.grid()
    plt.show()

    test = list()

    if data[x].isna().sum():
        data = data.loc[data[x].notnull(), :]

    if len(data[x].unique()) > 2:
        for u in data[x].unique():
            test.append(data.loc[data[x] == u, y])
        return display(spst.f_oneway(*test))
    else:
        for u in data[x].unique():
            test.append(data.loc[data[x] == u, y])
        return display(spst.ttest_ind(*test))
        
    
