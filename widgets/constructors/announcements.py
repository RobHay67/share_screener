import streamlit as st


from widgets.active import edit_active



def render_announcements(scope):
	# st.markdown('##### Announcements')
	col_adder = 'announcements'
	config_name = 'charts'

	edit_active(scope, config_name, col_adder)
	st.markdown("""---""")


