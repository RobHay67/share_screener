import plotly.graph_objects as go


def dividend_plot(scope, fig, overlay, chart_df, row_no, col_no):

	page 		= scope.page_to_display
	ticker 		= scope.pages[page]['ticker_list'][0]
	font_colour = scope.charts[overlay]['plot']['colour']

	chart_df.set_index('date', inplace=True)
	div_df = chart_df[chart_df[overlay].notnull()]

	for index, row in div_df.iterrows():
		div_date 	= index
		day_high 	= chart_df.at[div_date, 'high']
		dividend 	= '${:,.2f}'.format(row[overlay])
		div_message = 'dividend ' + dividend
		div_date 	= (div_date).strftime('%Y-%m-%d') 

		fig.add_annotation(
							x 			= div_date,
							y 			= day_high,
							opacity		= 0.7,
							text 		= div_message,
							# align 		= 'right',
							xanchor		= 'left',
							xshift		= 10,
							textangle	= 0,
							ax			= 0,
            				ay			= -75,
							# yshift		= 100,					# this is silly
							font 		= { 
											'size':12, 
											'color':font_colour
											},
							name 		= 'Dividends',
							showarrow 	= True,
							arrowcolor	= font_colour,
							arrowsize	= 3,
							arrowwidth	= 1,
							arrowhead	= 1,
							)

	chart_df.reset_index(inplace=True)




