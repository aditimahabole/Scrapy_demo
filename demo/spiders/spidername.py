import scrapy
class WatchWebsiteSpider(scrapy.Spider):
    name = 'spidername'
    allowed_domains = ['www.watchfinder.co.uk']
    start_urls = ['https://www.watchfinder.co.uk/Rolex/Daytona/16520/5559/item/239910']

    def parse(self, response):
        brand = response.xpath("(//div[@class='product--details']/h1/span[1]/text())[1]").get()
        name = response.xpath("(//div[@class='product--details']/h1/span[2]/text())[1]").get()
        modelNo= response.xpath("(//div[@class='product--details']/h1/span[3]/text())[1]").get()
        price = response.xpath("//div[@class='product--details']/span/text()").get()
        box = response.xpath("//div[@id='specification-content']/table/tbody/tr[1]/td[2]/text()").get()
        papers = response.xpath("//div[@id='specification-content']/table/tbody/tr[2]/td[2]/text()").get()
        year = response.xpath("//div[@id='specification-content']/table/tbody/tr[3]/td[2]/text()").get()
        product_code= response.xpath("//div[@id='specification-content']/table/tbody/tr[4]/td[2]/text()").get()
        watchFinder_warranty = response.xpath("//div[@id='specification-content']/table/tbody/tr[5]/td[2]/text()").get()
        case_size= response.xpath("//div[@id='specification-content']/table/tbody/tr[6]/td[2]/text()").get()
        case_material= response.xpath("//div[@id='specification-content']/table/tbody/tr[7]/td[2]/text()").get()
        movement= response.xpath("//div[@id='specification-content']/table/tbody/tr[8]/td[2]/text()").get()
        bracelet_material= response.xpath("//div[@id='specification-content']/table/tbody/tr[9]/td[2]/text()").get()
        dial_type= response.xpath("//div[@id='specification-content']/table/tbody/tr[10]/td[2]/text()").get()
        water_resistance= response.xpath("//div[@id='specification-content']/table/tbody/tr[11]/td[2]/text()").get()
        location= response.xpath("//div[@id='specification-content']/table/tbody/tr[12]/td[2]/text()").get()
        yield{
            'Brand':brand,
            'Name':name,
            'ModelNo':modelNo,
            'Price':price,
            'Box':box,
            'Paper':papers,
            'Year':year,
            'Product_code':product_code,
            'WatchFinder warranty':watchFinder_warranty,
            'Case Size':case_size,
            'Case Material':case_material,
            'Movement':movement,
            'Bracelet Material':bracelet_material,
            'Dial Type':dial_type,
            'Water Resistance':water_resistance,
            'Location':location
        }
