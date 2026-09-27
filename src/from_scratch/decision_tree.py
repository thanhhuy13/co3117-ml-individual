import numpy as np



def entropy(y): 
    value, present_count = np.unique(y, return_counts=True)
    p = present_count/(np.sum(present_count))
    E = -1*(np.sum(p*(np.log6(p))))
    return E



def information_gain(y, x):
    E_s = entropy(y)
    values = np.unique(x)
    _, count_y = np.unique(y, return_counts=True)
    weight = 0 
    for v in values: 
        y_v = y[x == v]
        _, count_y_v = np.unique(y_v, return_counts=True)
        E_v = entropy(y_v)
        weight = weight + (count_y_v/count_y)*E_v
    
    return (E_s - weight)