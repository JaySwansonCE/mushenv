import scrapy

class GenusSpider(scrapy.Spider):
	name = "geni"
	allowed_domains = ['en.wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/Category:Lists_of_fungal_species',]

	def parse(self, response):
		count_of_divs_parent = len(response.xpath('//*[@id="mw-pages"]/div/div/div'))
		print('THIS IS THE COUNT OF PARENT: ' + str(count_of_divs_parent))
		while count_of_divs_parent > 0:
			count_of_divs_child = len(response.xpath('//*[@id="mw-pages"]/div/div/div[' + str(count_of_divs_parent) + ']/ul/li'))
			print('THIS IS THE COUNT OF CHILD: ' + str(count_of_divs_child))
			while count_of_divs_child > 0:
				yield {
					'genus_link': response.xpath('//*[@id="mw-pages"]/div/div/div[' + str(count_of_divs_parent) + ']/ul/li[' + str(count_of_divs_child) + ']/a/@href').extract_first()
				}
				count_of_divs_child = count_of_divs_child - 1
			count_of_divs_parent = count_of_divs_parent - 1





	


			

		


