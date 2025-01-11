import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, roc_auc_score
import seaborn as sns

df = pd.read_csv("C:/Users/sonam/Downloads/Expanded_data_with_more_features.csv")
df.info()

