import scrapy


class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["www.reclameaqui.com.br"]
    start_urls = ["http://www.reclameaqui.com.br/"]
    result = []

    def parse(self, response):
        for title in response.xpath("/html//div[@class='sc-lsm4sxr-0 jLKCJu']"):
            good_title = title.xpath("span[@a='text']/text()").get()
            self.result.append(good_title)

        with open("result.txt", "w") as my_file:
            print(my_file.write(self.result))