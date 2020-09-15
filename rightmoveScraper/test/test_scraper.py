from rightmoveScraper import scraper
import unittest


class TestScraper(unittest.TestCase):

    def test_scraper(self):
        target_web = 'https://www.rightmove.co.uk/property-for-sale/find.html?' \
                     'locationIdentifier=OUTCODE%5E1569&index=0&propertyTypes=' \
                     '&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords='
        soups = scraper.pre_soup(target_web)
        blocks = scraper.get_block(soups[0])
        info = [scraper.get_info(block) for block in blocks]
        print(info)
        # self.assertEqual(info, '')

    def test_web_requests(self):
        target_web = 'https://www.rightmove.co.uk/property-for-sale/find.html?' \
                     'locationIdentifier=OUTCODE%5E1569&index=0&propertyTypes=' \
                     '&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords='
        soups = scraper.pre_soup(target_web)
        total_num = scraper.get_count(soups[0])
        print(total_num)
        for index in range(total_num // 24 + 1):
            if index == 42:
                break
            nextPage = target_web.replace('index=0', f'index={index * 24}')
            print(nextPage)
            soups = scraper.pre_soup(nextPage)


if __name__ == '__main__':
    unittest.main()


