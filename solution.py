import pandas as pd
import numpy as np

from scipy.stats import cramervonmises_2samp

chat_id =  689327667# Ваш chat ID, не меняйте название переменной


SGN_LVL = 0.01

def solution(x: np.array, y: np.array) -> bool:
    pval = cramervonmises_2samp(x,y).pvalue
    if pval < SGN_LVL:
        return True
    # true: выборки не равны
    return False
