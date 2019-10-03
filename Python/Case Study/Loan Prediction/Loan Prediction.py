# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 11:52:02 2017

@author: 10642546
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("C:/Users/10642546/Desktop/Chetan/Python/Case Study/Loan Prediction/train.csv")

df.head(n=10)
df.describe()

df['Property_Area'].value_counts()