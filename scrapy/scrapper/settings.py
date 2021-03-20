BOT_NAME = 'scrapper'

SPIDER_MODULES = ['scrapper.spiders']
NEWSPIDER_MODULE = 'scrapper.spiders'

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