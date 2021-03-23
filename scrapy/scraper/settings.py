BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

FEEDS = {
	'joismar_%(name)s.json': {
		'format': 'json',
		'encoding': 'utf8',
		'store_empty': False,
		'fields': None,
		'indent': 4,
		'overwrite': True,
		'item_export_kwargs': {
			'export_empty_fields': True,
		},
	}
}