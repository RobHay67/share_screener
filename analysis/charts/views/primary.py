import streamlit as st


from analysis.charts.views.components import render_activate_chart, render_announcements, render_bollinger_bands, render_dividends, render_moving_average



def view_primary(scope):
	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
	with col1: st.header('Primary Charts')
	with col1: st.write('renders on all analysis pages')
	with col2: 
		st.write(' ')
		st.write('.')
		render_activate_chart(scope, 'candlestick')
	with col3: 
		st.write(' ')
		st.write('.')
		render_activate_chart(scope, 'scatter')
	with col4: 
		st.write(' ')
		st.write('.')
		render_activate_chart(scope, 'bar')
	with col5: 
		st.write(' ')
		st.write('.')
		render_activate_chart(scope, 'line')  		# TODO I tried embedding the data_cols in the line grpah - see if this works
	with col6: 
		st.write(' ')
		st.write('.')
		render_activate_chart(scope, 'heiken_ashi')


	st.markdown("""---""")
	# col1,col2 = st.columns([3,7])
	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
	with col1: st.subheader('Overlays')
	with col2: 
		st.write(' ')
		st.write('applies to all of the above selected Primary Charts')
	st.markdown("""---""")
	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
	with col1: st.markdown('##### Dividends')
	with col2: st.markdown('##### Announcements')
	with col3: st.markdown('##### Bollinger Bands')
	with col4: st.markdown('##### Simple Moving Averages (SMA)')
	with col5: st.markdown('##### Exponential Moving Averages (EMA)')
	# with col6: st.markdown('##### Dividends')

	# st.markdown("""---""")

	# col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])

	with col1: render_dividends(scope)
	with col2: render_announcements(scope)
	with col3: render_bollinger_bands(scope)
	with col4:
		# st.markdown('##### Simple Moving Averages (SMA)')
		render_moving_average(scope, 'sma_1')
		render_moving_average(scope, 'sma_2')
		render_moving_average(scope, 'sma_3')
	with col5:
		# st.markdown('##### Exponential Moving Averages (EMA)')
		render_moving_average(scope, 'ema_1')
		render_moving_average(scope, 'ema_2')
		render_moving_average(scope, 'ema_3')

