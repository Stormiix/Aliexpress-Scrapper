import scrapy



testurl = "https://www.aliexpress.com/item/Original-LEAGOO-M8-3G-Mobile-Phone-Android-6-0-MTK6580A-Quad-Core-1-3GHz-RAM-2GB/32772354059.html"

class AliSpider(scrapy.Spider):
    name = "aliexpress"
    start_urls = [
        testurl,
    ]
    
    def process_links(self, links):
        for link in links:
            link.url = "http://localhost:8050/render.html?" + urlencode({ 'url' : link.url })
        return links

    def parse(self, response):
        product = response.css('div.p-price-content.notranslate')
        yield {
            'product_name': response.css('h1.product-name::text').extract_first(),
            'product_price': product.css('span.p-price::text').extract_first(),
            'product_currency': product.css('span.p-symbol::text').extract_first(),
            'product_stock':response.xpath('//em[@id="j-sell-stock-num"]/text()').extract()
        }
