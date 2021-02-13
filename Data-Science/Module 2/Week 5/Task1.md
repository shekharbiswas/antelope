# Analyze Product Sales 

Analysing only the products and not the sales data make the task of E-commerce data analysis incomplete in many ways. It is like having all the armours ready but never using it in battlefield.

<p align="center">
  <img  width="700" height="400" src="https://i2.wp.com/code-data-ai.com/wp-content/uploads/2020/03/1.jpeg?w=1240&ssl=1">
</p>


You loose most important KPIs of E-commerce if you can not include the sales informations in your analysis.

That is why you are supposed to analyse these sales informations and find out key insights from user behaviour. 

The sales dataset** contains the sales history (almost half a million records) for the period of almost an year for certain product categories.

Few things which came to my notice:

* **The dataset does not have proper 'Unit price' as it was corrupted and I would request your help to fix it with the help of products datasets.**

As you can see below:

<p align="center">
  <img  width="850" height="450" src="../images/unit_price.png">
</p>

<br>
<br>

That means you have to correct the Unit prices by checking the products datasets and putting the price from there into the sales datasets.
The products datasets also contains all the information like price, review counts, ratings etc.

<br>

* There is no segment like which product type the item belongs to.

For example, the first item **'Apple iPhone X, 256GB, Silver - Fully Unlocked....' belongs to category 'smartphone'.**

So adding this information would help us getting an important KPI : ***'Revenue by product category'.***

<br>
<br>

That is why apart from the sales data, I have requested Alan the products datasets for each of these product categories:

* DSLR cameras
* Smartphones
* Processors
* Monitors
* Mouse
* Keyboards

Please feel free to make use of them in this context.

There will be definitely more KPIs which you can think of while creating the SQL tables out of these datasets and analyzing it. The priority would be to solve all the business questions using SQL queries instead of Pandas dataframe commands. 


<br>

***To modify and include the missing informations in sales table, you have to use SQL Joins and ensure the number of record counts after each operation.***

<br>
<br>


To SUM UP, you should recieve the below 7 datasets:

* ***sales.csv***
* ***dslr.csv***
* ***smartphone.csv***
* ***processor.csv***
* ***monitor.csv***
* ***mouse.csv***
* ***keyboard.csv***

<br>
<br>


The sales data have below infomations:

**InvoiceNo:** A 8-digit integral number uniquely assigned to each transaction. If this code starts with letter 'C', it indicates a cancellation.

**StockCode:** A 5-digit integral number uniquely assigned to each distinct product.

**Description:** Product (item) name as mentioned on Amazon website.

**Quantity:** The quantities of each product (item) per transaction.

**InvoiceDate:**  the day and time when each transaction was generated.

**UnitPrice:** Product price per unit in USD.

**CustomerID:** a 5-digit integral number uniquely assigned to each customer.

**Country:** the name of the country where each customer resides.

<br>

[The datasets can be downloaded from here](https://github.com/shekharbiswas/Data-Analytics-Machine-Learning/blob/master/Module%202/Resources/ecom-sales.rar)

<br>
<br>

**There will be many products in the products datasets which have not been sold in this time period and those entries won't be in the sales dataset. You can consider cleaning the data (if any) before creating Database / tables. The visualisations can be made with seaborn / Matplotlib/ Plotly / express (animated)**

<br>






















<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


**This dataset is close proximation of real sales and might rquire some improvements. Your suggestions in this regard will be appreciated.
