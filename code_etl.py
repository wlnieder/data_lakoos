import json
import os
import pandas as pd
import psycopg2
from binance.spot import Spot as Client

ENDPOINT = os.environ['ENDPOINT']
DB_NAME = os.environ['DB_NAME']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']


def lambda_handler(event, context):
    # url to access binance api
    base_url = "https://api.binance.com"

    # create Client to access API
    spot_client = Client(base_url=base_url)

    # Access historical prices - Bitcoin/USD
    btcusd_history = spot_client.klines("BTCUSDT", "1d", limit=1)

    # as DataFrame
    columns = ['time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades',
               'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    btcusd_history_df = pd.DataFrame(btcusd_history, columns=columns)
    btcusd_history_df['time'] = pd.to_datetime(btcusd_history_df['time'], unit='ms')

    # Access historical prices - Etherum/USD
    ethusd_history = spot_client.klines("ETHUSDT", "1d", limit=1)

    # as DataFrame
    columns = ['time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades',
               'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    ethusd_history_df = pd.DataFrame(ethusd_history, columns=columns)
    ethusd_history_df['time'] = pd.to_datetime(ethusd_history_df['time'], unit='ms')

    # Access historical prices - Litecoin/USD
    ltcusd_history = spot_client.klines("LTCUSDT", "1d", limit=1)

    # as DataFrame
    columns = ['time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades',
               'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    ltcusd_history_df = pd.DataFrame(ltcusd_history, columns=columns)
    ltcusd_history_df['time'] = pd.to_datetime(ltcusd_history_df['time'], unit='ms')

    # Access historical prices - Cardano/USD
    adausd_history = spot_client.klines("ADAUSDT", "1d", limit=1)

    # as DataFrame
    columns = ['time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades',
               'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    adausd_history_df = pd.DataFrame(adausd_history, columns=columns)
    adausd_history_df['time'] = pd.to_datetime(adausd_history_df['time'], unit='ms')

    # Connection to datalakecrypto (Amazon RDS)
    try:
        conn = psycopg2.connect("host={} dbname={} user={} password={}".format(ENDPOINT, DB_NAME, USERNAME, PASSWORD))
    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)

    # get cursor
    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: Could not get curser to the Database")
        print(e)

    # allways Auto commit
    conn.set_session(autocommit=True)

    # Bitcoin-USD-Prices loading to Postgres
    def add_data(time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades,
                 taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore):
        try:
            # SQL statement with VALUE %s. All data has to be transmitted by %s, doesnt matter if string or float.
            statement = "INSERT INTO btcusd_history (time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades, taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades,
                    taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore)
            cur.execute(statement, data)
            print("Successfully added entry to database")  # check-message
        except psycopg2.Error as e:  # In the except block, which only executes when there is an exception, declare database.Error as e. This variable will hold information about the type of exception that occurs.
            print(f"Error adding entry to database: {e}")

    for pos, d in btcusd_history_df.iterrows():
        add_data(
            d["time"],
            d["open"],
            d["high"],
            d["low"],
            d["close"],
            d["volume"],
            d["close_time"],
            d["quote_asset_volume"],
            d["number_of_trades"],
            d["taker_buy_base_asset_volume"],
            d["taker_buy_quote_asset_volume"],
            d["ignore"])

    # Etherum-USD-Prices loading to Postgres
    def add_data(time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades,
                 taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore):
        try:
            # SQL statement with VALUE %s. All data has to be transmitted by %s, doesnt matter if string or float.
            statement = "INSERT INTO ethusd_history (time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades, taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades,
                    taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore)
            cur.execute(statement, data)
            print("Successfully added entry to database")  # check-message
        except psycopg2.Error as e:  # In the except block, which only executes when there is an exception, declare database.Error as e. This variable will hold information about the type of exception that occurs.
            print(f"Error adding entry to database: {e}")

    for pos, d in ethusd_history_df.iterrows():
        add_data(
            d["time"],
            d["open"],
            d["high"],
            d["low"],
            d["close"],
            d["volume"],
            d["close_time"],
            d["quote_asset_volume"],
            d["number_of_trades"],
            d["taker_buy_base_asset_volume"],
            d["taker_buy_quote_asset_volume"],
            d["ignore"])

    # Litecoin-USD-Prices loading to Postgres
    def add_data(time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades,
                 taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore):
        try:
            # SQL statement with VALUE %s. All data has to be transmitted by %s, doesnt matter if string or float.
            statement = "INSERT INTO ltcusd_history (time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades, taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades,
                    taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore)
            cur.execute(statement, data)
            print("Successfully added entry to database")  # check-message
        except psycopg2.Error as e:  # In the except block, which only executes when there is an exception, declare database.Error as e. This variable will hold information about the type of exception that occurs.
            print(f"Error adding entry to database: {e}")

    for pos, d in ltcusd_history_df.iterrows():
        add_data(
            d["time"],
            d["open"],
            d["high"],
            d["low"],
            d["close"],
            d["volume"],
            d["close_time"],
            d["quote_asset_volume"],
            d["number_of_trades"],
            d["taker_buy_base_asset_volume"],
            d["taker_buy_quote_asset_volume"],
            d["ignore"])

    # Cardano-USD-Prices loading to Postgres
    def add_data(time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades,
                 taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore):
        try:
            # SQL statement with VALUE %s. All data has to be transmitted by %s, doesnt matter if string or float.
            statement = "INSERT INTO adausd_history (time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades, taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (time, open, high, low, close, volume, close_time, quote_asset_volume, number_of_trades,
                    taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore)
            cur.execute(statement, data)
            print("Successfully added entry to database")  # check-message
        except psycopg2.Error as e:  # In the except block, which only executes when there is an exception, declare database.Error as e. This variable will hold information about the type of exception that occurs.
            print(f"Error adding entry to database: {e}")

    for pos, d in adausd_history_df.iterrows():
        add_data(
            d["time"],
            d["open"],
            d["high"],
            d["low"],
            d["close"],
            d["volume"],
            d["close_time"],
            d["quote_asset_volume"],
            d["number_of_trades"],
            d["taker_buy_base_asset_volume"],
            d["taker_buy_quote_asset_volume"],
            d["ignore"])

    # close connection
    cur.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')}