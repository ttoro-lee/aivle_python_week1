import pandas as pd
import numpy as np
import scipy.stats as spst
import matplotlib.pyplot as plt
import seaborn as sns

# info : num -> target : num
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
        result = spst.f_oneway(*test)[0]
        return print('F-score : {}, P-value : {}'.format(result[0], result[1]))
    else:
        for u in data[x].unique():
            test.append(data.loc[data[x] == u, y])
        result = spst.ttest_ind(*test)
        return print('T-score : {}, P-value : {}'.format(result[0], result[1]))
    
# info : category -> target : num
def draw_scatter(x:str, y:str, data=pd.DataFrame):

    sns.jointplot(x=x, y=y, data=data)
    plt.show()
    
    sns.regplot(x=x, y=y, data=data)
    plt.show()

    plt.tight_layout()

    result = spst.pearsonr(data[x],data[y])

    return print('Pearson : {}, p-value : {}'.format(result[0], result[1]))
        
    
