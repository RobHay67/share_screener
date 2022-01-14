import streamlit as st


from metrics.model.set_active import edit_active
from metrics.model.set_number import edit_number


def render_stochastic(scope):
	st.markdown('##### Stochastic Oscillator')
	metric = 'stochastic'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_number(scope, config_name, metric, 'lookback_days' )
	edit_number(scope, config_name, metric, 'slow' )
	edit_number(scope, config_name, metric, 'signal' )
	st.markdown("""---""")


