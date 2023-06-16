from pathlib import Path

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    # Override
    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]

        for url in urls:
            yield scrapy.Request(url, self.parse)

    # Override
    def parse(self, res):
        # page = res.url.split('/')[-2]
        # filename = f"quotes-{page}.html"
        # Path(filename).write_bytes(res.body)
        # self.log(f"Saved file {filename}")
        for quote in res.css("div.quote"):
            yield {
                "text" : quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
