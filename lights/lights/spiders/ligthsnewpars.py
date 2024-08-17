import scrapy


class LigthsnewparsSpider(scrapy.Spider):
    name = "ligthsnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/potolocnye-svetilniki"]

    def parse(self, response):
        ligths = response.css('div.wYUX2')
        for ligth in ligths:
            # Используем оператор yield для возвращения результатов
            yield {
                # Получаем название светильника
                'name': ligth.css('div.wYUX2 span::text').get(),
                # Получаем цену светильника
                'price': ligth.css('div.q5Uds.fxA6s span::text').get(),
                # Получаем URL светильника
                'url': ligth.css('a::attr(href)').get()
            }
