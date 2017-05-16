import scrapy
from scrapy_splash import SplashRequest

testurl = "https://www.aliexpress.com/item/Original-LEAGOO-M8-3G-Mobile-Phone-Android-6-0-MTK6580A-Quad-Core-1-3GHz-RAM-2GB/32772354059.html"
# scrapy crawl AliSpider -o products.json
class AliSpider(scrapy.Spider):
    name = "AliSpider"
    start_urls = [
        testurl,
    ]
    def numbers_only(*str):
        return [int(s) for s in str[1].split() if s.isdigit()]
    def start_requests(self):
            for url in self.start_urls:
                yield SplashRequest(url, self.parse,
                    endpoint='render.html',
                    args={'wait': 10},
                )
    def parse(self, response):
        product = response.css('div.p-price-content.notranslate')
        selector = scrapy.Selector(response=response, type="html")
        yield {
            'product_name': response.css('h1.product-name::text').extract_first(),
            'product_price': float(product.css('span.p-price::text').extract_first()),
            'product_currency': product.css('span.p-symbol::attr(content)').extract_first(),
            'product_stock': self.numbers_only(response.xpath('//em[@id="j-sell-stock-num"]/text()').extract_first())[0],
            'product_attr': response.xpath('//ul[@id="j-sku-list-3"]/li/a/@title').extract(),
            'product_description_long': selector.xpath("//div[@id='j-product-description']/*").extract()
            }
#"//div[@class='description-content']/text()"
