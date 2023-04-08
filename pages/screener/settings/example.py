import streamlit as st


def example_settings(scope):
	
	st.header('Analysis Selection Criteria')

	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns([1,1,1,1,1,1,1,1,1])

	with col1:st.markdown('#### Analysis')
	with col2:st.markdown('#### Trending')
	with col3:st.markdown('#### No of Instances')
	with col4:st.markdown('#### Over qty of Days')
	with col5:st.markdown('#### Percentage')
	with col6:st.markdown('#### Analysis')
	with col7:st.markdown('#### Analysis')
	with col8:st.markdown('#### Find Best')
	with col9:st.markdown('#### Use this Analysis')
	


	with col1:st.write('Volume')
	with col2:st.write('Down')
	with col3:st.write('2')
	with col4:st.write('5')
	with col5:st.write('-')
	with col6:st.write('Vol up 20%')
	with col9:st.write('tick this')

	with col1:st.write('AGM')
	with col2:st.write('After or Before')
	with col5:st.write('21')
	with col9:st.write('tick this')

	with col1:st.write('Dividend Ex Date (and cum?)')
	with col2:st.write('After or Before')
	with col5:st.write('21')
	with col9:st.write('tick this')

	with col1:st.write('SMA - 21')
	with col2:st.write('Above')
	with col5:st.write('-')

	with col9:st.write('tick this')


	with col1:st.write('RSI')
	with col2:st.write('Above')
	with col5:st.write('50 % - (slider control)')

	with col9:st.write('tick this')

	with col1:st.write('Stochastic Oscillator')
	with col2:st.write('Above')
	with col5:st.write('80 % - (slider control)')

	with col9:st.write('tick this')

	with col1:st.write('MACD (maybe its own section)')
	with col2:st.write('Up')
	with col2:st.write('MACD Strength S or W ')

	with col9:st.write('tick this')

	with col1:st.write('MACD (Volume')
	with col2:st.write('Up')
	with col2:st.write('MACD Strength S or W ')
	with col2:st.write('Cross Over Points')

	with col9:st.write('tick this')


	st.markdown("""---""")

	st.button('Determine Tickers meeting the above Criteria')






	# with col1:st.write('Open')
	# with col2:st.write('Up or Down')
	# with col3:st.write('4')
	# with col4:st.write('10')
	# with col5:st.write('-')
	# with col6:st.write('-')
	# with col8:st.button('Find Best Options')
	# with col9:st.write('tick this')

	# with col1:st.write('High')
	# with col2:st.write('Up')
	# with col3:st.write('8')
	# with col4:st.write('12')
	# with col5:st.write('-')
	# with col6:st.write('-')
	# with col9:st.write('tick this')

	# with col1:st.write('Low')
	# with col2:st.write('Up')
	# with col3:st.write('7')
	# with col4:st.write('10')
	# with col5:st.write('-')
	# with col6:st.write('-')
	# with col9:st.write('tick this')

	# with col1:st.write('Close')
	# with col2:st.write('Down')
	# with col3:st.write('3')
	# with col4:st.write('5')
	# with col5:st.write('-')
	# with col6:st.write('-')
	# with col9:st.write('tick this')