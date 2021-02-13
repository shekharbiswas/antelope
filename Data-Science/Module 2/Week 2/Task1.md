# Time Series

You will spend the first half of the week understanding the data and knowing timeseries. For that you can discuss with me and finally, send it to mentor's email address (Ask your mentor for that).

**As you might have noticed, this project encourages you to do self-learning to a larger extent and as you progress, you will do it .**

Advice is : **DO NOT just follow the task descriptions. Spend some time of the day asking yourself if there was no plans provided to you, how would you have approached the part of the project ? Sometimes, your own way of doing will be better than any guidances provided.** 

<br>

**You can discuss with your mentor with all sorts of help you require to reach to the point of indepenent project handling.**



[All the basics you need to know about time series](https://www.machinelearningplus.com/time-series/time-series-analysis-python/)


Once you have gone through the basic [Timeseries handling in Python](https://pandas.pydata.org/docs/user_guide/timeseries.html), you would be able to create some detailed analysis (daywise, monthwise, particular day, time etc.).

For example,

<br>
<p align="center">
  <img  width="500" height="350" src="../images/jan_2011.JPG">
</p>
<br>


<br>
<p align="center">
  <img  width="500" height="350" src="../images/28aug2012.JPG">
</p>
<br>




Last project, you were direcly provided with the exact dataset (For example, Price & Reviews DataSet). This time, it is your task to look for relevant data on the [client website :Capital bikeshare](https://www.capitalbikeshare.com/). 


The have a section on the website with the below details:

'
**Trip History Data**

Each quarter, we publish downloadable files of Capital Bikeshare trip data. The data includes:

Duration – Duration of trip
Start Date – Includes start date and time
End Date – Includes end date and time
Start Station – Includes starting station name and number
End Station – Includes ending station name and number
Bike Number – Includes ID number of bike used for the trip
Member Type – Indicates whether user was a "registered" member (Annual Member, 30-Day Member or Day Key Member) or a "casual" rider (Single Trip, 24-Hour Pass, 3-Day Pass or 5-Day Pass) 
'

Can you make use of these informations to enrich your findings / forecast.

#### Hint:

***How cool it would be to exactly know the start and end station. How about plotting them on Google maps to create a biking traffic pattern / routes. It requires some efforts. (Challenge yourself)***

One option to [create google map without any programming](https://support.google.com/mymaps/answer/3024454?hl=en&amp%3Bref_topic=3188329) and then embed that into your notebook. 


```
%%html

<iframe src="https://www.google.com/maps/d/u/0/embed?mid=1xwOR-Mjborq-vmpGz-JfhucdlDlAmo1c" width="640" height="480"></iframe>

```

If its still not clear, look at the video which explains the steps.

[![Create google maps without API](https://img.youtube.com/vi/uPA5dM9Ot1Y/0.jpg)](https://www.youtube.com/watch?v=uPA5dM9Ot1Y
)

<br>


***Can you think of applying K-means clustering algorithms for bicycle stations. This requires first understanding Clustering which is a type of Unsupervised Learning.***



[Spatiotemporal Clustering Analysis of Bicycle Sharing System with Data Mining Approach](../Resources/information-10-00163.pdf)


[One of the most widely used clustering techniques is 'K-Means Clustering'](https://realpython.com/k-means-clustering-python/)


***Knowing busy and free stations and more. (you are encouraged to come up with more ideas).***


For example, top 10 start stations by volume of traffic. (number of occurances)


```
data2011['Start station'].value_counts()[0:10].plot(kind = 'bar');

```

<br>
<p align="center">
  <img  width="500" height="350" src="../images/top10_start.JPG">
</p>
<br>


## Advanced Students

You can also obtain the corresponding weather information and holiday schedules from here:

[Weather Information](http://www.freemeteo.com)
[Holiday Schedule](http://dchr.dc.gov/page/holiday-schedule)

This is **not mandatory** for you to be able to create the hourly and daily datasets for recent years. However, this is a nice challenge which you will face in your day-to-day job. Also, you probably heard a lot about [how much time analysts spend to gather the appropriate data even before they start analysis.](https://www.forbes.com/sites/gilpress/2016/03/23/data-preparation-most-time-consuming-least-enjoyable-data-science-task-survey-says/#679a8b946f63)


***Can you think of including demographics data (for example, population, average salary etc.) for a particular location.***









## Resources

[Timeseries handling in Python](https://pandas.pydata.org/docs/user_guide/timeseries.html)

[Spoiler: Do not open](https://www.visualization.bike/capital/overview/2019/)

