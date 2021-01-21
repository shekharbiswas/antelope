import string
from lazypredict.Supervised import LazyClassifier, LazyRegressor
from sklearn.model_selection import train_test_split
from sklearn import datasets
a = list(string.ascii_uppercase)

for company in 'HAL':
     print(a[a.index(company) + 1])