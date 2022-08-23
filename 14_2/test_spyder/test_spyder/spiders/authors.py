import scrapy
from ..items import ExportToDB


class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        items = ExportToDB()
        for quote in response.xpath("/html//div[@class='quote']"):
            good_quote = quote.xpath("span[@class='text']/text()").get()
            if (good_quote.endswith('”') == True) and (good_quote.startswith('“') == True):
                good_quote = good_quote[1:-1]
            items["keywords"] = quote.xpath("div[@class='tags']/a/text()").extract()
            items["author"] = quote.xpath("span/small/text()").extract()
            items["quote"] = good_quote
            items["link"] = str(self.start_urls[0]) + quote.xpath("span/a/@href").get()
            yield items
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)


