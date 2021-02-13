---
title: 'Task 2 :Final Presentation'
metaTitle: 'Task 2'
metaDescription: 'Data Science course'
access: data
---

# Final Presentation

**BlueBerry Winery** has a primary goal of selling the wines at proper price based on its quality. So, the report to the client might include the estimated price along with the assessment of quality for a sample of wine prior to bottling.  

You do not have any price information on the current dataset. **Data analysts often search for other datasets to enrich their research and strengthen the analytics outcome.** However,this being your first project, you are provided with the [dataset  containing wine reviews](https://drive.google.com/file/d/1OCndQ96ffaAQhsOrDh83iqymDwPXrVDK/view?usp=sharing).

This dataset requires few modifications before one can really use it.

[To refresh you Pandas skills](https://dsft.code-data-ai.com/pandas-dataframe/)


[Revisit Statistics](https://www.statisticshowto.com/probability-and-statistics/percentiles-rank-range/)


### Steps to clean the data

- Filter 'Portugal' and 'Vinho Verde' region.

- Remove Price outliers (hint: Take price between 25 and 75 percentile).

- You can use this data set assuming price will increase with wine quality.

[No one likes a bad assumption](https://towardsdatascience.com/check-your-assumptions-about-your-data-20be250c143)

Cut rating into 7 levels or 3 levels based on the levels of wine quality you have used in the dataset. For each rating, check the price range (min_price, max_price) and mean_price/median_price.

[pandas cut function](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.cut.html)

- Next, you will obtain ***a dataframe with rating and price*** where rating is equivalent to quality of the product and price is a dependent variable.

[table_price_rating](../images/table_price_rating.JPG)

**Here bin can be treated equivalent to wine quality**

- Lastly, you would try to estimate the price of wines you have analysed and provide suggestions on 'Pricing'.

***You already know what are the basic guidelines for a presentation and also do not forget to come up with a storyline to convey your message to the CEO in the best possible way.***

*Generally, a data analytics presentation lasts for 12 - 15 minutes and consists of 6 - 12 slides.*
