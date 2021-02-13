# Exploration & Modelling

## Formulate some hypothesis and try to evaluate

***Here are some of the hypothesis which could influence the demand of bikes:***

Hourly trend: Most of the businessed have rush hours and weak hours. It should not be an exception for bike rentals as well.

Daily Trend: Registered users vs casual users.

Rain: The demand of bikes might be changed on a rainy day as compared to a sunny day. Similarly, people prefer to go out in less humid days.

Temperature: In warm countries, temperature generally keep people inside. You have to check Washington DC's tempearture for making any guess.

Business model: Businesses often rely on registred customers more than casual users. There might be some interesting insights that can strengthen this assumption.


## Create some proofs

The dataset after preprocessing (which you performed in the previous step) is ready for some visual inspection. 

You have already performed many visualisation techniques in previous project. This time its your job to think what kind of plots would be interesting for a Bike rental company.

For example, 

```
import seaborn as sns

sns.set(rc={'figure.figsize':(11,8)})

sns.set_context("paper", font_scale=1, rc={"lines.linewidth": 2.5})
#sns.set(style="ticks", context="talk")
#plt.style.use("dark_background")
sns.set_style("dark")

#fig, ax = plt.subplots()
ax = sns.pointplot(data = hdf[['hour','total_count','season']], x = 'hour', y = 'total_count',
              scale = 0.2, hue = 'season');

plt.setp(ax.get_legend().get_texts(), fontsize='15') # for legend text
plt.setp(ax.get_legend().get_title(), fontsize='16') # for legend title

ax.set(title = 'Season wise hourly distribution of bike rentals',ylabel= 'mean(total_count)');

```



<p align="center">
  <img  width="550" height="350" src="../images/seasons.JPG">
</p>


**If you observe that people are using more bikes in Winter, you have to question about the quality of the data.**

[Why Data Quality matters ?](https://www.lotame.com/why-is-data-quality-important/)

Similarly, below plots can be created:

<p align="center">
  <img  width="550" height="350" src="../images/holiday.JPG">
</p>

Monthly average total count for 12 months.

<br>

<p align="center">
  <img  width="550" height="350" src="../images/monthly.JPG">
</p>

<br>

The below plot requires creation new feature 'is_weekend'
<br>
<p align="center">
  <img  width="550" height="350" src="../images/weekend.JPG">
</p>

<br>
<p align="center">
  <img  width="550" height="350" src="../images/temp.JPG">
</p>
<br>


***Explore more on these kind of visualisations and come up with 5 or more insights.***

<br>

## Outlier Analysis

Before you start modelling, you need to understand if there is bad data which is not good for model generalisation. These are called 'outliers'.

According to experts,

'You should proceed with caution when considering to remove observations from the data. In many cases, there is a valid reason for these observations to be outliers and that is what the researcher should be studying. Why was this an outlier?

Another issue with outliers is where to draw the line. It may not be clear where the outlier behavior starts. There are some people who arbitrarily eliminate a percentage at the tails (e.g. 5%), which makes no sense whatsoever.'

Generally people suggest running your models with the outlier, and without, comparing the results and document any decision to remove or transform the outlier.



According to Jim Frost,

***An outlier is an unusually large or small observation. Outliers can have a disproportionate effect on statistical results, such as the mean, which can result in misleading interpretations.***


***For example, a data set includes the values: 1, 2, 3, and 34. The mean value, 10, which is higher than the majority of the data (1, 2, 3), is greatly affected by the extreme data point, 34. In this case, the mean value makes it seem that the data values are higher than they really are. You should investigate outliers because they can provide useful information about your data or process. Often, it is easiest to identify outliers by graphing the data.***


### Skewed data

Skewed data are not equally distributed on both sides of the distribution—it is not a symmetrical distribution. Use a histogram to easily see whether your data are skewed.

As you have learnt from statistics, you can describe skewed data as either right skewed or left skewed.Data are skewed right when most of the data are on the left side of the graph and the long skinny tail extends to the right.


```
sns.distplot(hdf.total_count); 
```
<br>
<p align="center">
  <img  width="550" height="350" src="../images/distplot_skewed.JPG">
</p>
<br>


The distribution plot of the count values reveals that the count values are right skewed. You can use the median and interquartile range (IQR) to identify and remove outliers from the data. 

[What Is the Interquartile Range Rule?](https://www.thoughtco.com/what-is-the-interquartile-range-rule-3126244#:~:text=Using%20the%20Interquartile%20Rule%20to%20Find%20Outliers&text=Multiply%20the%20interquartile%20range%20(IQR,IQR)%20from%20the%20first%20quartile.)


sample example,

```
q1 = hdf.cnt.quantile(0.25)
q3 = hdf.cnt.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
hdf = hdf.loc[(hdf.cnt >= lower_bound) & (hdf.cnt <= upper_bound)]
```


(An alternative approach would be the transformation of the target values to a normal distribution and using mean and standard deviation.)

```
hdf = hdf[np.abs(hdf["total_count"]-hdf["total_count"].mean()) <= 3*hdf["total_count"].std()]
```

(**Reminder**: The code snippets are just for giving you idea. You are encouraged to write the codes in your own way.)

***Also check out other features for outliers. Please consider using box plots to visualise outliers in such cases.***

Many algorithms are robust to outliers. As per one practising Data Analyst (source: Quora),

*As far as classifiers go, many classification algorithms are somewhat robust to outliers. Algorithms that create linear boundaries (e.g. LDA) are somewhat robust but will be biased if data are not linearly separable. Algorithms that use ensemble methods (e.g. RF) do quite well at least on training data. Tree models (again RF) do well in the presence of outliers.*

*Tuning model hyper parameters plays a huge role in classifiers. Regression wise, I focus on using robust models. The tradeoff is speed. I don’t mind that at training time.*

*One can use the rule of thumb "if the outlier is an error, we remove it, if not we think really hard on the implications of it in the final data product."* 

## Modelling

* Split the datasets into train and test.

* Select important features based on co-relation matrix.

* Check for categorical variables and apply one hot encoding.

[why one-hot-encode data in machine-learning](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/)

* [Look if any preprocessing is required](https://scikit-learn.org/stable/modules/preprocessing.html#)

*You apply same pre-processing on both test and train set keeping the values to be precited (here, total count) untouched*

Ex-

[MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html) might work better than Standard scaler sometimes.

[Artcle](https://benalexkeen.com/feature-scaling-with-scikit-learn/#:~:text=It%20essentially%20shrinks%20the%20range,min%2Dmax%20scaler%20works%20better.)


* One of the simplest regression analysis techniques is [Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html). 


Revise the [concept of cross_val_score](https://towardsdatascience.com/cross-validation-explained-evaluating-estimator-performance-e51e5430ff85)

Apply and check cross_val_score on the data to check the best value of 'no of folds'. Often, analysts plot a graph for this which look like below:


<br>
<p align="center">
  <img  width="850" height="350" src="../images/r2_cross_val.JPG">
</p>
<br>

You can choose any other parameter on Y-axis.

If the r-squared or the coefficient of determination is low (lets say X) on an average for 10-fold cross validation, this will point to the fact that the predictor is only able to explain X% of the variance in the target variable.

You are encouraged to plot and confirm [the normality of data](https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/). It is important to understand if the data can be modeled by a linear model or not.


As per experts, 
A standard regression model assumes that the errors are normal, and that all predictors are fixed, which means that the response variable is also assumed to be normal for the inferential procedures in regression analysis. 

The fit does not require normality.

If y appears to be non-normal, one would better try to transform it to be approximately normal.

This is being left as an experiment for you to explore.

<br>


```
X = train
y= y.total_count.values.reshape(-1,1)

lin_reg = linear_model.LinearRegression()
```

One simple way of proceeding would be call the fit() function to build our linear regression model and then call the predict() function on the test dataset to get the predictions for evaluation. Also one has to
keep in mind the aspects of overfitting and reduce its affects and obtain a generalizable model. As discussed previously, cross validation is one method to keep overfitting in check.

You can use the k-fold cross validation (specifically 10-fold) as shown in the following snippet.

```
predicted = cross_val_predict(lin_reg, X, y, cv=10)

```

You can choose the value of CV from cross_val_score.

Tips:

[It is important not to confuse with cross_val_score and cross_val_predict.](https://stackoverflow.com/questions/43613443/difference-between-cross-val-score-and-cross-val-predict)


<br>

The below code explains how you can use multiple algorithms and compare their RMSE / RMSLE results:

[What’s the Difference Between RMSE and RMSLE?](https://medium.com/analytics-vidhya/root-mean-square-log-error-rmse-vs-rmlse-935c6cc1802a)


You can also make it a function and pass arguments accordingly.

```
models=[RandomForestRegressor(max_features= 'auto', n_estimators= 100, n_jobs= -1),AdaBoostRegressor(),BaggingRegressor(),SVR(),KNeighborsRegressor()]
model_names=['RandomForestRegressor','AdaBoostRegressor','BaggingRegressor','SVR','KNeighborsRegressor']
rmsle=[]
rmse = []
d1= {}
d2 = {} 
for model in range (len(models)):
    clf=models[model]
    clf.fit(x_train,y_train)
    test_pred=clf.predict(x_test)
    rmsle.append(np.sqrt(mean_squared_log_error(test_pred,y_test)))
    rmse.append(np.sqrt(mean_squared_error(test_pred,y_test, squared=False)))

d1={'Modelling Algo':model_names,'RMSLE':rmsle}   


d2={'Modelling Algo':model_names,'RMSE':rmse}   



rmsle_frame=pd.DataFrame(d1)
#rmsle_frame

rmse_frame=pd.DataFrame(d2)
#rmse_frame


sns.catplot(y='Modelling Algo',x='RMSLE',data=rmsle_frame,kind='bar',height=5,aspect=2);

```

<br>
<p align="center">
  <img  width="850" height="400" src="../images/rmsle.JPG">
</p>
<br>


```
sns.catplot(y='Modelling Algo',x='RMSE',data=rmse_frame,kind='bar',height=5,aspect=2);

```
<br>
<p align="center">
  <img  width="850" height="400" src="../images/rmse.JPG">
</p>
<br>

Hyperparameters are the knobs and controls we set with an aim to optimize the model’s performance on unseen data. Hyperparameters help you achieve objectives of avoiding overfitting and so on. 

[hyperparameter-tuning-random-forest](https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74)

**You are advised to use [Hyper parameter tuning](https://scikit-learn.org/stable/modules/grid_search.html#) for these models to get the best results.**

<br>









## Resources

* [Making plots with seaborn](https://seaborn.pydata.org/examples/index.html)
