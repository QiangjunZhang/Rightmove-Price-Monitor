import unittest
from rightmoveScraper import scraperDAO as db


class TestScraperDAO(unittest.TestCase):

    def test_insert_entry(self):
        db.create_table()
        pId = 111
        stat = 'add on 2001'
        addr = 'Manchester'
        agen = 'WREN'
        bed = 2
        price = 1000
        db.add_data_entry(pId, stat, addr, agen, bed, price)
        self.assertTrue(db.read_all(), [('111', 'add on 2001', 'Manchester', 'WREN', 2.0, 1000.0)])
        db.close_connection()


if __name__ == '__main__':
    unittest.main()