
import streamlit as st

from page.widgets.active import edit_active
from page.widgets.number import edit_number


def volume_oscillator_settings(scope):
	
	schema_key = 'vol_osssy'
	schema_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, schema_group, schema_key)
	with col2:edit_number(scope, schema_group, schema_key, 'fast' )
	with col3:edit_number(scope, schema_group, schema_key, 'slow' )
	