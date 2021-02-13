# Create Dataframes and Design DataBase  


<p align="center">
  <img  width="550" height="400" src="https://images.unsplash.com/photo-1544383835-bda2bc66a55d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=721&q=80">
</p>

<br>

So far you have been lucky to get the dataframes. Now, You have to create your own pandas dataframes out of these JSON files and thereafter, you will design your database & create tables there.



## Create Dataframes

* The first dataframe out of search_output.jsonl looks like below:

<p align="center">
  <img src="../images/s_raw.JPG">
</p>

* However, please apply data cleaning and make it nicer (this term is very relative).

<p align="center">
  <img src="../images/s_processed.JPG">
</p>

<br>

* Do you know you can shorten the URL of products by collecting ASIN as this is unique.

And, the URL standard format is:\
https://www.amazon.com/dp/ASIN

So if you have ASIN, you already have the product link!

<br>

* We will create below dataframes:

<br>

**summary**

This table will be unique for 8 types of products.
So, it might contain around 8000 records provided you have collected 1000 products from each catergory.

<br>

**product_details**

There will be 8 tables for each types of products as processors won't have the same set of columns as that of DSLR cameras.

<br>

**bought_together**

Single table which will contain all the items and frequently bought items.

(Hint: In the product details, you will get 'freq_bought' and also the link 'freq_bought_link' )

There will lots of items which do not have freq_bought item. Those informations can be deleted from this dataframe.


<br>

**customer_reviews**

Single table of all product reviews. This will certainly be the largest dataframe to deal with. However, we are not taking all the reviews, just recent reviews which are shown on the 1st page of many review pages.

Now the question is how would you get the review links in a single csv file. This is very common issue in data analytics that you will miss some steps and you would have to re-visit the early step.

The best way will be to modify ***product.py*** to include the code for ***review_urls.txt*** which would be similar to ***product_urls.txt***.Also, you can get it from ***product_details*** , so decision is yours.



We could have definitely created a few more dataframes. However, this time we would give you the option and you can create one / two more based on your interests.

[Here is the summary how all the dataframes might look like](https://docs.google.com/spreadsheets/d/1NPgMiNczdLHgiBR9_iOSV8_zxTNzmz-sYfauOBgIK-U/edit?usp=sharing)

However, you can choose the columns (especially in product_details dataframe).

[customer_reviews table might look like this where product is the name of the product and title is the 'review title'](https://github.com/shekharbiswas/DesignDatabase/blob/master/data.csv)

<br>
<br>

## Create Database

<p align="center">
  <img  width="700" height="450" src="https://i2.wp.com/code-data-ai.com/wp-content/uploads/2020/03/1.jpeg?w=1240&ssl=1">
</p>

<br>

* [Learn MySQL basics](https://mode.com/sql-tutorial/introduction-to-sql)

While learning, you should practice also in MODE SQL editor.

* [Install MySQL Workbench](https://www.mysql.com/products/workbench/)


Try to explore the MySQL workbench and check how it works. By now, you should be able to pick up a software looking at its official documentation. A lot of companies require you to learn their own softwares and this can be a good exercise for you. 

Once you have a good understanding of DBMS and SQL, you would have to design your database. However, the basic database and its design principles should be clear.

* [Introduction to Relational Database Design](http://web.mit.edu/11.521/www/lectures/lecture10/lec_data_design.html)


[Database design principles](https://www.oreilly.com/library/view/access-database-design/0596002734/ch04.html)


* [Data types in MySQL](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)


As you have already seen, few of the main tasks are choosing 'Primary Key', 'Foreign Key' carefully and reducing 'redundancy' (1NF, 2NF etc.) to take as less space as possible. So, keeping all these in mind, you have to choose the table columns and finally set up the database.

There are many ways you can save your created dataframe to MySQL. One of the option is to use **PyMySQL**.

[PyMySQL’s documentation](https://pymysql.readthedocs.io/en/latest/#)

Also, you can use **SQLAlchemy**

[SQLAlchemy: The Python SQL Toolkit and Object Relational Mapper](https://www.sqlalchemy.org/)



## Resources

* To accomplish the above steps you might require a lots of exploration on your own which is good. However, you should not feel lost and that is why the below github repository contains the guidelines for creating dataframes and databases.

You are strongly advised to look at it once you have spent quite a good amount of time (at least 2 - 3 hours) trying yourself.

[GITHUB link: create dataframes and design databases](https://github.com/shekharbiswas/DesignDatabase)

