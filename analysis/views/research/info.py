import streamlit as st
import pandas as pd

from pages.view.two_cols import view_2_columns



def company_general(metadata):
	col1,col2 = st.columns([5,7])
	with col1: 
		st.markdown('** Sector **: ' + metadata.info['sector'])
		st.markdown('** Industry **: ' + metadata.info['industry'])
		st.markdown('** Phone **: ' + metadata.info['phone'])
		st.markdown('** Address **: ' 
					+        metadata.info['address1'] 
					+ ', ' + metadata.info['city'] 
					+ ', ' + metadata.info['zip'] 
					+ ', ' + metadata.info['country']
					)
	st.markdown('** Website **: ' + metadata.info['website'])

def business_summary(metadata):
	sentences = metadata.info['longBusinessSummary'].split('. ')
	my_expander = st.expander(label='Business Summary', expanded=False)
	for sentence in sentences:
		with my_expander: st.write(sentence)


def fundamental(metadata):
	# col1,col2 = st.columns([5,7])
	my_expander = st.expander(label='Fundamental Information', expanded=False)
	with my_expander:
		view_2_columns( 'Enterprise Value (AUD)', metadata.info['enterpriseValue'])
		view_2_columns( 'Enterprise To Revenue Ratio', metadata.info['enterpriseToRevenue'])
		view_2_columns( 'Enterprise To Ebitda Ratio', metadata.info['enterpriseToEbitda'])
		view_2_columns( 'Net Income (AUD)', metadata.info['netIncomeToCommon'])
		view_2_columns( 'Profit Margin Ratio', metadata.info['profitMargins'])
		view_2_columns( 'Forward PE Ratio', metadata.info['forwardPE'])
		view_2_columns( 'PEG Ratio', metadata.info['pegRatio'])
		view_2_columns( 'Price to Book Ratio', metadata.info['priceToBook'])
		view_2_columns( 'Forward EPS (AUD)', metadata.info['forwardEps'])
		view_2_columns( 'Beta', metadata.info['beta'])
		view_2_columns( 'Book Value (AUD)', metadata.info['bookValue'])
		view_2_columns( 'Dividend Rate (%)', metadata.info['dividendRate'])
		view_2_columns( 'Dividend Yield (%)', metadata.info['dividendYield'])
		view_2_columns( 'Five year Avg Dividend Yield (%)', metadata.info['fiveYearAvgDividendYield'])
		view_2_columns( 'Payout Ratio', metadata.info['payoutRatio'])


def general(metadata):
	# st.markdown('##### General meta_data Info') 
	my_expander = st.expander(label='General Information', expanded=False)
	with my_expander:
		st.markdown('** Market **: ' + metadata.info['market'])
		st.markdown('** Exchange **: ' + metadata.info['exchange'])
		st.markdown('** Quote Type **: ' + metadata.info['quoteType'])



def market_info(metadata):
	my_expander = st.expander(label='Market Information', expanded=False)


	volume = str(metadata.info['volume'])
	averageVolume = str(metadata.info['averageVolume'])
	marketCap = str(metadata.info['marketCap'])
	floatShares = str(metadata.info['floatShares'])
	regularMarketPrice = str(metadata.info['regularMarketPrice'])
	bidSize = str(metadata.info['bidSize'])
	askSize = str(metadata.info['askSize'])
	sharesShort = str(metadata.info['sharesShort'])
	shortRatio = str(metadata.info['shortRatio'])
	sharesOutstanding = str(metadata.info['sharesOutstanding'])

	with my_expander:
		st.markdown('** Volume **: ' + volume)
		st.markdown('** Average Volume **: ' + averageVolume)
		st.markdown('** Market Cap **: ' + marketCap)
		st.markdown('** Float Shares **: ' + floatShares)
		st.markdown('** Regular Market Price (USD) **: ' + regularMarketPrice)
		st.markdown('** Bid Size **: ' + bidSize)
		st.markdown('** Ask Size **: ' +askSize)
		st.markdown('** Share Short **: ' + sharesShort)
		st.markdown('** Short Ratio **: ' + shortRatio)
		st.markdown('** Share Outstanding **: ' + sharesOutstanding)


