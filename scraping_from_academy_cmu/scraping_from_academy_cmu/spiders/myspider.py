import scrapy
from scrapy_splash import SplashRequest


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    handle_httpstatus_all = True
    allowed_domains = ["academy.cs.cmu.edu"]
    start_urls = ["http://academy.cs.cmu.edu/docs"]


    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})


    def parse(self, response):
        title = response.css('title::text').get()
        links = response.css('a::attr(href)').getall()
        print(title)
        print(links)
