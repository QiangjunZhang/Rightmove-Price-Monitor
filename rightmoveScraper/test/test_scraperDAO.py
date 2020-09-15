import unittest
from datetime import date

from rightmoveScraper import scraperDAO as db


class TestScraperDAO(unittest.TestCase):

    def test_insert_entry(self):
        conn = db.open_connection()
        db.create_table(conn)
        pId = 111
        stat = 'add on 2001'
        addr = 'Manchester'
        agen = 'WREN'
        bed = 2
        price = 1000
        instance_list = [(pId, stat, addr, agen, bed, price)]
        db.add_data_entry(conn, instance_list)
        self.assertTrue(db.read_all_from_property(conn),
                        [('111', 'add on 2001', 'Manchester', 'WREN', 2.0, 1000.0)])
        self.assertTrue(db.read_all_from_price_history(conn),
                        [('111', 1000.0, date.today())])

        db.close_connection(conn)

    def test_update_entry(self):
        conn = db.open_connection()
        db.create_table(conn)
        pId = 111
        stat = 'add on 2001'
        addr = 'Manchester'
        agen = 'WREN'
        bed = 2
        price1 = 1000
        price2 = 2000
        instance_list = [(pId, stat, addr, agen, bed, price1),
                         (pId, stat, addr, agen, bed, price2)
                         ]

        db.add_data_entry(conn, instance_list)
        self.assertTrue(db.read_all_from_property(conn),
                        [('111', 'add on 2001', 'Manchester', 'WREN', 2, 2000)])
        self.assertTrue(db.read_all_from_price_history(conn),
                        [('111', 1000, date.today()),
                         ('111', 2000, date.today())
                         ])

        db.close_connection(conn)


if __name__ == '__main__':
    unittest.main()
