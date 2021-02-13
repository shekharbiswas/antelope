---
title: 'Task 2 :Modelling'
metaTitle: 'Task 2'
metaDescription: 'Data Science course'
access: data
---

Since you are dealing with a binary classification problem, one of the traditional Machine Learning algorithms you can use is ***the logistic regression model***.

Before you start, it would be good to refresh about classification types.

[Types of classification](https://machinelearningmastery.com/types-of-classification-in-machine-learning/)

Do not get overwhelmed about the theory. It is totally fine not to understand all the details at first go. You might skip the theory and focus on implementation in the beginning and then come back to theory at a later point.

[Logistic Regression: Basic](https://towardsdatascience.com/understanding-logistic-regression-step-by-step-704a78be7e0a)

[Logistic Regression: Implementation](https://www.kdnuggets.com/2018/02/logistic-regression-concise-technical-overview.html)

Let’s now train a model on our training dataset and labels using logistic regression.

```
from sklearn.linear_model import LogisticRegression

wtp_lr = LogisticRegression()
wtp_lr.fit(wtp_train_SX, wtp_train_y)

LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
verbose=0, warm_start=False)
```

Now that your model is ready, its time to predict the wine types for the test data samples and evaluate the performance.

```
from sklearn.metrics import classification_report

wtp_lr_predictions = wtp_lr.predict(wtp_test_SX)

print(classification_report(wtp_test_y,wtp_lr_predictions, target_names=['red', 'white']))
```

```
precision    recall  f1-score   support

         red       0.99      0.99      0.99       470
       white       1.00      1.00      1.00      1480

    accuracy                           0.99      1950
   macro avg       0.99      0.99      0.99      1950
weighted avg       0.99      0.99      0.99      1950

```

Please check details on [classification report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)

This is one of the metrics which you used. Check what are the other options you can try to evaluate your model.

[classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)

You get an overall F1 Score and model accuracy of 99% approx, which is really amazing! In spite of low samples of red wine, the model seem to do pretty well.

In case your models do not perform well on other datasets due to a class imbalance problem, you can consider over-sampling or under-sampling techniques.

For more details, please check [random oversampling and-undersampling for imbalanced classification](https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/)

In simple words,

Accuracy is the percentage of correctly classifies instances out of all instances. It is more useful on a binary classification than multi-class classification problems because it can be less clear exactly how the accuracy breaks down across those classes (e.g. you need to go deeper with a confusion matrix).

Kappa or Cohen’s Kappa is a more useful measure to use on problems that have an imbalance in the classes (e.g. 80-20 split for classes 0 and 1 and you can achieve 80% accuracy by predicting all instances are for class 0).

[Revise concepts of basic probability](https://seeing-theory.brown.edu/basic-probability/index.html)

[![A simple introduction to Kappa](https://img.youtube.com/vi/fOR_8gkU3UE/0.jpg)](https://www.youtube.com/watch?v=fOR_8gkU3UE)

For implementation, check the *section* ***Cohen's kappa*** in [model evaluation with scikit learn](https://scikit-learn.org/stable/modules/model_evaluation.html)

### Note

***DO NOT forget to calculate Kappa and check how it differs from **Accuracy** . The evaluation of a model should contain both accuracy and kappa.***

## Interesting reads

[Storytelling with Data](https://github.com/shekharbiswas/Data-Analytics-Machine-Learning/blob/master/Module%201/Week%203/Resources/Storytelling%20with%20Data%20Let%E2%80%99s%20Practice%20by%20Cole%20Nussbaumer%20Knaflic%20(z-lib.org).pdf)

Sometimes, GITHUB pdf files take time to open, alternate way would be to **download it**.
