
import streamlit as st


from charts.candlestick import view_candlestick

def render_selected_charts(scope, ticker):

	for key, value in scope.chart.items():
		print( key.ljust(20), value)


	# any measures (SMA or EMA) should have been added at this stage, we just need to know we need to render them
	analysis_df = scope.selected[scope.display_page]['analysis_df'][ticker]





	# add subplot properties when initializing fig variable
	# fig = make_subplots(rows=4, cols=1, shared_xaxes=True,
    #                 vertical_spacing=0.01, 
    #                 row_heights=[0.5,0.1,0.2,0.2])				# this does the height of each plot - not sure if this is proportional or otherwise

	# so it looks like I need the number of charts (rows)
	# and the height of each chart
	# maybe store this stuff in a dictionary as we go along and then iterate through that at the end???

	# looks like we add a trace for any overlays to the charts - where the hell do we store this info





	if scope.chart['candlestick']:
		print ('render the candlestick')
		view_candlestick(analysis_df)

	if scope.chart['line']:
		print ('render the line')

	if scope.chart['macd']:
		print ('render the macd')

	if scope.chart['stochastic']:
		print ('render the stochastic')

	if scope.chart['ichi_moku']:
		print ('render the ichi_moku')

	if scope.chart['heiken_ashi']:
		print ('render the heiken_ashi')

	if scope.chart['vac']:
		print ('render the vac')

	if scope.chart['vol_osclillator']:
		print ('render the vol_osclillator')

	if scope.chart['bollinger_bands']:
		print ('render the bollinger_bands')

	if scope.chart['dividends']:
		print ('render the dividends')

	if scope.chart['announcements']:
		print ('render the announcements')


	# Format the Axis
	# fig.update_layout(yaxis_tickformat='$',
    #               yaxis2_tickformat='$',
    #               yaxis3_tickformat='$',
    #               yaxis4_tickformat='$',
    #               height=750,
    #               width=1200,
    #               showlegend=False,
    #               title_text=Current_Stock_Profile.shortName)

