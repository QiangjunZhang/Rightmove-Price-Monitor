import sqlite3


conn = sqlite3.connect('housePrice.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS property(propertyId INTEGER CONSTRAINT constraint_name PRIMARY KEY, status VARCHAR, \
                                                    address VARCHAR, agent VARCHAR, bedroom INTEGER, price INTEGER)')


def add_data_entry(pId, stat, addr, agen, bed, pric):
    add_command = f"REPLACE INTO property (propertyId, status, address, agent, bedroom, price) VALUES \
              ('{pId}', '{stat}', '{addr}', '{agen}', {bed}, {pric})"
    # print(add_command)
    c.execute(add_command)
    conn.commit()


def get_total_num():
    c.execute('SELECT count (1) from property')
    return c.fetchall()


def read_all():
    c.execute('SELECT * FROM property')
    return c.fetchall()


def read_from_db(sql_command):
    c.execute(sql_command)
    conn.commit()
    return c.fetchall()


def update():
    c.execute('SELECT * FROM property')
    [print(row) for row in c.fetchall()]

    c.execute('UPDATE stuffToPlot SET value = (99) WHERE value = 8')

    c.execute('DELETE FROM stuffToPlot WHERE value =99')
    conn.commit()


def clear_db(databaseName):
    c.execute(f'DELETE FROM {databaseName}')
    conn.commit()


def close_connection():
    c.close()
    conn.close()

