# Project 3:  VS Electronics

<p align="center">
  <img  width="600" height="350" src="https://cdn.pixabay.com/photo/2020/04/03/06/47/business-ions-4997574_960_720.png">
</p>

<br>

VS Electronics want to set up their online business across EU and focus on selling 'Laptops','Monitors','Headphones','Processors' etc.

Although the parent company **VS Group** is very famous in agriculture and food businesses, they apparently do not have any background in e-commerce businesses. As you might have noticed, their primary objective is to enter in Electronics segment as of now. So, you can keep your research limited to the electronics items.

A lot of companies do a through research on competitors irrespective of the fact whether the company is a start-up or already into the business.
This kind of competitive analysis can be defined as a process of identifying your competitors and evaluating their strategies to determine their strengths (e.g., highest selling products, ads strategy etc.) and weaknesses(e.g., part of the year when sales volume is real low, high shiping costs for some regions etc.) relative to your own business, product, and service. 

The goal of the competitive analysis is to gather the insights necessary to find a line of attack and develop your go-to-market strategy.



This task requires you to understand the domain beforehand and create a small report ( 1 -2 pages) 'Case Study: Ecommerce Domain' which would contain:

* Basic overview of E-commerce business model
* Name of top 3 e-commerce retailers in Germany
* Can you think of some of the possible competitors who might be interesting to analyse.

[Ecommerce in Germany](https://www.growcode.com/blog/ecommerce-in-germany/)




## Web Scraping

One of best way to know your competitor is to look at what they show publicly on their websites. There are so much informations like product details, prices, customer reviews, product seller information etc. which can  help you understand your competitor's business in a great extent.

To gather data from websites, you need to learn **Web scraping** which is basically a technique of extracting relevant information from websites. 

Lets say you want to find the price of an item on the eCommerce website. To do so, you visit the website, search for the item and then scroll until you find the price of the item.

But now let’s say you want to do this for thousands of items, perhaps across multiple pages of the website. As you can imagine if you have to do manually checking prices on all of them , it might take you days even months based on the size of the website and product lists. That is when you can think of writing a web scaper to do this task programmatically.

This mostly focuses on acquiring data which are stored inside HTML / CSS elements of web pages and transform it into a structure data (database, spreadsheet etc.).*Therefore, one can think of brushing up HTML and CSS basic knowledge before starting to scrape the website.*

Understanding how browser works is also important aspect as most of the webscraping would be done by providing web scraper with one or more URLs to load. The scraper then loads the entire HTML code for the page, even might include CSS & JS (advanced scraper). This is quite comparable with how browser works in fetching the web page content.

[![Check out: How Browser works ](https://img.youtube.com/vi/hJHvdBlSxug/0.jpg)](https://www.youtube.com/watch?v=hJHvdBlSxug)

Once, you have understood how browser works, you can revise the concepts of API in this context:

[![What is API ? ](https://img.youtube.com/vi/OVvTv9Hy91Q/0.jpg)](https://www.youtube.com/watch?v=OVvTv9Hy91Q)


<br>

[![A basic introduction: What is webscarping?](https://img.youtube.com/vi/Ct8Gxo8StBU/0.jpg)](https://www.youtube.com/watch?v=Ct8Gxo8StBU
)

<br>

You can also choose to follow a book which explains all the terminologies before you start to do web scraping yourself.

[**Detailed Analysis : Web Scraping with Python**](https://yanfei.site/docs/dpsa/references/PyWebScrapingBook.pdf)


Once, you have gone through the basic concepts, can you also include ***kind of informations you want to have from the products*** in the report 'Case Study: Ecommerce Domain' you just prepared. You can consider any standard websites (ex- Amazon, Zalando etc.) for this.


## Web Scraping Algorithms

Beautiful Soup is a widely used Python package which help to parse HTML and XML documents (including having malformed markup, i.e. non-closed tags, so named after tag soup). It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.

[Getting started with beautiful soup](https://www.pluralsight.com/guides/web-scraping-with-beautiful-soup)

<br>
For more details:

[the beautifulsoup official documentation](https://readthedocs.org/projects/beautiful-soup-4/downloads/pdf/latest/)

<br>

Scrape a web page of your choice in Amazon using beautiful soup and extract few particular information from the page.

For example, you can choose to scrape the webpage of product [Apple iphone pro 11](https://www.amazon.com/Apple-iPhone-64GB-Space-Gray/dp/B07ZPKZSSC/ref=sr_1_1?dchild=1&keywords=iphone+11&qid=1595272453&sr=8-1)


Please extract basic informations: Name of the product, size, review count and rating etc. The below image is just for explanation and might vary from the original one. Also, you can choose the elements/ informations you want to retrieve from the product page.

<p align="center">
  <img  width="550" height="350" src="../images/product_basics.JPG">
</p>


**Once you have finished the exploration on Beautifulsoup, please try to think about below stuffs**:

<br>

* Briefly describe the differences between the webbrowser, requests, bs4.
(hint : You can choose to elaborate your understanding visually by making diagrams)

* How web scraping is related / not-related to Data Mining and API ?

* Do you think if you send huge number of requests to a web page, there is a good chance the server denies your further request.

* Can you think of such scenarios which will hinder your web scraping activity.

* Can you think of few other business models which are based on web scraping.

<br>

**Checklist: Can you answer these technical questions**

* What type of object is returned by requests.get()? How can you access the downloaded content as a string value ?

* What requests method checks that the download worked ?

* How can you get the HTTP status code of a requests response ?

* How do you save a requests response to a file ?

<br>

**You should be able to answer above questions before you move to the next assignment**

You can keep the answers to these questions in your ***Learning report*** which you have to submit at the end of this module.

## Limitations of Beautifulsoup

There is no doubt that Beautiful soup is one of most widely used Data scraping library in the world. However, it is still treated as a beginner's choice. It not only takes much memory but also lacks many functionalities and is good for scraping small number of pages.

For example, you can not use **Xpath expressions** with Beautiful Soup.

[AN INTRODUCTION TO XPATH: HOW TO GET STARTED](https://blog.scrapinghub.com/2016/10/27/an-introduction-to-xpath-with-examples#:~:text=XPath%20is%20a%20powerful%20language,extract%20web%20data%20using%20Scrapy.&text=Just%20paste%20the%20HTML%20samples,and%20play%20with%20the%20expressions.)


[Know more about Xpath expressions: visit here](https://devhints.io/xpath)


To overcome these drawbacks, you can come up with alternative solutions like 'Scrapy', 'selectorlib' etc.

Here, we will use [selectorlib official doc](https://selectorlib.com/)which do the job quite good for scraping this huge amount of data.

The first task requires you to understand the basic working principles of this library and next, you would implement these to extract amazon product data in next week.

<br>


## Resources

* [Guide for web scraping :Automate the boring stuff](https://automatetheboringstuff.com/2e/chapter12/)

* [Google is your best friend](www.google.com)

* [web scraping additional tutorial](https://realpython.com/beautiful-soup-web-scraper-python/) for more details.
