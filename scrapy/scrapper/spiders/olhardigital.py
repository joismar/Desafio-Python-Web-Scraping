import scrapy

class OlharDigitalSpyder(scrapy.Spider):
	'''
	use scrapy crawl olhardigital -a qtde=<QTDE>
	'''
	name = 'olhardigital'

	# Passo 1
	start_urls = ['https://olhardigital.com.br/']

	def __init__(self, qtde=5, *args, **kwargs):
			super(OlharDigitalSpyder, self).__init__(*args, **kwargs)
			self.qtde = int(qtde)

	def parse(self, response):
		# Passo 2
		# OBS: Existe a possibilidade da ordem ser alterada, nesse caso acredito que seria  
		# mais eficiente o uso do xpath selector "*//li/a[text()[contains(., 'Coronavírus')]]".
		# OBS²: Poderiamos também iniciar o bot diretamente no desse link se a idéia for  
		# capturar a partir dessa página.
		yield response.follow(response.css('ul.menu > li:nth-child(3) > a')[0], self.parse)

		for post_link in response.css('div.text > a')[:self.qtde]:
			# Parte 3
			yield scrapy.Request(post_link.attrib['href'], callback=self.parsePost)

	def parsePost(self, response):
		# Parte 4
		# OBS: Não tem subtitle e time na página da postagem
		yield {
			'title': response.css('div.text > h1::text').get().strip(), 
			'subtitle': None, 
			'date': response.css('span.date::text').get().strip(), 
			'time': None
		}
			

