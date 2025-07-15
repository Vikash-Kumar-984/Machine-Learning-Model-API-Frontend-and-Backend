# Machine-Learning-Model-API-Frontend-and-Backend

This repository contains the end to end project of frontend and backend for Machine Learning Model (APIs) on babies.csv dataset.

1 ounce = 28 grams

Gestation = 9 Months (280 Days)

Serialization: It converts the whole code into the binary format to the pickel file

pip freeze > requirements.txt : To import all the requirements(like pandas, scikit-learn, gunicorn,etc.) to requirements.txt file

model.pkl will be moved from model folder to home folder

# Git Setup

git init

git status #to track untracked file to be commit

git add . #to add all the files from local to github cloud

git commit -m "first commit"

git branch -M main #Define main branch

git remote add origin https://github.com/Vikash-Kumar-984/Machine-Learning-Model-API-Frontend-and-Backend.git #to add particular code to given origin

git push -u origin main #just pushing the code

# Code Changes Commit

  * git status #After changing the code

  * git add .

  * git commit -m "Changes in code commit"

  * git push -u origin main

# 1. What is deployment?

- Deployment means making your web application (like your Flask app) live on the internet so that other people can use it — not just on your computer.
For example, if you've built a machine learning model in Flask, deployment means putting it online so users can send requests and get predictions from anywhere in the world.

- Analogy:
Think of it like writing a document in MS Word (your local system). Deployment is like uploading it to Google Docs so your friends or coworkers can access it anytime.

# 2. How deployment is useful in Data Science?

- In data science, we often build models (e.g., to predict prices, detect spam, 
or classify images).

But just building the model isn't enough — we need to share it with real 
users or clients.

Deployment allows:

Others (users, apps, businesses) to use your model via a web interface or API
Integration into websites, mobile apps, or automation systems
Continuous feedback from users to improve the model

Example:

You built a model to predict Insurance Bill. 
By deploying it, a user can visit a web page, 
enter bill details, and get a bill 
instantly — powered by your model.

# 3. Overview of deployment stack.

A deployment stack is like a set of
 tools and technologies that work 
together to make your app live and 
usable online.

Local Computer -> Nginx (Web Server) -> Gunicorn (Application Server) -> Flask Framework

| Layer                  | Tool / Technology                | Purpose                                                     | 
|------------------------| ---------------------------------| ------------------------------------------------------------| 
| Application            | Flask (Python)                   | The core app (routes, logic, model)                         | 
|                        |                                  |                                                             | 
| Server                 | Gunicorn or uWSGI                | Runs your Flask app in production                           | 
|                        |                                  |                                                             | 
| Web Server             | Nginx or Apache                  | Handles incoming web traffic and sends it to your Flask app | 
|                        |                                  |                                                             | 
| Cloud Platform         | Render, Heroku, AWS, etc.        | Hosts your app online                                       | 
|                        |                                  |                                                             | 
| Domain (optional)      | GoDaddy, Namecheap, etc.         | A human-readable URL (like myapp.com)                       | 
|                        |                                  |                                                             | 

# Application Server (Gunicorn) : 

  * Flask’s built-in server (flask run) is not suitable for production.
  
  * Tools like Gunicorn or uWSGI wrap around your Flask app and make it faster and more stable.
  
  * Gunicorn is a Python Web Server Gateway Interface (WSGI) HTTP server used to serve Python web applications like Flask and Django. It acts as a bridge between the web server and your application, handling incoming requests and passing them to the appropriate application for processing. Gunicorn is particularly useful for production environments because it can handle multiple concurrent requests, ensuring high performance and scalability.


# Web Server (Nginx)

A web server like Nginx:

 * Nginx is a fast, production level HTTP server.
 
 * Accepts incoming requests (e.g., from browsers or Postman)
 
 * Forwards them to Gunicorn

# Cloud Hosting (Render/Heroku/AWS/etc.)

 - You deploy your Flask app and model to a cloud platform.

 -  The platform automatically connects everything:
    * Gunicorn

    * Web server

    * App environment

You get a public URL to share with others 
(e.g., https://flask-predictor.onrender.com)














