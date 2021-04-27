import pandas as pd
import numpy as np


import warnings
warnings.filterwarnings('ignore')

# Import the heart attack data
heart_df = pd.read_csv('../Resources/Files/heart.csv')

cat_cols = ['sex','cp','fbs','restecg','exng','slp','caa','thall']
con_cols = ['age','trtbps','chol','thalachh','oldpeak']
target_col = ['output']