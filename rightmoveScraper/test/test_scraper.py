from rightmoveScraper import scraper
import unittest


class TestScraper(unittest.TestCase):

    def test_insert_entry(self):
        target_web = 'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=POSTCODE' \
                     '%5E514951&radius=1.0&sortType=10&propertyTypes=&includeSSTC=true&mustHave=' \
                     '&dontShow=&furnishTypes=&keywords='
        soups = scraper.pre_soup(target_web)
        blocks = scraper.get_block(soups[0])
        info = [scraper.get_info(block) for block in blocks]
        print(info)
        # self.assertEqual(info, '')

if __name__ == '__main__':
    unittest.main()


