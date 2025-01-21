import streamlit as st


def data_type_button(scope, button_type, number=1):
	widget_key = 'widget>'+button_type+str(number)
	match button_type:
		case 'blank'		:button_label = ' '
		case 'dict'			:button_label=":blue[{ }]"
		case 'list'			:button_label=":orange[[ list ]]"
		case 'string'		:button_label=":orange['string']"
		case 'integer'		:button_label=":green[integer]"
		case 'true_false'	:button_label=":blue[True or False]"
		case 'password'		:button_label=":red[*********]"
		case _				:button_label=":red[ERROR]"

	button = st.button(
		label=button_label, 
		key=widget_key, 
		use_container_width=True, 
		type='secondary',
		)
	return button
