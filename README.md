The creators of this repository are collecting data to fill a data lake.
The data will be used to gain insight into the behaviour of cryptocurrencies during a crisis (specifically the current war in Ukraine).

This repository contains code used to retrieve data from three different sources: Twitter, Google Trends and Binance.

Hello, here I show a straight way to get marketprices from cryptocurrencies on binance with the binance-connector.

1. code_etl.py shows the code implemented in my AWS Lambda Function, to get daily marketiprices.
2. code_etl_historical.ipynb shows the code for Jupyter Notebook, which I used to get historical data (100 days ago).
3. gitignore hides my layer (zip-format) for my AWS Lambda Funtcion, with which i get access to several packages (e.g. pandas, binance-connector,...). This layer was uploaded in a S3-Bucket and then connected to my ETL-Lambda Function.
