import sqlite3
import os
import ast


STOCKS_DB = 'stocks.db'
STOCK_HIS_FILE = './stocks_his/'
STOCK_COLUMNS = ''' (date, begin, end, stock_up, stock_up_percentage,
                     low, high, volume, turnover, turnover_rate)'''


def get_sql_create_tables(stocks):
    sql = 'CREATE TABLE IF NOT EXISTS '
    return times_sql_for_create_table(sql, stocks)


def times_sql_for_create_table(sql, args):
    sqls = ''
    for arg in args:
        sqls += sql + get_stock_with_prefix(arg[0]) + ' ' + STOCK_COLUMNS + ';\n'
    return sqls


# refer
# https://docs.python.org/2/library/sqlite3.html#sqlite3.cursor.executescript
# build multiple SQL statements for cursor.executescript()
def times_sql(sql, args):
    sqls = ''
    for index in range(len(args)):
        sqls += sql + '(' + str(args[index])[1:-1] + ');\n'
    return sqls


def get_stock_with_prefix(stock):
    if '6' == stock[0]:
        return 'SH' + str(stock)
    return 'SZ' + str(stock)


def get_stock_price_his(stock):
    # get the stock's price history data from STOCK_HIS_FILE
    with open(STOCK_HIS_FILE + stock + '.txt', 'r') as f:
        return ast.literal_eval(f.read()[1:-2])['hq']


def get_sql_insert_data(stocks):
    sql_insert_data = ''
    for stock in stocks:
        table = get_stock_with_prefix(str(stock[0]))

        # If there is a valid data in file, the file's size
        # will greater than 200
        if os.path.getsize(STOCK_HIS_FILE + str(stock[0]) + '.txt') > 200:
            content = get_stock_price_his(str(stock[0]))
            sql = 'INSERT INTO ' + table + STOCK_COLUMNS + ' VALUES '
            sql_insert_data += times_sql(sql, content)
        else:
            size = os.path.getsize(STOCK_HIS_FILE + str(stock[0]) + '.txt')
            print str(stock[0]) + ': ' + str(size)

    return sql_insert_data


def create_all_stocks_table():
    conn = sqlite3.connect(STOCKS_DB)
    cursor = conn.cursor()

    # get stock list from stocks
    cursor.execute('SELECT stock_id FROM stocks')
    stocks = cursor.fetchall()

    # for every stock, create a table to store stock's price data
    sql_stocks_table = get_sql_create_tables(stocks)
    cursor.executescript(sql_stocks_table)
    conn.commit()

    # insert data
    sql_insert_data = get_sql_insert_data(stocks)
    cursor.executescript(sql_insert_data)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_all_stocks_table()
