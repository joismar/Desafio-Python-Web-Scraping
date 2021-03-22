import scrapy
import re
import json

class AirBnbSpider(scrapy.Spider):
	'''
	Use "scrapy crawl airbnb"
	Adicione "-a loc=<Cidade>-<SIGLAESTADO>-<Pais>" para especificar o local da pesquisa
	'''
	name = 'airbnb'
	
	def __init__(self, loc='Borá-SP-Brasil', *args, **kwargs):
			super(AirBnbSpider, self).__init__(*args, **kwargs)
			self.loc = loc
			
			# Passo 1 e 2
			# OBS: Como os filtros é apenas de localidade, encontrei uma forma de buscar apenas
			# pela URL sem necessidade de fazer uma interceptação por requests, acredito que seria
			# nesse momento que o Splash seria útil, mas sinceramente não li o suficiente sobre ele
			# e não achei necessário.
			self.start_urls = [f'https://www.airbnb.com.br/s/{self.loc}/homes']

			# Aqui inicializei algumas variáveis pra o cálculo das médias
			self.total_star = 0
			self.total_price = 0
			self.total = 0

			# Existe possibilidade do estabelecimento não ter estrelas, então criei um contador específico
			self.total_for_stars = 0
		
	def parse(self, response):
		# Parte 3
		# Infelizmente não sou muito fã de capturar elementos pela sua posição, mas no caso de classes
		# e ids gerados aleatoriamente foi necessário
		rooms = response.xpath("*//div/a[contains(@href, '/rooms')]/following-sibling::div[2]")
		self.total = len(rooms)

		for room in rooms:
			av = room.xpath('./div[5]/div/span/span[3]/text()[2]')
			star = room.xpath('./div[5]/div/span/span[2]/text()')

			# Esse foi um método de busca por regex para dinamizar a busca do preço, nesse caso a busca
			# por posição era ineficiente pois tinha uma div que podia desaparecer
			price = list(filter(
				lambda item: 
					re.search(r'(?<=\$)\d+', item),
					room.xpath('./div[5]//text()').getall()
			))

			# Somei os totais
			self.total_star += 0 if not star else float(star.get().strip())
			self.total_for_stars += 0 if not star else 1

			self.total_price += 0 if not price else float(price[0].split('$')[1])

			# Parte 4
			yield {
				"titulo": room.xpath('./div/div/div[2]/text()').get().strip(), 
				"qtd_avaliacoes:": None if not av else av.re('\d+')[0], 
				"qtd_estrelas": None if not star else star.get().strip(),
				"preco_rs": price[0].split('$')[1],
			}

	# Método é chamado se o bot terminar com sucesso e calcula as médias
	def closed(self, reason):
		if reason == 'finished':
			self.calcAvg()

	# Método realiza o cálculo das médias
	def calcAvg(self):
		self.saveAvg(
			{
				'price_avg': round(self.total_price/self.total, 2),
				'star_avg': round(self.total_star/self.total_for_stars, 2)
			}
		)

	# Método sobrescreve o arquivo de médias
	def saveAvg(self, avg):
		# Parte 5
		with open(f'joismar_{self.name}_resumo.json', 'w') as result_avg_file:
			result_avg_file.write(json.dumps({
				'TOTAL': self.total,
				'AVG': avg
			}))



