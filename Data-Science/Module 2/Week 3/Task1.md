# Micro Services : Docker & Google Kubernetes Engine (GKE)

Before you use some microservices architechture, spend some time understanding the core concepts. There are so many resources out there.

These below articles might have many things in common.


* [What Are Microservices? An Introduction to Microservice Architecture](https://dzone.com/articles/what-is-microservices-an-introduction-to-microserv)


* [4 Microservices Examples: Amazon, Netflix, Uber, and Etsy](https://blog.dreamfactory.com/microservices-examples/)

* [Docker & The Rise Of MicroServices](https://timber.io/blog/docker-and-the-rise-of-microservices/#:~:text=With%20Docker%2C%20you%20can%20make,ship%20and%20deploy%20your%20application.)


Microservices have a few disadvantages as well if you consider the complexity caused by careful management of inter module message communication, database updates etc. No doubt, it requires more resources too.

There is no need to understand every bit of it at the moment. You can always revisit this theory portion once in a while, however, the basic concepts of **why microservices work better than a Monolithic architecture** should be clear.



[Set up, build and run docker image](https://docs.docker.com/get-started/)

### Set up the docker environment.

#### Mac

[Install docker on Mac](https://docs.docker.com/docker-for-mac/install/)

#### Windows

[Install on windows 10 pro: check for system requirements](https://docs.docker.com/docker-for-windows/install/)

If the system requirements are not met, [check here: windows 10 home](https://docs.docker.com/docker-for-windows/install-windows-home/)

However, it has to be latest Windows 10 Home. There is a good chance for windows users *not to meet even* this criteria and then you have to [go here and follow the steps](https://docs.docker.com/toolbox/toolbox_install_windows/)


<br>
<p align="center">
  <img  width="750" height="450" src="../images/docker_unsupported.jpg">
</p>
<br>

Once you have installed the docker toolbox successfully, you should see below message on the command prompt:


<br>
<p align="center">
  <img  width="750" height="400" src="../images/install_docker.jpg">
</p>
<br>

Get familiar with the terminologies (specially *Docker objects*)
[Basic intro: Docker](https://docs.docker.com/get-started/overview/)

Many beginners find it difficult to understand from official documentation, so you are advised to look out for more simple explanations on websites like quora / stack overflow.

For example, here is a [nice explanation of docker base image](https://www.quora.com/What-exactly-is-a-base-image-in-Docker)

Similarly, look for explanations of other terms so that you can co-relate the meaning of these later when you start using it actually.

[Docker hub: understand the basics](https://docs.docker.com/docker-hub/)


Steps of implementation:

<br>
<p align="center">
  <img  width="700" height="300" src="../images/docker_diagram.JPG">
</p>
<br>


### Create Dockerfile

Dockerfile consists of a set of instructions to create docker image of the application.


[Please have a look at these basic commands which are used in a Dockerfile](https://docs.docker.com/engine/reference/builder/#:~:text=The%20EXPOSE%20instruction%20informs%20Docker,not%20actually%20publish%20the%20port.)

The below commands will be used to create the docker file, so a basic understanding of all these commands is must before you proceed further.


* FROM
* COPY
* EXPOSE
* WORKDIR
* RUN
* CMD


[Simple explanation if official doc is too much in the beginning](https://medium.com/@tasnuva2606/dockerize-flask-app-4998a378a6aa)


A sample dockerfile would look like:

```
FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python flask_api.py
```

Each of these lines of Dockerfile is a layer and each layer contains only the delta, or changes from the layers before it.


[More about Docker EXPOSE Ports](https://vsupalov.com/docker-expose-ports/)

### Create Docker APP

Once you have finished the Dockerfile, you need to create requirements.txt file with all the libraries required to be installed before you run the docker process in the container.

[All the files are present here](https://github.com/shekharbiswas/Data-Analytics-Machine-Learning/tree/master/Module%202/dockerapp)

The following commands on your docker command prompt will help you create the docker app and test it through the web link.

* docker build -t bike_app .
* docker images
* docker run -p 8000:8000 bike_app

The below video explains the steps:

[![Create Docker App](https://img.youtube.com/vi/6MkLCp9K41s/0.jpg)](https://www.youtube.com/watch?v=6MkLCp9K41s)





### Kubernetes

As per official doc,
Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

[Get an idea of Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

<br>

[why-and-when-you-should-use-kubernetes](https://hackernoon.com/why-and-when-you-should-use-kubernetes-8b50915d97d8)


<br>

**Google Kubernetes Engine**

[This tutorial explains in detail how you can deploy docker app on Google Cloud](https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app)


<br>

If things are not clear, you can watch the video which talks about this exact application with minimal features.

<br>

[![Create Docker App](https://img.youtube.com/vi/1LR1WMGvgdI/0.jpg)](https://www.youtube.com/watch?v=1LR1WMGvgdI)

<br>
<br>

[github link for the same](https://github.com/shekharbiswas/capitalbikeshare-docker-kubernetes)
<br>



***In all of these cases, you were supposed to include modify the basic app version and add at least 2 more functionalities or features. As you already been aware of KPIs, it would always be nicer to have some KPI metrics incorporated in the app so that it adds business values besides being fun for end users.*** 


<br>

## Resources

[what-is-the-need-for-docker-daemon](https://stackoverflow.com/questions/42641011/what-is-the-need-for-docker-daemon)



