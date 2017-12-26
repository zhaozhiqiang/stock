import sqlite3

HSGT_DB = '../../../data/hsgt.db'
HSGT_COLUMNS = '''(date, s_code, s_name, close_price, up_percentage, share_hold_sum, share_rate, share_hold_price, share_hold_price_1, share_hold_price_5, share_hold_price_10)'''


class HSGTDB:
    conn = sqlite3.connect(HSGT_DB)
    cursor = conn.cursor()

    def __init__(self):
        self.create_hsgt()

    def create_hsgt(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS hsgt ''' +
            HSGT_COLUMNS)

    def __del__(self):
        self.dispose()

    def connect(self):
        self.conn = sqlite3.connect(HSGT_DB)
        self.cursor = self.conn.cursor()

    def dispose(self):
        self.cursor.close()
        self.conn.close()

    def get_last_date(self):
        self.cursor.execute("select date from hsgt ORDER BY date DESC")
        return self.cursor.fetchone()[0]

    def insert_data(self, data):
        self.cursor.executemany(
            "insert into hsgt  values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.conn.commit()


if '__main__' == __name__:
    hsgt_db = HSGTDB()
    hsgt_db.create_hsgt()
