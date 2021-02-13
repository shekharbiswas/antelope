# Create APP from your ML model

## Heroku

Heroku is a cloud based commercial Platform as a Service(PaaS). It simplifies custom software application development, deployment, and maintenance of enterprise applications by providing various tools, services, and workflows.


Get to know the terminologies.

[What are the Cloud Computing Services - PaaS/ IaaS/ CaaS/ FaaS/ SaaS](https://medium.com/@nnilesh7756/what-are-cloud-computing-services-iaas-caas-paas-faas-saas-ac0f6022d36e)

As you will deploy your app on Heroku, you need to sign up there.

## Basics of Flask 

Flask is a micro web framework written in python and used in web development. The term 'microframework' means it does not require particular tools or libraries. 

Flask is a back-end framework, so you have to use HTML to code for the front end.

Front end is something you can see. Backend is not visible to end-users.

'Front-end is also referred to as the “client-side” as opposed to the backend which is basically the “server-side” of the application. The essentials of backend web development include languages such as Java, Ruby, Python, PHP, . Net, etc. The most common frontend languages are HTML, CSS, and JavaScript.'

(source: Medium Article)


[More on front end and back end](https://medium.com/@sagarajkt/the-fundamentals-of-front-end-and-back-end-development-5973ac0910cf#:~:text=Front%2Dend%20is%20also%20referred,HTML%2C%20CSS%2C%20and%20JavaScript.)

<br>

Although there are many backend web frameworks to deploy machine learning models, many experts suggest,  

'It is always a good idea to start with Flask. It's a great tool for learning web development fundamentals and best practices along with the core pieces of a web framework that are common to almost all frameworks and most importantly, it is easier to start with Flask.'

[install Flask](https://pypi.org/project/Flask/)


[quickstart guide](https://flask-doc.readthedocs.io/en/latest/quickstart.html#a-minimal-application)

In the beginning, you might consider to look for other simple explanations to understand basics of flask, as official docs might not be that much appealing first time.

[Very basic explanation](https://medium.com/acmvit/get-started-with-flask-b006fd08f96e#:~:text=Flask%20is%20a%20micro%2Dframework,jinja2%20as%20the%20templating%20engine.)

However, you are always advised to refer to the [official user guide](https://flask-doc.readthedocs.io/en/latest/).



## HTML components

There is no use of backend until and unless you have a front end to reach out to the end users. Most simple way to start front end would be to write HTML code (this is not a programming language, its one type of mark up language used for designing web page.)

[Get hands on with HTML](https://www.w3schools.com/html/)

You can explore as much as you want, however, the below concepts are must before you think of simple web page design.


* [basic](https://www.w3schools.com/html/html_basic.asp)
* [elements](https://www.w3schools.com/html/html_elements.asp)
* [forms](https://www.w3schools.com/html/html_forms.asp)


## Basic Javascript

[Get hands on with JS](https://www.w3schools.com/js/)

## Create Flask APP

You have already seen the basic components of a Flask App while following the tutorial.

Let's first try to design our basic app. interface. 

*This is just for sample and you are supposed to modify it as per your needs and functionalities.*

<br>
<p align="center">
  <img  width="400" height="450" src="../images/html_design.jpg">
</p>
<br>





[All the files have been kept in this folder](../flaskapp/)


* First step would be to create your machine learning model and save it.

[model.py](../flaskapp/model.py)

It will generate the 'model.pkl'.


* Create the front end. This file generates the design we just talked a while ago.

[A sample index.html would look like this.](../flaskapp/templates/index.html)

If you want to introduce new fields, you have to change in this file.

[Know more about 'Rendering Templates' here](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

Flask look for templates in the 'templates' folder, so you have to keep 'index.html' inside templates folder.

Go through them and try to understand the HTML forms and JS (if required).

* Create the app.py which is basically the main file you will run to see the results of your deployed machine learning model.

[GET and POST methods](https://pythonbasics.org/flask-http-methods/)




[link to the app.py file](../flaskapp/model.py)


While you run the app.py file, there might be some file error or system error; For file error, please check the location you are running the app. And for system errors, you are supposed to read the manual and try to figure it out.


Once you run the app.py, you would be able to test you app and predict the total bike count on the street based on those user inputs in real time!

## Postman

Postman is a great tool to check an API's functioanlity without the hassle of writing a bunch of code to create front end. 

However, usage of postman is not mandatory in this case as you have to create the front end as well.

This video explains how you can use it.

[![Postman to test your Flask App using Python](https://img.youtube.com/vi/D1lngM5Ta1w/0.jpg)](https://www.youtube.com/watch?v=D1lngM5Ta1w)


## Additional feature enhancements

* Can you think about how you can integrate google maps if some end user would like to know about the route.

* What other features from the feature lists would be cool to have. You can also do feature engineering to add new feature out of existing ones.

* Can you think of any KPI that can be shown on your APP.

* Be creative and add at least a few relevant functionalities you can do.

* Revise HTML / JavaScript  to create a nicer design of the app. 






## Deploy the APP on HEROKU

* create a **requirements.txt** file with all of the modules: 

The first thing you need to do is define which libraries the application uses. That way, Heroku knows which libraries to provide for the app, similar to how you install them locally when developing the app.


* For Heroku to be able to run the application, you need to define a set of processes/commands that it should run beforehand. These commands are located in the **Procfile**.

```
web: gunicorn app:app
```

The web command tells Heroku to start a web server for the application, using [gunicorn](https://vsupalov.com/what-is-gunicorn/). Since the application is called **app.py**, set the app name to be app as well.


* create and upload the contents of flaskapp on github repository.

* Log in to your Heroku account.

* Create new app.

* Connect to github.

* Manual Deploy.

* Click on view [ your all has been successfully deployed ]

**Internal Server Error** : Sometimes you might get this error and for this you are supposed to check **Build Logs** and error logs.
For more details, please refer [heroku guidelines](https://devcenter.heroku.com/articles/logging#:~:text=You%20can%20view%20your%20logs,menu%20select%20%E2%80%9CView%20logs%E2%80%9D.)

Also, you can check with the below web link:

'https://dashboard.heroku.com/apps/app-name'

'app-name' is the particular app name.
  
 
## Set up Google Cloud 

Next week, you will implement your project on Google Cloud; therefore you are supposed to finish the Cloud environment set up (if not done already). You have to go to [Google cloud console](https://console.cloud.google.com/) and log on with your email ID. Thereafter, you have to provide few informations including debit / credit card details to activate the free trial feature.


Once done, check the billing info (including terms and conditions) and there, you should have the trial usage fee of $300 getting reflected like below.

<br>
<p align="center">
  <img  width="1000" height="450" src="../images/gcp_setup.JPG">
</p>
<br>


## Resources 

* This tutorial deploys a different machine learning model, so you can follow it just to know the steps to follow to deploy an app on Heroku However, the above instructions should be sufficient. 


[Tutorial: Deploy Machine Learning Model on Heroku using Flask](https://www.youtube.com/watch?v=n8yXd4tZylg)

