import matplotlib.pyplot as plt
from rightmoveScraper import scraperDAO as db


def get_properties():
    for row in db.read_all():
        print(row)


def get_total_num():
    print(db.get_total_num())


if __name__ == '__main__':
    get_properties()
    get_total_num()
    db.close_connection()
