import streamlit as st


from views.two_cols import view_2_columns


def fundamental(info):
	st.markdown('##### Fundamental Info') 
		
	view_2_columns( 'Enterprise Value (AUD)', info['enterpriseValue'])
	view_2_columns( 'Enterprise To Revenue Ratio', info['enterpriseToRevenue'])
	view_2_columns( 'Enterprise To Ebitda Ratio', info['enterpriseToEbitda'])
	view_2_columns( 'Net Income (AUD)', info['netIncomeToCommon'])
	view_2_columns( 'Profit Margin Ratio', info['profitMargins'])
	view_2_columns( 'Forward PE Ratio', info['forwardPE'])
	view_2_columns( 'PEG Ratio', info['pegRatio'])
	view_2_columns( 'Price to Book Ratio', info['priceToBook'])
	view_2_columns( 'Forward EPS (AUD)', info['forwardEps'])
	view_2_columns( 'Beta', info['beta'])
	view_2_columns( 'Book Value (AUD)', info['bookValue'])
	view_2_columns( 'Dividend Rate (%)', info['dividendRate'])
	view_2_columns( 'Dividend Yield (%)', info['dividendYield'])
	view_2_columns( 'Five year Avg Dividend Yield (%)', info['fiveYearAvgDividendYield'])
	view_2_columns( 'Payout Ratio', info['payoutRatio'])


