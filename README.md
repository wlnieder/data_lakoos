
Hello, here I show a straight way to get marketprices from cryptocurrencies on binance with the binance-connector.

1. code_etl.py shows the code implemented in my AWS Lambda Function, to get daily marketiprices.
2. code_etl_historical.ipynb shows the code for Jupyter Notebook, which I used to get historical data (100 days ago).
3. gitignore hides my layer (zip-format) for my AWS Lambda Funtcion, with which i get access to several packages (e.g. pandas, binance-connector,...). This layer was uploaded in a S3-Bucket and then connected to my ETL-Lambda Function.
