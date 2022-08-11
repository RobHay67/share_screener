import streamlit as st


from widgets.active import edit_active





def render_dividends(scope):
	# st.markdown('##### Dividends')
	column_adder = 'dividends'
	type_config = 'charts'

	edit_active(scope, type_config, column_adder)
	st.markdown("""---""")


