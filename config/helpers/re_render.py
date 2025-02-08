import logging



def app_is_re_rendering():
	logging.warning("app_is_re_rendering")
	for i in range(10):print('')
	print ( '\033[94m' + 'Application Re-Rendering - see below this line ' + '>'*33 + '\033[0m')

	print(  '\033[94m' + 'Debug    > Render components (buttons / dropdowns)' + '\033[0m')
	print(  '\033[94m' + 'Info     > Render main pages (Controllers / Routers)' + '\033[0m')
	print(  '\033[94m' + 'Warning  > Python Functions' + '\033[0m')
	print(  '\033[94m' + 'Error    > Actual Errors or unexpected results (look into these)' + '\033[0m')
	print(  '\033[94m' + 'Critical > TODOs or placeholders notes that are currently being worked upon' + '\033[0m')

	for i in range(5):print('')