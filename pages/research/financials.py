
import streamlit as st
import pandas as pd


# pixel_width = 70 * no_columns
# pixel_row_height = 40



def financial_statements(metadata):

	col1,col2,col3 = st.columns([4,1,4])

	# if 'financials' in metadata.keys:
	profit_loss = pd.DataFrame(metadata.financials)
	# if 'quarterly_financials' in metadata.keys():
	profit_loss_qtr = pd.DataFrame(metadata.quarterly_financials)


	with col1:
		my_expander = st.expander(label='Financials - Annual')
		my_expander.dataframe(profit_loss, len(profit_loss.columns) * 100, len(profit_loss)*40)

	with col3:
		my_expander = st.expander(label='Financials - Quarterly')
		my_expander.dataframe(profit_loss_qtr, 2000, 2000)








def annual(metadata):
	ticker_info = pd.DataFrame(metadata.financials)
	my_expander = st.expander(label='Financials - Annual')
	my_expander.dataframe(ticker_info, 2000, 2000)



def quarterly(metadata):
	ticker_info = pd.DataFrame(metadata.quarterly_financials)
	my_expander = st.expander(label='Financials - Quarterly')
	my_expander.dataframe(ticker_info, 2000, 2000)


def balance_sheet(metadata):
	ticker_info = pd.DataFrame(metadata.balance_sheet)
	my_expander = st.expander(label='Balance Sheet - Annual')
	my_expander.dataframe(ticker_info, 2000, 2000)

def balance_sheet_qtr(metadata):
	ticker_info = pd.DataFrame(metadata.quarterly_balance_sheet)
	my_expander = st.expander(label='Balance Sheet - Quarterly')
	my_expander.dataframe(ticker_info, 2000, 2000)



def cashflow(metadata):
	ticker_info = pd.DataFrame(metadata.cashflow)
	my_expander = st.expander(label='Cash Flow - Annual')
	my_expander.dataframe(ticker_info, 2000, 2000)


def cashflow_qtr(metadata):
	ticker_info = pd.DataFrame(metadata.quarterly_cashflow)
	my_expander = st.expander(label='Cash Flow - Quarterly')
	my_expander.dataframe(ticker_info, 2000, 2000)


def earnings(metadata):
	ticker_info = pd.DataFrame(metadata.earnings)
	my_expander = st.expander(label='Earnings - Annual')
	my_expander.dataframe(ticker_info, 2000, 2000)


def earnings_qtr(metadata):
	ticker_info = pd.DataFrame(metadata.quarterly_earnings)
	my_expander = st.expander(label='Earnings - Quarterly')
	my_expander.dataframe(ticker_info, 2000, 2000)



