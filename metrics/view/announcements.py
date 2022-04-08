import streamlit as st


from widgets.active import edit_active



def render_announcements(scope):
	# st.markdown('##### Announcements')
	metric = 'announcements'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	st.markdown("""---""")


