import streamlit as st


def show_too_many_verdicts(no_of_verdicts, number_of_tabs, tab_group_size):
	st.error('Too many passing verdicts ('+str(no_of_verdicts)+') to render.')
	st.write('Maximum No of Tabs           = '+str(number_of_tabs))
	st.write('Maximum Verdicts in each tab = '+str(tab_group_size))
	st.write('Limit = Tabs x Verdict per Tab = '+str(tab_group_size * number_of_tabs))
