


import streamlit as st

# ==============================================================================================================================================================
# Company Research Render Controller
# ==============================================================================================================================================================
def render_research_page(scope):
	st.header('Company Research')
	render_data_loader(scope, 'research' )
	st.markdown("""---""")
	
	ticker = scope.ticker['research']

	if ticker != 'select a ticker':	
		meta_data, info, divs = fetch_yfinance_metadata(ticker)

		render_company_general_info(info)
		render_dividend_info(divs)
		render_fundamental_info(info)
		render_general_meta_data(info)
		plot_basic_chart(scope)		
		render_market_info(info)
		# render_ticker_file(scope)
		render_ticker_file(scope, ticker)



