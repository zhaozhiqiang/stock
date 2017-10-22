from subprocess import check_output
from multiprocessing import Pool
import os
import sqlite3


PROCESS_NUM = 8
STOCK_HIS_FILE = './stocks_his'
STOCKS_DB = 'stocks.db'
CURL_ARG_0 = 'http://q.stock.sohu.com/hisHq?code=cn_'
CURL_ARG_1 = '000001'
CURL_ARG_2 = '&start='
CURL_ARG_3 = '20170101'
CURL_ARG_4 = '&end='
CURL_ARG_5 = '20170930'
CURL_ARG_6 = '&stat=1&order=D&period=d&callback=historySearchHandler&rt=json'
CURL_ARG_END = CURL_ARG_2 + CURL_ARG_3 + CURL_ARG_4 + CURL_ARG_5 + CURL_ARG_6


def get_existing_stocks():
    existing_stock_list = []
    conn = sqlite3.connect(STOCKS_DB)
    c = conn.cursor()
    stock_column = c.execute('SELECT stock_id FROM stocks')
    for row in stock_column:
        existing_stock_list.append(row[0])
    return existing_stock_list


def switch_to_target_file():
    if not os.path.exists(STOCK_HIS_FILE):
        os.mkdir(STOCK_HIS_FILE)

    os.chdir(STOCK_HIS_FILE)


def process_part_stocks(part_num, stocks):
    process_num = part_num
    stocks_len = len(stocks)
    while part_num < stocks_len:
        if not os.path.isfile('./' + str(stocks[part_num]) + '.txt'):
            stock_his = check_output(["curl", CURL_ARG_0 + str(stocks[part_num]) + CURL_ARG_END])
            with open('./' + str(stocks[part_num]) + '.txt', 'w') as f:
                f.write(stock_his)
        part_num += PROCESS_NUM


if __name__ == '__main__':
    stocks = get_existing_stocks()

    switch_to_target_file()
    p = Pool()
    for i in range(PROCESS_NUM):
        p.apply_async(process_part_stocks, args = (i, stocks))
    p.close()
    p.join()
