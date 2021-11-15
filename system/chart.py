import streamlit as st

from system.reports import view_3_columns




# Chart Variables
def scope_chart(scope):
	scope.chart_lines = []
	scope.chart_macd_on_price = {}
	scope.chart_macd_on_volume = {}


def view_chart(scope):
	st.subheader('Charting Parameters')
	view_3_columns( 'Chart Line', scope.chart_lines, 'chart_lines' )
	view_3_columns( 'Chart MACD on Price', scope.chart_macd_on_price, 'chart_macd_on_price' )
	view_3_columns( 'Chart MACD on Volume', scope.chart_macd_on_volume, 'chart_macd_on_volume' )