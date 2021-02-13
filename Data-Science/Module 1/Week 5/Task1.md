---
title: 'Task 1 :Predictive Modelling (Ensemble Modelling)'
metaTitle: 'Task 1'
metaDescription: 'Data Science course'
access: data
---

Moving forward with the next level to improve the model, you can have a look at some ensemble modeling methods. Ensemble models are typically Machine Learning models that combine or take a weighted (average/majority) vote of the predictions of each of the individual base model estimators that have been built using supervised methods of their own. 

The ensemble is expected to generalize better over underlying data, be more robust, and make superior predictions as compared to each individual base model. Ensemble models can be categorized under two major families.

### Bagging methods

The term bagging stands for bootstrap aggregating, where the ensemble model tries to improve prediction accuracy by combining predictions of individual base models trained over randomly generated training samples. At any instance, an average of all  predictions from the individual estimators is taken for the ensemble model to make its final prediction. Random sampling tries to reduce model variance, reduce overfitting, and boost prediction accuracy. 

Examples include random forests.

### Boosting methods

In contrast to bagging methods, which operate on the principle of combining or averaging, in boosting methods, you build the ensemble model incrementally by training each base model estimator sequentially. Training Each model involves putting special emphasis on learning the instances which it previously misclassified.

The idea is to combine several weak base learners to form a
powerful ensemble. Weak learners are trained sequentially over multiple iterations of the training data with weight modifications inserted at each retrain phase. At each re-training of a weak base learner, higher weights are assigned to those training instances which were misclassified previously. Thus, these methods try to focus on
training instances which it wrongly predicted in the previous training sequence.

Boosted models are ***prone to over-fitting*** so one should be  careful. Examples include Gradient Boosting, AdaBoost, and the  popular XGBoost.

[Ensemble methods: bagging, boosting and stacking](https://towardsdatascience.com/ensemble-methods-bagging-boosting-and-stacking-c9214a10a205)

Building a model using random forests, a popular bagging method would be a nice idea to explore the ensemble techniques.

In the random forest model, each base learner is a decision tree model trained on a bootstrap sample of the training data.

Besides this, when you want to split a decision node in the tree, the split is chosen from a random subset of all the features instead of taking the best split from all the features. 

Due to the introduction of this randomness,bias increases and when you average the result from all the trees in the forest, the overall variance decreases, giving a robust ensemble model which generalizes well. RandomForestClassifier from scikit-learn averages the probabilistic prediction from all the trees in the forest for the final
prediction instead of taking the actual prediction votes and then averaging it.

[More on Random Forest](https://towardsdatascience.com/understanding-random-forest-58381e0602d2)

```
from sklearn.ensemble import RandomForestClassifier
# train the model
wqp_rf = RandomForestClassifier()
wqp_rf.fit(wqp_train_SX, wqp_train_y)
# predict and evaluate performance
wqp_rf_predictions = wqp_rf.predict(wqp_test_SX)

print(classification_report(wqp_test_y,wqp_rf_predictions, target_names=wqp_label_names))
```

```
              precision    recall  f1-score   support

         low       0.94      0.28      0.43        54
      medium       0.78      0.71      0.74       718
        high       0.81      0.88      0.84      1178

    accuracy                           0.80      1950
   macro avg       0.84      0.62      0.67      1950
weighted avg       0.80      0.80      0.79      1950
```

The model prediction results on the test dataset depict an overall F1 Score and model accuracy of approximately 79%. This is definitely an improvement of 6% from what you obtained with just decision trees proving that ***ensemble learning is working better***.

The above classification report looks a bit weird (check **support**, in case you do not get it, please discuss with your mentor).

***Next, try other algorithms like KNN, SVM similarly for Wine Quality Prediction like you did for Wine Type prediction.***

## Interesting Reads

[scikit-learn-hacks-tips-tricks](https://www.analyticsvidhya.com/blog/2020/05/7-scikit-learn-hacks-tips-tricks/)

## Resources

[official doc scikit-learn](https://scikit-learn.org/stable/)
