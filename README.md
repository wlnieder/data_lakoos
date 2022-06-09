# Cryptocurrencies during Crisis

The creators of this repository are collecting data to fill a data lake for a university project.
The data will be used to gain insight into the behavior of cryptocurrencies during a crisis - specifically the current war in Ukraine (June 2022).

This repository contains code used to retrieve data from three different API's: Twitter, Google Trends and Binance.
Additionally, there is code used to process the Twitter data. 
Twitter and Google Data is used to map the course of the war, while from Binance the cryptocurrency rates are retrieved.
The goal is to see, if cryptocurrencies show potential safe haven characteristics during this time of crisis.


## Twitter Data
The code in Lambda_Twitter_ETL is used in an AWS Lambda function.
It collects Tweets from the Twitter search API and pushes them into an AWS S3 bucket.
In the input section of the code "start_time" and "end_time" define the timeframe from whicht Tweets are collected.

To connect to the Twitter search API a bearer token is needed. You find your bearer token under "Keys and tokens"  on your Twitter Developer Dashboard. If you do not already have a Twitter Developer account, you will first have to create one to get your token. 

When collecting Tweets, keep in mind, that there are monthly Tweet caps depending on your access type as well as a maximum number of requests per 15 minutes. Adapt the code according to the limitations of your account.
Rate limits with essential access (Developer Account): https://developer.twitter.com/en/docs/twitter-api/rate-limits

In the input part of the code you can choose what kind of Tweets you want to collect. In my case I wanted English Tweets that contain the word "sanctions", and I did not want retweets, replies or quotes.

Furthermore, in the create_url function you can define what kind of data you want to collect from each Tweet. Find more information about what data you can collect here: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet  

Additionally to the tweets collected daily, we hydrated tweet IDs from the following GitHub repository: https://github.com/echen102/ukraine-russia   
Emily Chen and Emilio Ferrara collected these tweets in the context of the invasion of Ukraine on 22 February 2022 by Russia and the resulting, ongoing war. For further information, please check out their associated paper: [Tweets in Time of Conflict: A Public Dataset Tracking the Twitter Discourse on the War Between Ukraine and Russia](https://arxiv.org/abs/2203.07488)

As we created counts of English tweets containing specific keywords, the hydrated tweets had to be filtered and a count had to be created.
For the cleaning and processing of the Twitter data, the code was used in the following order: 
1. Twitter_file_splitting_PowerShell
2. Twitter_Cleaning_And_Filtering
3. Twitter_Merging_Keyword_Files_5_Parts
4. Twitter_Merging_Total_And_Creating_Count


## Google Trends Data
With the Python code data_historical_ keywords it is possible to retrieve the search volume for certain keywords from Google Trends. Since the API has limitations regarding requests, a time delay is necessary. Because of this, the script takes a while to get the desired output.

The code lambda_function_google_trends is intended to implement the Google Trends query for an AWS Lambda function. For this, the corresponding package pytrends must be loaded in a layer. This works best if you work with Python 3.8.

## Binance Data
Hello, here I show a straight way to get marketprices from cryptocurrencies on binance with the binance-connector.

1. code_etl.py shows the code implemented in my AWS Lambda Function, to get daily marketiprices.
2. code_etl_historical.ipynb shows the code for Jupyter Notebook, which I used to get historical data (100 days ago).
3. gitignore hides my layer (zip-format) for my AWS Lambda Funtcion, with which i get access to several packages (e.g. pandas, binance-connector,...). This layer was uploaded in a S3-Bucket and then connected to my ETL-Lambda Function.
