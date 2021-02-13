
# Scrape Amazon

<p align="center">
  <img  width="550" height="300" src="../images/amazon.png">
</p>

<br>

Before you begin, please read this carefully:


'It is completely legal to use Amazon data for research and comparative purposes as long as it's for your own consumption. If you try to publish these results on the web, Amazon may take legal action against your business. It will help if you are careful when using images or videos as they may be copyrighted. Furthermore, you should make sure that all the information you extract is available to the public, and no account or captcha is required to obtain it. If you are trying to profit from Amazon data, you must make sure that your price comparisons have an added value that makes them unique. In other words, you can't just explicitly sell Amazon data, as you would be violating their Terms of Service, your price comparison will have to offer comprehensive research done by your business that you can claim as your intellectual property.'

That suggests, you can use the data for education purpose and can not create a business out of it without proper pre-cautions.


***VS Electronics*** is interested in below list of products to be scraped from Amazon website. 

* Laptops
* Monitors
* Processors
* Mouse
* Keyboard
* DSLR Cameras
* Smartphones (include Andriod & iPhones)
* Headphones


In each segment, you are supposed to take at least 1000 products. The more the better, however, this might be very time consuming / even impossible to get all listed products in a particular segment.

<br>

## Scraping Processors


<br>

[GITHUB link: All the codes and files can be accessed here](https://github.com/shekharbiswas/scrape_processor)

<br>

* create ***search_urls.txt*** which will contain all the product pages.
You can use a for loop to change the page number.

<br>

If not clear look at ***create_search_urls.py***

```
https://www.amazon.com/s?k=Processor&ref=nb_sb_noss_2
https://www.amazon.com/s?k=Processor&i=computers-intl-ship&page=2&qid=1594555641&ref=sr_pg_2
https://www.amazon.com/s?k=Processor&i=computers-intl-ship&page=3&qid=1594555641&ref=sr_pg_3
https://www.amazon.com/s?k=Processor&i=computers-intl-ship&page=4&qid=1594555641&ref=sr_pg_4
https://www.amazon.com/s?k=Processor&i=computers-intl-ship&page=5&qid=1594555641&ref=sr_pg_5
https://www.amazon.com/s?k=Processor&i=computers-intl-ship&page=6&qid=1594555641&ref=sr_pg_6
https://www.amazon.com/s?k=Processor&i=computers-intl-ship&page=7&qid=1594555641&ref=sr_pg_7
https://www.amazon.com/s?k=Processor&i=computers-intl-ship&page=8&qid=1594555641&ref=sr_pg_8
https://www.amazon.com/s?k=Processor&i=computers-intl-ship&page=9&qid=1594555641&ref=sr_pg_9
https://www.amazon.com/s?k=Processor&i=computers-intl-ship&page=10&qid=1594555641&ref=sr_pg_10


....
....

```
<br>

* Create ***search.yml*** which contains all the element paths from where the informations would be extracted. 

<br>

* Run ***search.py*** which takes ***search_urls.txt*** and ***search.yml*** as inputs and write the basic product details to ***search_output.jsonl***. Also it should write the urls of the products in ***product_urls.txt***.

Please understand the code and modify it according to your needs.

Each line of the ***search_output.jsonl*** would look like below:

```

{"title": "EVanlak DispalyPort Headless Ghost Display Emulator for PC 4K DP Dummy Plug (fit Headless 1080@60Hz-3840x2160@17hz)-3Pack", "url": "https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_next_computers-intl-ship_sr_pg2_1?ie=UTF8&adId=A06108363P349IDK8P7SH&url=%2FEVanlak-DispalyPort-Headless-Emulator-3840x2160%2Fdp%2FB07YLQZXKY%2Fref%3Dsr_1_13_sspa%3Fdchild%3D1%26keywords%3DProcessor%26qid%3D1594555641%26s%3Dcomputers-intl-ship%26sr%3D1-13-spons%26psc%3D1&qualifier=1594557670&id=7409642144659484&widgetName=sp_atf_next", "rating": "5.0 out of 5 stars", "review_count": "7", "price": "$16.99"}, 
```

As you can observer already, lots of string manipulation would be required after you convert the json files into pandas dataframes.

<br>

* Create the ***products.yml*** to select particular informations from product pages.

**Remember that, 'products.yml' would change based on the type of products you are scraping as the css elements of one product type generally do not match with the other product type. Sometimes this can be real tricky to know the elemenets.**

To create / modify this yaml file you can use [selector gadget](https://selectorgadget.com/). There is a [chrome extension](https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb?hl=en) which you have to install and use for the same.

<br>

[![A small demo how you can use Selector Gadget to get CSS selectors for the YAML file](https://img.youtube.com/vi/GSMVAliPhxU/0.jpg)](https://www.youtube.com/watch?v=GSMVAliPhxU)



<br>

* Run the ***product.py*** takes ***product_urls.txt*** and ***products.yml*** as inputs and output the ***product_output.jsonl***

Each output line in ***product_output.jsonl*** would look like:

<br>

```
{"name": "EVanlak DispalyPort Headless Ghost Display Emulator for PC 4K DP Dummy Plug (fit Headless 1080@60Hz-3840x2160@17hz)-3Pack", "product_tech_spec": null, "product_addl_info": [{"info": "Product Dimensions", "value": "13.33 x 0.7 x 0.2 inches"}, {"info": "Item Weight", "value": "0.352 ounces"}, {"info": "Manufacturer", "value": "EVanlak"}, {"info": "ASIN", "value": "B07YLQZXKY"}, {"info": "Customer Reviews", "value": "/*\n* Fix for UDP-1061. Average customer reviews has a small extra line on hover\n* https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40\n*/\n.noUnderline a:hover {\ntext-decoration: none;\n} 5.0 out of 5 stars 7 ratings P.when('A', 'ready').execute(function(A) {\nA.declarative('acrLink-click-metrics', 'click', { \"allowLinkDefault\" : true }, function(event){\nif(window.ue) {\nue.count(\"acrLinkClickCount\", (ue.count(\"acrLinkClickCount\") || 0) + 1);\n}\n});\n}); P.when('A', 'cf').execute(function(A) {\nA.declarative('acrStarsLink-click-metrics', 'click', { \"allowLinkDefault\" : true },  function(event){\nif(window.ue) {\nue.count(\"acrStarsLinkWithPopoverClickCount\", (ue.count(\"acrStarsLinkWithPopoverClickCount\") || 0) + 1);\n}\n});\n}); 5.0 out of 5 stars"}, {"info": "Best Sellers Rank", "value": "#850 in Computer Graphics Cards"}, {"info": "Date First Available", "value": "October 1, 2019"}], "seller": "EVanlak stroe", "seller_link": "https://www.amazon.com/gp/help/seller/at-a-glance.html/ref=dp_merchant_link?ie=UTF8&seller=AZ7INH5Q0KA03&isAmazonFulfilled=1", "freq_bought": null, "freq_bought_link": null, "link_to_all_reviews": "/EVanlak-DispalyPort-Headless-Emulator-3840x2160/product-reviews/B07YLQZXKY/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"}

```
<br>

(You can modify the code to exclude and include informations you find interesting)

**link_to_all_reviews** contains only the relative web address.

For example, 
'/EVanlak-DispalyPort-Headless-Emulator-3840x2160/product-reviews/B07YLQZXKY/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

Can you correct the code to add 'https://www.amazon.com' prefix to it and then write it in ***product_output.jsonl***.

Check out the code thoroughly if you can find similar things.

<br>




<br>

***The same thing you have to repeat for all of the product types.***

<br>

Once you have obtained the json file containing the product informations, you have to create a dataframe for each of these product types, i.e., one for Processors, one for laptops etc. As this is a nested json file, it is always a challenge to create a simple dataframe out of it.

<br>

[Also, you are advised to validate the json files before you use them.](https://jsonlint.com/)

<br>
<br>



## Resources

[Google is your best friend: Don't click here]()



