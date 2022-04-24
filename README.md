# Cryptocurrencies during Crisis

The creators of this repository are collecting data to fill a data lake for a university project.
The data will be used to gain insight into the behavior of cryptocurrencies during a crisis - specifically the current war in Ukraine (April 2022).

This repository contains code used to retrieve data from three different sources: Twitter, Google Trends and Binance.


## Twitter Data
The code in Lambda_Twitter_ETL is used in an AWS Lambda function.
It collects Tweets from the Twitter search API and pushes them into an AWS S3 bucket.
In the input section of the code "start_time" and "end_time" define the timeframe from whicht Tweets are collected.

To connect to the Twitter search API a bearer token is needed. You find your bearer token under "Keys and tokens"  on your Twitter Developer Dashboard. If you do not already have a Twitter Developer account, you will first have to create one to get your token. 

When collecting Tweets, keep in mind, that there are maximum monthly Tweet caps (depending on access type) as well as a maximum number of requests per 15 minutes. Adapt the code according to the limitations of your account.
Rate limits with essential access (Developer Account): https://developer.twitter.com/en/docs/twitter-api/rate-limits

In the input part of the code you can choose what kind of Tweets you want to collect. In my case I wanted English Tweets that contain the word "sanctions", and I did not want retweets, replies or quotes.

Furthermore, in the create_url function you can define what kind of data you want to collect from each Tweet. Find more information about what data you can collect here: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet

## Google Trends Data


## Binance Data
Hello, here I show a straight way to get marketprices from cryptocurrencies on binance with the binance-connector.

1. code_etl.py shows the code implemented in my AWS Lambda Function, to get daily marketiprices.
2. code_etl_historical.ipynb shows the code for Jupyter Notebook, which I used to get historical data (100 days ago).
3. gitignore hides my layer (zip-format) for my AWS Lambda Funtcion, with which i get access to several packages (e.g. pandas, binance-connector,...). This layer was uploaded in a S3-Bucket and then connected to my ETL-Lambda Function.
