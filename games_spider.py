import scrapy

class GamesSpider(scrapy.Spider):
    name = "games_spider"

    start_urls = [f"https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/{i}/" for i in range(1, 17)]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        titles = response.css(
            'span.psw-t-body.psw-c-t-1.psw-t-truncate-2.psw-m-b-2::text').getall()
        prices = response.css('span.psw-m-r-3::text').getall()

        for title,price in zip(titles,prices):
            yield{
                'title':title.strip(),
                'price':price.strip().replace('\xa0', ' ')
            }