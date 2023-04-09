import streamlit as st

from pages.config.two_cols import view_2_columns

def company_general(metadata):
	# st.subheader(metadata.info['longName'])

	info_keys = metadata.info.keys()
	
	col1,col2,col3,col4 = st.columns([1,1,2,4])

	with col1:
		if 'logo_url' in info_keys:
			st.image(metadata.info['logo_url'])

	with col2:
		st.caption('Sector')
		st.caption('Industry')
		st.caption('Phone')
		st.caption('Address')
		st.caption('Website')

	with col3:
		if 'sector' in info_keys:
			st.write(metadata.info['sector'])
		if 'industry' in info_keys:
			st.write(metadata.info['industry'])
		if 'phone' in info_keys:
			st.write(metadata.info['phone'])
		if 'website' in info_keys:
			st.write(metadata.info['website'])
		if 'address1' in info_keys:
			st.write(metadata.info['address1'] 
			+ ', ' + metadata.info['address2'] 
			+ ', ' + metadata.info['city'] 
			+ ', ' + metadata.info['zip'] 
			+ ', ' + metadata.info['country'])

	with col4:
		if 'longBusinessSummary' in info_keys:
			sentences = metadata.info['longBusinessSummary'].split('. ')
			my_expander = st.expander(label='Business Summary', expanded=False)
			for sentence in sentences:
				with my_expander: st.write(sentence)



		# st.markdown('** Sector **: ' + metadata.info['sector'])
		# st.markdown('** Industry **: ' + metadata.info['industry'])
		# st.markdown('** Phone **: ' + metadata.info['phone'])
		# st.markdown('** Address **: ' 
		# 			+        metadata.info['address1'] 
		# 			+ ', ' + metadata.info['city'] 
		# 			+ ', ' + metadata.info['zip'] 
		# 			+ ', ' + metadata.info['country']
		# 			)
		# st.markdown('** Website **: ' + metadata.info['website'])

		

# def business_summary(metadata):
# 	sentences = metadata.info['longBusinessSummary'].split('. ')
# 	my_expander = st.expander(label='Business Summary', expanded=False)
# 	for sentence in sentences:
# 		with my_expander: st.write(sentence)





def fundamental(metadata):
	# col1,col2 = st.columns([5,7])
	my_expander = st.expander(label='Fundamental Information', expanded=False)
	with my_expander:
		# view_2_columns( 'Enterprise Value (AUD)', metadata.info['enterpriseValue'])
		# view_2_columns( 'Enterprise To Revenue Ratio', metadata.info['enterpriseToRevenue'])
		# view_2_columns( 'Enterprise To Ebitda Ratio', metadata.info['enterpriseToEbitda'])
		# view_2_columns( 'Net Income (AUD)', metadata.info['netIncomeToCommon'])
		# view_2_columns( 'Profit Margin Ratio', metadata.info['profitMargins'])
		view_2_columns( 'Forward PE Ratio', metadata.info['forwardPE'])
		# view_2_columns( 'PEG Ratio', metadata.info['pegRatio'])
		view_2_columns( 'Price to Book Ratio', metadata.info['priceToBook'])
		# view_2_columns( 'Forward EPS (AUD)', metadata.info['forwardEps'])
		# view_2_columns( 'Beta', metadata.info['beta'])
		view_2_columns( 'Book Value (AUD)', metadata.info['bookValue'])
		# view_2_columns( 'Dividend Rate (%)', metadata.info['dividendRate'])
		# view_2_columns( 'Dividend Yield (%)', metadata.info['dividendYield'])
		# view_2_columns( 'Five year Avg Dividend Yield (%)', metadata.info['fiveYearAvgDividendYield'])
		# view_2_columns( 'Payout Ratio', metadata.info['payoutRatio'])


def general(metadata):
	# st.markdown('##### General meta_data Info') 
	my_expander = st.expander(label='General Information', expanded=False)
	with my_expander:
		st.markdown('** Market **: ' + metadata.info['market'])
		st.markdown('** Exchange **: ' + metadata.info['exchange'])
		st.markdown('** Quote Type **: ' + metadata.info['quoteType'])



def market_info(metadata):
	my_expander = st.expander(label='Market Information', expanded=False)
	info_keys = metadata.info.keys()
	
	volume = str(metadata.info['volume']) if 'volume' in info_keys else '0'
	averageVolume = str(metadata.info['averageVolume']) if 'averageVolume' in info_keys else '0'
	marketCap = str(metadata.info['marketCap']) if 'marketCap' in info_keys else '0'
	floatShares = str(metadata.info['floatShares']) if 'floatShares' in info_keys else '0'
	regularMarketPrice = str(metadata.info['regularMarketPrice']) if 'regularMarketPrice' in info_keys else '0'
	bidSize = str(metadata.info['bidSize']) if 'bidSize' in info_keys else '0'
	askSize = str(metadata.info['askSize']) if 'askSize' in info_keys else '0'
	sharesShort = str(metadata.info['sharesShort']) if 'sharesShort' in info_keys else '0'
	shortRatio = str(metadata.info['shortRatio']) if 'shortRatio' in info_keys else '0'
	sharesOutstanding = str(metadata.info['sharesOutstanding']) if 'sharesOutstanding' in info_keys else '0'


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






# ----------------------------------------------------------------------------------------------------------------------------------------
# metadata = yf.Ticker('CBA.AX')
# metadata.info
#
# renders the following variables - comment out those being used above Rob
#
# ----------------------------------------------------------------------------------------------------------------------------------------

{
#  'zip': '2000',
#  'sector': 'Financial Services',
 'fullTimeEmployees': 44375,
#  'longBusinessSummary': 'Commonwealth Bank of Australia provides integrated financial services in Australia, New Zealand, and internationally. It operates through Retail Banking Services, Business Banking, Institutional Banking and Markets, and New Zealand segments. The company offers retail, premium, business, offshore, and institutional banking services; and funds management, superannuation, and share broking products and services, as well as car, health, life, income protection, and travel insurance. It offers transaction, savings, foreign currency accounts; term deposits; personal and business loans; overdrafts; equipment finance; credit cards; international payment and trade; and private banking services, as well as home and car loans, and importer finance products. The company also provides advisory services for high net worth individuals; equities trading and margin lending services; debt capital, transaction banking, working capital, and risk management services; and international and foreign exchange services. As of June 30, 2021, it operated 875 branches and 2,492 ATMs. The company was founded in 1911 and is based in Sydney, Australia.',
#  'city': 'Sydney',
#  'phone': '61 2 9378 2000',
 'state': 'NSW',
#  'country': 'Australia',
 'companyOfficers': [],
#  'website': 'http://www.commbank.com.au',
 'maxAge': 1,
#  'address1': 'Tower 1',
 'fax': '61 2 9118 7192',
#  'industry': 'Banks—Diversified',
 'address2': 'Ground Floor 201 Sussex Street',
 'ebitdaMargins': 0,
#  'profitMargins': 0.42470002,
 'grossMargins': 0,
 'operatingCashflow': -19876999168,
 'revenueGrowth': 0.274,
 'operatingMargins': 0.54885,
 'ebitda': None,
 'targetLowPrice': 73,
 'recommendationKey': 'hold',
 'grossProfits': 23972000000,
 'freeCashflow': None,
 'targetMedianPrice': 93.5,
 'currentPrice': 94.81,
 'earningsGrowth': 0.491,
 'currentRatio': None,
 'returnOnAssets': 0.00839,
 'numberOfAnalystOpinions': 14,
 'targetMeanPrice': 93.9,
 'debtToEquity': None,
 'returnOnEquity': 0.11739001,
 'targetHighPrice': 112,
 'totalCash': 158097997824,
 'totalDebt': 249914998784,
 'totalRevenue': 23971999744,
 'totalCashPerShare': 89.198,
 'financialCurrency': 'AUD',
 'revenuePerShare': 13.536,
 'quickRatio': None,
 'recommendationMean': 3.4,
#  'exchange': 'ASX',
 'shortName': 'CWLTH BANK FPO',
 'longName': 'Commonwealth Bank of Australia',
 'exchangeTimezoneName': 'Australia/Sydney',
 'exchangeTimezoneShortName': 'AEDT',
 'isEsgPopulated': False,
 'gmtOffSetMilliseconds': '39600000',
#  'quoteType': 'EQUITY',
 'symbol': 'CBA.AX',
 'messageBoardId': 'finmb_874262',
#  'market': 'au_market',
 'annualHoldingsTurnover': None,
#  'enterpriseToRevenue': 10.84,
 'beta3Year': None,
#  'enterpriseToEbitda': None,
 '52WeekChange': 0.19906414,
 'morningStarRiskRating': None,
#  'forwardEps': 5.2,
 'revenueQuarterlyGrowth': None,
#  'sharesOutstanding': 1706390016,
 'fundInceptionDate': None,
 'annualReportExpenseRatio': None,
 'totalAssets': None,
#  'bookValue': 44.41,
#  'sharesShort': None,
 'sharesPercentSharesOut': None,
 'fundFamily': None,
 'lastFiscalYearEnd': 1625011200,
 'heldPercentInstitutions': 0.19841999,
#  'netIncomeToCommon': 8842999808,
 'trailingEps': 5.399,
 'lastDividendValue': 2,
 'SandP52WeekChange': 0.26866078,
#  'priceToBook': 2.1348796,
 'heldPercentInsiders': 0.0041,
 'nextFiscalYearEnd': 1688083200,
 'yield': None,
 'mostRecentQuarter': 1625011200,
#  'shortRatio': None,
 'sharesShortPreviousMonthDate': None,
#  'floatShares': 1767823060,
#  'beta': 0.644632,
#  'enterpriseValue': 259866214400,
 'priceHint': 2,
 'threeYearAverageReturn': None,
 'lastSplitDate': 939168000,
 'lastSplitFactor': '1:1',
 'legalType': None,
 'lastDividendDate': 1629158400,
 'morningStarOverallRating': None,
 'earningsQuarterlyGrowth': 0.546,
 'priceToSalesTrailing12Months': 6.7488256,
 'dateShortInterest': None,
#  'pegRatio': 4.17,
 'ytdReturn': None,
#  'forwardPE': 18.232693,
 'lastCapGain': None,
 'shortPercentOfFloat': None,
 'sharesShortPriorMonth': None,
 'impliedSharesOutstanding': None,
 'category': None,
 'fiveYearAverageReturn': None,
 'previousClose': 95.77,
 'regularMarketOpen': 95.8,
 'twoHundredDayAverage': 97.4035,
 'trailingAnnualDividendYield': 0.03654589,
#  'payoutRatio': 0.527,
 'volume24Hr': None,
 'regularMarketDayHigh': 96.36,
 'navPrice': None,
 'averageDailyVolume10Day': 3427248,
 'regularMarketPreviousClose': 95.77,
 'fiftyDayAverage': 103.5892,
 'trailingAnnualDividendRate': 3.5,
 'open': 95.8,
 'toCurrency': None,
 'averageVolume10days': 3427248,
 'expireDate': None,
 'algorithm': None,
#  'dividendRate': 4,
 'exDividendDate': 1629158400,
 'circulatingSupply': None,
 'startDate': None,
 'regularMarketDayLow': 94.22,
 'currency': 'AUD',
 'trailingPE': 17.560658,
 'regularMarketVolume': 3031113,
 'lastMarket': None,
 'maxSupply': None,
 'openInterest': None,
#  'marketCap': 161782841344,
 'volumeAllCurrencies': None,
 'strikePrice': None,
 'averageVolume': 2934442,
 'dayLow': 94.22,
 'ask': 94.85,
#  'askSize': 7100,
#  'volume': 3031113,
 'fiftyTwoWeekHigh': 110.19,
 'fromCurrency': None,
#  'fiveYearAvgDividendYield': 5.09,
 'fiftyTwoWeekLow': 78.79,
 'bid': 94.81,
 'tradeable': False,
#  'dividendYield': 0.0422,
#  'bidSize': 36400,
 'dayHigh': 96.36,
#  'regularMarketPrice': 94.81,
 'preMarketPrice': None,
 'logo_url': 'https://logo.clearbit.com/commbank.com.au'}





# Latest CBA Call
{
	'zip': '2000', 
	'sector': 'Financial Services',
	 'fullTimeEmployees': 47532, 
	 'longBusinessSummary': 'Commonwealth Bank of Australia provides integrated financial services in Australia, New Zealand, and internationally. It operates through Retail Banking Services, Business Banking, Institutional Banking and Markets, and New Zealand segments. The company offers retail, premium, business, offshore, and institutional banking services; and funds management, superannuation, and share broking products and services, as well as car, health, life, income protection, and travel insurance. It offers transaction, savings, foreign currency accounts; term deposits; personal and business loans; overdrafts; equipment finance; credit cards; international payment and trade; and private banking services, as well as home and car loans, and importer finance products. The company also provides advisory services for high net worth individuals; equities trading and margin lending services; debt capital, transaction banking, working capital, and risk management services; and international and foreign exchange services. As of June 30, 2021, it operated 875 branches and 2,492 ATMs. The company was founded in 1911 and is based in Sydney, Australia.', 
	 'city': 'Sydney',
	  'phone': '61 2 9378 2000',
	   'state': 'NSW',
	    'country': 'Australia', 
		'companyOfficers': [],
		 'website': 'https://www.commbank.com.au',
		  'maxAge': 1,
		   'address1': 'Tower 1', 
		  'fax': '61 2 9118 7192', 
		  'industry': 'Banks—Diversified', 
		  'address2': 'Ground Floor 201 Sussex Street', 
		  'ebitdaMargins': 0,
		   'profitMargins': 0.44432998, 
		   'grossMargins': 0,
		    'operatingCashflow': -18645000192,
			 'revenueGrowth': 0.107, 
			 'operatingMargins': 0.56715, 
			 'ebitda': None, 
			 'targetLowPrice': 77, 
			 'recommendationKey': 'underperform',
			  'grossProfits': 23972000000, 
			  'freeCashflow': None, 'targetMedianPrice': 91, 'currentPrice': 89.67, 'earningsGrowth': 0.226, 'currentRatio': None, 'returnOnAssets': 0.0089, 'numberOfAnalystOpinions': 15, 'targetMeanPrice': 95.09, 'debtToEquity': None, 'returnOnEquity': 0.13129, 'targetHighPrice': 114, 'totalCash': 147941998592, 'totalDebt': 262988005376, 'totalRevenue': 25166000128, 'totalCashPerShare': 86.776, 'financialCurrency': 'AUD', 'revenuePerShare': 14.331, 'quickRatio': None, 'recommendationMean': 3.6, 'exchange': 'ASX', 'shortName': 'CWLTH BANK FPO', 'longName': 'Commonwealth Bank of Australia', 'exchangeTimezoneName': 'Australia/Sydney', 'exchangeTimezoneShortName': 'AEST', 'isEsgPopulated': False, 'gmtOffSetMilliseconds': '36000000', 'quoteType': 'EQUITY', 'symbol': 'CBA.AX', 'messageBoardId': 'finmb_874262', 'market': 'au_market', 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 10.483, 'beta3Year': None, 'enterpriseToEbitda': None, '52WeekChange': -0.12650901, 'morningStarRiskRating': None, 'forwardEps': 5.48, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 1704880000, 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'totalAssets': None, 'bookValue': 43.791, 'sharesShort': None, 'sharesPercentSharesOut': None, 'fundFamily': None, 'lastFiscalYearEnd': 1625011200, 'heldPercentInstitutions': 0.21244, 'netIncomeToCommon': 9825000448, 'trailingEps': 6.046, 'lastDividendValue': 1.75, 'SandP52WeekChange': -0.1346069, 'priceToBook': 2.0476809, 'heldPercentInsiders': 0.00411, 'nextFiscalYearEnd': 1688083200, 'yield': None, 'mostRecentQuarter': 1640908800, 'shortRatio': None, 'sharesShortPreviousMonthDate': None, 'floatShares': 1699868932, 'beta': 0.744834, 'enterpriseValue': 263818936320, 'priceHint': 2, 'threeYearAverageReturn': None, 'lastSplitDate': 939168000, 'lastSplitFactor': '1:1', 'legalType': None, 'lastDividendDate': 1644883200, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': 0.206, 'priceToSalesTrailing12Months': 6.074727, 'dateShortInterest': None, 'pegRatio': 1.57, 'ytdReturn': None, 'forwardPE': 16.363138, 'lastCapGain': None, 'shortPercentOfFloat': None, 'sharesShortPriorMonth': None, 'impliedSharesOutstanding': 0, 'category': None, 'fiveYearAverageReturn': None, 'previousClose': 87.55, 'regularMarketOpen': 88.38, 'twoHundredDayAverage': 101.31155, 'trailingAnnualDividendYield': 0.042832665, 'payoutRatio': 0.65790004, 'volume24Hr': None, 'regularMarketDayHigh': 89.69, 'navPrice': None, 'averageDailyVolume10Day': 5336101, 'regularMarketPreviousClose': 87.55, 'fiftyDayAverage': 102.3408, 'trailingAnnualDividendRate': 3.75, 'open': 88.38, 'toCurrency': None, 'averageVolume10days': 5336101, 'expireDate': None, 'algorithm': None, 'dividendRate': 3.5, 'exDividendDate': 1644969600, 'circulatingSupply': None, 'startDate': None, 'regularMarketDayLow': 87.98, 'currency': 'AUD', 'trailingPE': 14.831293, 'regularMarketVolume': 2447641, 'lastMarket': None, 'maxSupply': None, 'openInterest': None, 'marketCap': 152876580864, 'volumeAllCurrencies': None, 'strikePrice': None, 'averageVolume': 2453089, 'dayLow': 87.98, 'ask': 89.67, 'askSize': 7100, 'volume': 2447641, 'fiftyTwoWeekHigh': 110.19, 'fromCurrency': None, 'fiveYearAvgDividendYield': 4.92, 'fiftyTwoWeekLow': 86.98, 'bid': 89.6, 'tradeable': False, 'dividendYield': 0.04, 'bidSize': 36400, 'dayHigh': 89.69, 'regularMarketPrice': 89.67, 'preMarketPrice': None, 'logo_url': 'https://logo.clearbit.com/commbank.com.au'}