import streamlit as st

from screener.views.active_trials.builder import build_english_explanation


def show_active_trials(scope):
	# Introduction
	col1,col2 = st.columns([4,8])
	with col1:st.subheader('Trials (Tests) - active only')
	with col2:st.write('https://www.investopedia.com/articles/active-trading/041814/four-most-commonlyused-indicators-trend-trading.asp')

	first_row = True
	col1,col2,col3,col4,col5 = st.columns([2,1,7,1,1])
	# headings
	with col1:st.caption('Trial Name')
	with col2:st.caption('-- and ---')
	with col3:st.caption('Criteria (english explanation)')
	with col4:st.caption('Definition')
	with col5:st.caption('Config Ref')
	st.divider()

	for trial in scope.trials['active_list']:

		connector = 'and ------- >'
		if first_row : connector, first_row = ('....', False)
		definition = scope.trials['user_config'][trial]['definition']
	
		with col1: st.write(scope.trials['user_config'][trial]['short_name'])	
		english_explanation = build_english_explanation(scope, trial)
		with col2: st.write(connector)
		with col3: st.write(english_explanation)
		with col4: st.write("[defintion]("+definition+")")
		with col5: st.write(trial)

	


