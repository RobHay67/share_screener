import logging

def scope_display(scope):
	logging.debug("scope_display")
	scope.display = {}
	scope.display['page'] = 'streamlit_app'
	scope.display['config_page'] = 'Rob'
	scope.display['config_key'] = None
	scope.display['config_value'] = None