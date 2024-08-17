import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        divans = response.css('div._Ud0k')

        # Настраиваем работу с каждым отдельным диваном в списке
        for divan in divans:
            # Используем оператор yield для возвращения результатов
            yield {
                # Получаем имя дивана
                'name': divan.css('div.lsooF span::text').get(),
                # Получаем цену дивана
                'price': divan.css('div.pY3d2 span::text').get(),
                # Получаем URL дивана
                'url': divan.css('a::attr(href)').get()
            }
