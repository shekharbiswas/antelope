import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')

#import model_evaluation_utils as meu
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import GridSearchCV
#import imblearn
import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor
from scipy import stats
import pickle

df = pd.read_csv('hdf_denorm.csv')

## preprocess
#df.rename(columns={'instant':'rec_id',
#'dteday':'datetime',
#'holiday':'is_holiday',
#'workingday':'is_workingday',
#'weathersit':'weather_condition',
#'hum':'humidity',
#'atemp':'felt_temperature',
#'mnth':'month',
#'cnt':'total_count',
#'hr':'hour',
#'yr':'year'},inplace=True)

df = df[['hour','is_holiday', 'weekday','felt_temperature_actual','humidity_actual','users_total']]
#df.is_holiday = df.is_holiday.astype('category')
#df.weekday = df.weekday.astype('category')
df = pd.get_dummies(df)

## modelling
x = df.drop(columns = ['users_total'])
y = df['users_total']

ada = AdaBoostRegressor()
ada.fit(x,y)
pickle.dump(ada, open('my_model.pkl','wb'))

