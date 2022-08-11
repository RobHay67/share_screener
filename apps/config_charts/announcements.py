import streamlit as st


from widgets.active import edit_active



def render_announcements(scope):
	# st.markdown('##### Announcements')
	column_adder = 'announcements'
	type_config = 'charts'

	edit_active(scope, type_config, column_adder)
	st.markdown("""---""")


