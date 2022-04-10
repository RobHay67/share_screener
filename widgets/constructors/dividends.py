import streamlit as st


from widgets.active import edit_active





def render_dividends(scope):
	# st.markdown('##### Dividends')
	metric = 'dividends'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	st.markdown("""---""")

