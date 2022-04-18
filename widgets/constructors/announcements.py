import streamlit as st


from widgets.active import edit_active



def render_announcements(scope):
	# st.markdown('##### Announcements')
	expander = 'announcements'
	config_name = 'charts'

	edit_active(scope, config_name, expander)
	st.markdown("""---""")


