#!/bin/bash

STOCKS_HIS="./stocks_his"
STOCKS_DB="./stocks.db"

# remove old data
if [ -d "$STOCKS_HIS" ]; then
    rm -rf "$STOCKS_HIS"
fi

if [ -f "$STOCKS_DB" ]; then
    rm "$STOCKS_DB"
fi

# create table [stocks]
python create_stocks.py

# download stocks' price data
python curl.py

# insert stocks transaction data to sqlite
python save_to_sqlite.py
