import sqlite3
from datetime import date


def open_connection():
    return sqlite3.connect('housePrice.db')


def create_table(conn):
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS property('
              'propertyId INTEGER PRIMARY KEY,'
              'status TEXT, '
              'address TEXT, '
              'agent TEXT, '
              'bedroom INTEGER, '
              'price INTEGER)')

    c.execute('CREATE TABLE IF NOT EXISTS price_history('
              'propertyId INTEGER,'
              'price INTEGER, '
              'date TEXT,'
              'FOREIGN KEY (propertyId) REFERENCES property (propertyId))')


def add_data_entry(conn, instance_list):
    c = conn.cursor()
    # check whether it exsited, if exsited, whether price changed
    for instance in instance_list:
        curr_property_id = instance[0]
        curr_price = instance[-1]
        c.execute(f'SELECT price FROM property WHERE propertyId = {curr_property_id}')
        last_price = c.fetchone()
        if (last_price and curr_price != last_price) or not last_price:
            c.execute('REPLACE INTO property ('
                      'propertyId,'
                      'status, '
                      'address, '
                      'agent, '
                      'bedroom, '
                      'price) '
                      'VALUES (?,?,?,?,?,?)', instance)
            c.execute('INSERT INTO price_history ('
                      'propertyId,'
                      'price, '
                      'date)'
                      'VALUES (?,?,?)', (curr_property_id, curr_price, date.today()))
    conn.commit()


def get_total_num(conn):
    c = conn.cursor()
    c.execute('SELECT count (1) from property')
    return c.fetchall()


def read_all_from_property(conn):
    c = conn.cursor()
    c.execute('SELECT '
              'propertyId,'
              'status,'
              'address, '
              'agent, '
              'bedroom, '
              'price FROM property')
    return c.fetchall()


def read_all_from_price_history(conn):
    c = conn.cursor()
    c.execute('SELECT '
              'propertyId,'
              'price, '
              'date FROM price_history')
    return c.fetchall()


def read_from_db(conn, sql_command):
    c = conn.cursor()
    c.execute(sql_command)
    conn.commit()
    return c.fetchall()


def update(conn):
    c = conn.cursor()
    c.execute('SELECT * FROM property')
    [print(row) for row in c.fetchall()]

    c.execute('UPDATE stuffToPlot SET value = (99) WHERE value = 8')

    c.execute('DELETE FROM stuffToPlot WHERE value =99')
    conn.commit()


def close_connection(conn):
    conn.close()
