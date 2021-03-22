from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import logger
import json
import re

class AirBnbBot():
	def __init__(self, headless=True, loc='Borá-SP-Brasil'):
		logger.setup_debug_log()
		self.log = logger.log
		self.loc = loc
		self.options = webdriver.ChromeOptions()
		self.items = []

		if headless:
			self.options.add_argument("--headless")

		self.driver = webdriver.Chrome(
			options = self.options
		)

		# Linhas para instanciar o browser com o selenium hub 
		#
		# self.og.info('Conectando ao driver remoto...')
		# 
		# self.driver = webdriver.Remote(
		#   command_executor = 'http://127.0.0.1:4444/wd/hub',
		#   desired_capabilities = {
		# 	  "browserName": "chrome",
		# 	  "platformName": "linux"
		#   },
		#		options = self.options
		# )

		self.startBot()


	def startBot(self):	
		try:
			self.log.info('Conectado com sucesso!')

			# Passo 1 e 2
			self.driver.get(f'https://www.airbnb.com.br/s/{self.loc}/homes')

			WebDriverWait(self.driver, 60).until(
				EC.presence_of_element_located(('xpath', "*//div/a[contains(@href, '/rooms')]/following-sibling::div[2]"))
			)

			# Parte 3
			# Infelizmente não sou muito fã de capturar elementos pela sua posição, mas no caso de classes
			# e ids gerados aleatoriamente foi necessário
			rooms = self.driver.find_elements_by_xpath("*//div/a[contains(@href, '/rooms')]/following-sibling::div[2]")

			i = 0
			while i < len(rooms):
				room = rooms[i]
				try:
					try:
						av = re.search(
							r'\d+',
							room.find_element_by_xpath('./div[5]/div/span/span[3]').text
						).group(0)
						star = room.find_element_by_xpath('./div[5]/div/span/span[2]').text
					except (NoSuchElementException, StaleElementReferenceException) as e:
						av = None
						star = None

					price = re.search(
						r'(?<=\$)\d+', 
						room.find_element_by_xpath('./div[5]').text
					).group(0)

					title = room.find_element_by_xpath('./div/div/div[2]').text

					self.items.append({
						'titulo': title.strip(),
						'qtd_avaliacoes': None if not av else int(av),
						'qtd_estrelas': None if not star else float(star.replace(',', '.')),
						'preco_rs': float(price)
					})

					self.log.info('Captured: ' + str(self.items[-1]))

					i += 1
				except (NoSuchElementException, StaleElementReferenceException) as e:
					self.log.error(e)
					self.log.info('Tentando denovo em 10 segundos...')
					self.driver.get(f'https://www.airbnb.com.br/s/{self.loc}/homes')
					sleep(10)

			self.driver.quit()

			self.saveItems(self.items)
			avg = self.calcAvg()
			self.saveAvg(avg)

		except Exception as e:
			self.driver.quit()
			self.log.error(e)

	# Método que salva o json
	def saveItems(self, items):
		with open(f'joismar_airbnb2.json', 'w') as result_file:
			result_file.write(json.dumps(items, indent=4))

	# Método realiza o cálculo das médias
	def calcAvg(self):
		# Aqui fiz outro método pra cálculo das médias, esse método tbm
		# podia ser utilizado com o spider
		total = len(self.items)
		total_for_stars = len([i for i in self.items if i['qtd_estrelas']])
		total_price = sum([i['preco_rs'] for i in self.items])
		total_star = sum([i['qtd_estrelas'] for i in self.items if i['qtd_estrelas']])

		return {
			'price_avg': round(total_price/total, 2),
			'star_avg': round(total_star/total_for_stars, 2)
		}

	# Método sobrescreve o arquivo de médias
	def saveAvg(self, avg):
		# Parte 5
		with open(f'joismar_airbnb2_resumo.json', 'w') as result_avg_file:
			result_avg_file.write(json.dumps({
				'TOTAL': len(self.items),
				'AVG': avg
			}))

if __name__ == '__main__':
	bot = AirBnbBot()