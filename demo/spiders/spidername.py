import scrapy
class SpidernameSpider(scrapy.Spider):
    name = 'spidername'
    allowed_domains = ['www.watchfinder.co.uk']
    start_urls = ['http://www.watchfinder.co.uk/']

    def parse(self, response):
        items = response.xpath("/div[@data-testid='watchItem']").get()
        # items  give all watches so we can then make a loop and then store below data
        # for each watch

        url = response.xpath("(//div[@data-testid='watchItem']/a/@href)").get()
        price =  response.xpath("(//div[@data-testid='watchPrice']/text())").get()
        box_value = response.xpath("(//span[@data-testid='watchBoxValue']/text())").get()
        paper_value = response.xpath("(//span[@data-testid='watchPapersValue']/text())").get()
        year_value = response.xpath("(//span[@data-testid='watchYearValue']/text())").get()
        model_number = response.xpath("(//div[@data-testid='watchModelNumber']/text())").get()

        
        
        yield{
            'url':url,
            'price':price,
            'box':box_value,
            'paper':paper_value,
            'year':year_value,
            'modelNo':model_number,
        }

