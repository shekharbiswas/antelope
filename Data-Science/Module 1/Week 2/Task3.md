---
title: 'Project 1 :Wine Quality Prediction'
metaTitle: 'Task 4'
metaDescription: 'Data Science course'
access: data
---

![wine_image](../images/wine.jpg)

*"Age appears best in four things: old wood to burn, old wine to drink, old friends to trust, and old authors to read."* - Francis Bacon  

**Congratulations** for finishing all the preliminary *Python & Statistics challenges*. You have already mastered a few tools which are your day-to-day weapons for any kind of Analysis. Therefore, We welcome you on-board as ***Data Analyst (Intern)*** in the department of **Analytics & Research** where you will be reporting to Mark & Jennifer throughout this project.


Mark has already sent an email where he has explained the objective of the project. As an intern, your task will be to follow the guidelines and reply to Mark's email as you progress with the project. You would be provided with all the guidance time to time in the beginning, however, you have to research and learn as much as possible.



## Understanding Data

Before you start loading in the data, it might be a good idea to check how much you really know about wine and its composition. 

Most of you probably know that there are, in general, two very popular types of wine: \
[Red wine](https://en.wikipedia.org/wiki/Red_wine) \
[White wine](https://en.wikipedia.org/wiki/White_wine)

There are many other varieties, however, as per the business, the analysis will be limited to these two varieties.

There are 3 data files (look at **Data Source** section at the bottom)

- The file named **winequality-red.csv** contains the dataset pertaining to 1599 records of red wine samples.

- The file named **winequality-white.csv** contains the dataset pertaining to 4898 records of white wine samples.

- The file named **winequality.names** consists of detailed information and the data dictionary pertaining to the datasets.

Knowing this is one thing, but if you want to analyze this data, you will need to know just a little bit more.

The dataset contains physicochemical and sensory variables which require a bit more understanding.

- Fixed acidity: acids are major wine properties and contribute greatly to the wine’s taste. Usually, the total acidity is divided into two groups: the volatile acids and the nonvolatile or fixed acids. Among the fixed acids that you can find in wines are the following: tartaric, malic, citric, and succinic. This variable is expressed in 
***g(tartaricacid)/dm3*** in the data sets.

- Volatile acidity: the volatile acidity is basically the process of wine turning into vinegar. In the U.S, the legal limits of Volatile Acidity are 1.2 g/L for red table wine and 1.1 g/L for white table wine. In these data sets, the volatile acidity is expressed in ***g(aceticacid)/dm3***.

- Citric acid is one of the fixed acids that you’ll find in wines. It’s expressed in g/dm3 in the two data sets.
Residual sugar typically refers to the sugar remaining after fermentation stops, or is stopped. It’s expressed in ***g/dm3*** in the red and white data.

- Chlorides can be a significant contributor to saltiness in wine. Here, you’ll see that it’s expressed in ***g(sodiumchloride)/dm3***.

- Free sulfur dioxide: the part of the sulfur dioxide that is added to a wine and that is lost into it is said to be bound, while the active part is said to be free. The winemaker will always try to get the highest proportion of free sulfur to bind. This variable is expressed in ***mg/dm3*** in the data.

- Total sulfur dioxide is the sum of the bound and the free sulfur dioxide (SO2). Here, it’s expressed in mg/dm3. There are legal limits for sulfur levels in wines: in the EU, red wines can only have 160mg/L, while white and rose wines can have about 210mg/L. Sweet wines are allowed to have 400mg/L. For the US, the legal limits are set at 350mg/L, and for Australia, this is 250mg/L.

- Density is generally used as a measure of the conversion of sugar to alcohol. Here, it’s expressed in ***g/cm3***.

- pH or the potential of hydrogen is a numeric scale to specify the acidity or basicity the wine. As you might know, solutions with a pH less than 7 are acidic, while solutions with a pH greater than 7 are basic. With a pH of 7, pure water is neutral. Most wines have a pH between 2.9 and 3.9 and are therefore acidic.

- Sulfates are to wine as gluten is to food. You might already know sulfites from the headaches that they can cause. They are a regular part of winemaking around the world and are considered necessary. In this case, they are expressed in ***g(potassiumsulphate)/dm3***.

- Alcohol: wine is an alcoholic beverage, and as you know, the percentage of alcohol can vary from wine to wine. It shouldn’t be surprised that this variable is included in the data sets, where it’s expressed in % vol.

- Quality: wine experts graded the wine quality between 0 (very bad) and 10 (very excellent). The eventual number is the median of at least three evaluations made by those same wine experts. Some analysts might combine these levels to **Low, Medium & High-Quality* wines. 

## Load the Data

Use the [Pandas read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) function to read the data.

Example-

The below code tries to read the red wine file into a dataframe called 'red-wine'

```
red_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv')
```

If you get any error / unusual data format, please check **sep** argument.


**DO NOT** forget to load the necessary libraries.


## Data Exploration

Besides trying to predict the quality, you can choose to explore how the composition of Red wine and White wine differ.
In simple words, 

**Can you tell whether a wine is Red or White by looking at its composition.**

For the same, the data frame should be combined to a single data frame with a column **'Wine Type'**. Also, create 3 quality labels : low, medium & high for ease of analysis.


```
//  create a new variable 'wine_type'

red_wine['wine_type'] = 'red'


// bucket wine quality scores into qualitative quality labels

red_wine['quality_label'] = red_wine['quality'].apply(lambda value: 'low'
if value <= 5 else 'medium'
if value <= 7 else 'high')

red_wine['quality_label'] = pd.Categorical(red_wine['quality_label'],
categories=['low', 'medium', 'high'])

```

**Do the same with White Wine**


Then combine the two datasets into one - ***wines***

```

wines = pd.concat([red_wine, white_wine])

// re-shuffle records just to randomize data points

wines = wines.sample(frac=1, random_state=42).reset_index(drop=True)


```

The original dataset has been modified to contain two new attributes :

- wine_type: Since originally there were two datasets for red and white wine and after combining them the dataset contains this extra column to identify wine type.\
One of the predictive models can be built to predict the type of wine by looking at the other 12 attributes.

- quality_label: This is a derived attribute from the quality attribute contain three labels - **low**, **medium**, and **high**.

Wines with a quality score of 3, 4, and 5 are **low quality**;\
score of 6 and 7 are **medium quality**;\
and score of 8 and 9 are **high quality** wines. 




## Data Source

[Download files from UCI repository](https://archive.ics.uci.edu/ml/datasets/wine+quality)




## Resources

* The below dataset contains the pricing and reviews of wines which you will use in the end of the project to estimate the wine price based on its quality. However, you can think of other features which might be interesting to analyze for this project.

Here is the [dataset  containing wine reviews](https://drive.google.com/file/d/1OCndQ96ffaAQhsOrDh83iqymDwPXrVDK/view?usp=sharing).

* [Modeling Wine Preferences from Physicochemical Properties](http://www3.dsi.uminho.pt/pcortez/wine5.pdf)
