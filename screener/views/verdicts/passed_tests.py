import streamlit as st
from screener.views.tab_names import determine_tab_names

from app.views.navigation.button import button_page_link
from app.views.navigation.links import website_hyperlink


def show_passing_verdicts(scope, no_of_verdicts, tab_group_size, verdict_list):
		# Render the Results (in tabs and there could be lots)
		st.subheader('Passing Test Results       (' + str(no_of_verdicts) + ') passed')
		list_of_tab_names = determine_tab_names(no_of_verdicts, tab_group_size)
		# Create Tabs and populate from verdicts
		tabs = st.tabs(list_of_tab_names)
		ticker_start = 0
		for i, tab in enumerate(tabs):
			tickers_for_tab = verdict_list[ticker_start:ticker_start+tab_group_size]
			ticker_start += tab_group_size
			with tab:
				for ticker in tickers_for_tab:
					col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13 = st.columns([1,4,1,1,1,1,1,1,1,1,1,1,1])
					
					company_name = scope.config['ticker_search'][ticker]
					with col1 :st.write(ticker)
					with col2 :st.write(company_name)
					with col3 :button_page_link(scope, 'chart', ticker)
					with col4 :button_page_link(scope, 'intraday', ticker)
					with col5 :button_page_link(scope, 'volume', ticker)
					with col6 :button_page_link(scope, 'research', ticker)
					with col7:
						# google = st.page_link("http://www.google.com", label="Google", icon="🌎")
						hyperlinks = ['one','two']
						widget_key = 'widget_'+ticker

						st.selectbox ( 
							label		='Market',
							options		=hyperlinks,
							# index		=pos_for_previous, 
							help		='Select an Entire Share Market for Analysis',
							on_change	=on_select_external_link,
							args		=(scope, widget_key, ),
							key			=widget_key,
						) 
					with col8:
						st.page_link("http://www.google.com", label="Google", icon="🌎")


					# with col7 :website_hyperlink(scope, 'eTrade', ticker)
					# with col8 :website_hyperlink(scope, 'asx', ticker)
					# with col9 :website_hyperlink(scope, 'google', ticker)
					# with col10:website_hyperlink(scope, 'yahoo', ticker)
					# with col11:website_hyperlink(scope, 'market index', ticker)
					# with col12:website_hyperlink(scope, 'hot copper', ticker)
					# with col13:website_hyperlink(scope, 'market watch', ticker)




def on_select_external_link(scope, widget_key):
	test = "[market watch](https://www.marketwatch.com/investing/stock/wbc/charts?countrycode=au)"
	changed_value = scope[widget_key]
	# print('^'*88)
	# print(changed_value)

	# store the selection
	# scope.page[page]['selectors']['tickers'] = []
	# scope.page[page]['selectors']['industries'] = []
	# scope.page[page]['selectors']['market'] = changed_value
	# scope.page[page]['search_results'] = {}

	# st.link_button
