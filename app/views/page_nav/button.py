import streamlit as st




def button_page_link_chart(scope, ticker):
	page = 'chart'
	page_icon = '📊'
	widget_key = 'widget_navigate_to_' + page + '_page_for_' + ticker

	if st.button(
				label=page_icon,
				key=widget_key,
				use_container_width=True,
				):
		scope.page[page]['selectors']['ticker'] = ticker
		st.switch_page("charts/views/page_charts.py")
		
	# TODO - this works - but can we refactor into single functions





def link_to_page_button(scope, page, ticker):
	
	# st.write('This is the link_to_page_button')
	# st.switch_page("charts/views/page_charts.py")

	widget_key = 'widget_link_to_' + page + '_page_for_' + ticker
	# streamlit_page_name = page

	match page:
		case 'chart':app_desc = '📊'
		case 'volume':app_desc = '🔊'
		case 'intraday':app_desc = '🌤️'
		case 'research':app_desc = '🕵'
		case _:app_desc = page

	# if page == 'chart':
	# 	app_desc = '📊'
	# 	streamlit_page_name = 'charting'
	# elif page == 'volume':
	# 	app_desc = '🔊'
	# elif page == 'intraday':
	# 	app_desc = '🌤️'
	# elif page == 'research':
	# 	app_desc = '🕵'
	# else:
	# 	app_desc = page

	nav_button = st.button(
						label=app_desc,
						key=widget_key,
						use_container_width=True,
						# on_click=navigate_to_page, 
						# args=(scope, page, ),
						)
	
	st.write(nav_button)
	if nav_button:st.switch_page("charts/views/page_charts.py")




def navigate_to_page(scope, page):

	st.write('Navigate to > '+page)
	
	st.switch_page("charts/views/page_charts.py")


	# previous_value = scope.page[page]['render']['chart_settings']
	# new_value = True if previous_value == False else False

	# scope.page[page]['render']['chart_settings'] = new_value

	# if open_app_button:
	# 	if page != 'screener':	
	# 		scope.page[page]['selectors']['ticker'] = ticker
	# 	else:
	# 		scope.page[page]['selectors']['tickers'] = [ticker]
	# 		scope.page[page]['selectors']['industries'] = []
	# 		scope.page[page]['selectors']['market'] = 'select market'
	# 		scope.page[page]['search_results'] = {}

	# 	switch_page(streamlit_page_name)