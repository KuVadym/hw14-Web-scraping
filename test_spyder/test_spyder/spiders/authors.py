import scrapy
import json 


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["academy.cs.cmu.edu"]
    page = "docs"
    start_urls = ["http://academy.cs.cmu.edu/docs"]

    def parse(self, response):
        data = json.loads(response.text)
        print("start data")
        print(data)
        print("end data")

        # for quote in data["quotes"]:
        #     yield {"quote": quote["text"]}
        # if data["has_next"]:
        #     self.page += 1
        #     url = f"https://quotes.toscrape.com/api/quotes?page={self.page}"
        #     yield scrapy.Request(url=url, callback=self.parse)