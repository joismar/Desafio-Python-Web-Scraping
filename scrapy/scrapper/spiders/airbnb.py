import scrapy
import re
import json

class AirBnbSpyder(scrapy.Spider):
	'''
	use scrapy crawl airbnb -a loc=<city>-<state>-<country>
	'''
	name = 'airbnb'
	
	def __init__(self, loc='Borá-SP-Brasil', *args, **kwargs):
			super(AirBnbSpyder, self).__init__(*args, **kwargs)
			self.loc = loc
			
			# Passo 1 e 2
			# OBS: Como os filtros são apenas a localidade, encontrei uma forma de buscar apenas
			# pela URL sem necessidade de 
			self.start_urls = [f'https://www.airbnb.com.br/s/{self.loc}/homes']

			self.total_star = 0
			self.total_price = 0
			self.total = 0
		
	def parse(self, response):
		rooms = response.xpath("*//div/a[contains(@href, '/rooms')]/following-sibling::div[2]")
		self.total = len(rooms)

		for room in rooms:
			
			# Parte 3
			av = room.xpath('./div[5]/div/span/span[3]/text()[2]')
			star = room.xpath('./div[5]/div/span/span[2]/text()')

			price = list(filter(
				lambda item: 
					re.search(r'(?<=\$)\d+', item),
					room.xpath('./div[5]//text()').getall()
			))

			self.total_star += 0 if not star else float(star.get().strip())
			self.total_price += 0 if not price else float(price[0].split('$')[1])

			# Parte 4
			yield {
				"titulo": room.xpath('./div/div/div[2]/text()').get().strip(), 
				"qtd_avaliacoes:": None if not av else av.re('\d+')[0], 
				"qtd_estrelas": None if not star else star.get().strip(),
				"preco": price[0],
			}


	def closed(self, reason):
		if reason == 'finished':
			self.calcAvg()


	def calcAvg(self):
		self.saveAvg(
			{
				'price_avg': self.total_price/self.total,
				'star_avg': self.total_star/self.total
			}
		)

	def saveAvg(self, avg):
		# Parte 5
		with open(f'joismar_{self.name}_resumo.json', 'w') as result_avg_file:
			result_avg_file.write(json.dumps({
				'TOTAL': self.total,
				'AVG': avg
			}))



