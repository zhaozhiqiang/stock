import xlrd
import sqlite3


EXCEL = './excel/A.xlsx'
STOCKS_DB = 'stocks.db'


def get_stocks_from_excel():
    data = xlrd.open_workbook(EXCEL)
    table = data.sheet_by_index(0)
    new_stock_list = []

    # get valid stock id
    # NG data example: 603232.0
    for row in range(table.nrows):
        stock_id = str(table.cell(row, 0).value)[0:6]
        new_stock_list.append((stock_id,))

    return new_stock_list


def get_existing_stock_list(c):
    existing_stock_list = []
    stock_column = c.execute('SELECT stock_id FROM stocks')
    for row in stock_column:
        existing_stock_list.append(row[0])
    return existing_stock_list


def remove_duplicate_item(new_stock_list, old_stock_list):
    new_stock_list = []
    for index_in_all in range(len(new_stock_list)):
        add_to_new_stock_list = True
        for index_in_old in range(len(old_stock_list)):
            if new_stock_list[index_in_all][0] == old_stock_list[index_in_old]:
                add_to_new_stock_list = False

        if add_to_new_stock_list:
            new_stock_list.append(new_stock_list[index_in_all])

    return new_stock_list


def get_stock_list(cursor):
    new_stock_list = get_stocks_from_excel()
    old_stock_list = get_existing_stock_list(cursor)

    # if there is no data in stocks
    if 0 == len(old_stock_list):
        return new_stock_list
    else:
        return remove_duplicate_item(new_stock_list, old_stock_list)


def create_stocks():
    conn = sqlite3.connect(STOCKS_DB)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS stocks (stock_id)''')

    stock_list = list(set(get_stock_list(cursor)))
    cursor.executemany('INSERT INTO stocks VALUES (?)', stock_list)
    print 'Total item: ' + str(cursor.rowcount)

    cursor.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_stocks()
