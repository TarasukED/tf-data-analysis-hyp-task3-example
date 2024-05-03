import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1742143281 # Ваш chat ID, не меняйте название переменной

def solution(control_transactions, test_transactions) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    stat, p_value = ttest_ind(test_transactions, control_transactions, alternative='greater')
    alpha = 0.09
    return p_value < alpha 
