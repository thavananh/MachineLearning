import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath('.//text()').extract_first()
            link = country.xpath('.//@href').extract_first()

            # absolute_url = f'https://www.worldometers.info/world-population/{link}'
            absolute_url = response.urljoin(link)

            yield scrapy.Request(url=absolute_url, callback=self.parse_country, meta={'country_name': country_name})

    def parse_country(self, response):
        #(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]
        country = response.meta['country_name']
        table_rows = response.xpath('(//table[contains(@class, "table")])[1]/tbody/tr')
        for row in table_rows:
            year = row.xpath('./td[1]/text()').get()
            population = row.xpath('./td[2]/strong/text()').get()
            yearly_percent_change = row.xpath('./td[3]/text()').get()
            yearly_change = row.xpath('./td[4]/text()').get()
            migrants = row.xpath('./td[5]/text()').get()
            median_age = row.xpath('./td[6]/text()').get()
            fertility_rate = row.xpath('./td[7]/text()').get()
            density = row.xpath('./td[8]/text()').get()
            urban_population_percent = row.xpath('./td[9]/text()').get()
            urban_population = row.xpath('./td[10]/text()').get()
            country_share_of_world_population = row.xpath('./td[11]/text()').get()
            world_population = row.xpath('./td[12]/text()').get()
            country_population_rank = row.xpath('./td[13]/text()').get()
            yield {
                'country': country,
                'year': year,
                'population': population,
                'yearly_percent_change': yearly_percent_change,
                'migrants': migrants,
                'median_age': median_age,
                'fertility_rate': fertility_rate,
                'density': density,
                'urban_population_percent': urban_population_percent,
                'urban_population': urban_population,
                'country_share_of_world_population': country_share_of_world_population,
                'world_population': world_population,
                'country_population_rank': country_population_rank
            }