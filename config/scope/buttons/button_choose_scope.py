import logging
import streamlit as st


def scope_button(scope, scope_key, scope_value, make_red=False, suffix_only=True):
	logging.debug(f"_scope_button > {scope_key}")
	# Render a button and give it a unique name
	widget_key = 'widget>' + scope_key
	button_type = 'primary' if make_red else 'secondary'

	if suffix_only:
		# Extract the last item in the string which is seperated by either a [ or a .
		last_bracket = '['+scope_key.rsplit('[',1)[-1]
		last_dot = scope_key.rsplit('.', 1)[-1]
		button_label = last_bracket if len(last_bracket) < len(last_dot) else last_dot
		button_label = ':orange['+button_label+']'
	else:
		button_label = scope_key

	button = st.button(
		label=button_label, 
		key=widget_key, 
		use_container_width=True, 
		type=button_type,
		on_click=set_scope_button, 
		args=(scope, widget_key, scope_value, ),
		)
	return button


def set_scope_button(scope:dict, widget_key:str, scope_value, ):
	logging.warning("set_scope_button")
	previous_value = scope.display['config_key']
	if previous_value == widget_key: 
		scope.display['config_key'] = None
		scope.display['config_value'] = None
	else:
		scope.display['config_key'] = widget_key
		scope.display['config_value'] = scope_value



