import scrapy
class MPMOilSpider(scrapy.Spider):
    name= 'mpmoil_spider'
    start_urls = ["http://products.mpmoil.nl/?&language=en"]

    def parse(self,response):
        urls = response.ccs('.product;attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url.parse_details)

    def parse_details(self,response):
        yield{
            'Description': response.css('div#productDescription').extract_first(),
            'Specs': response.css('div#productSpecs').extract_first(),
            'PackingUnits': response.css('div#productItems').extract_first(),
            'Title': response.css('div#title').extract_first(),
        }