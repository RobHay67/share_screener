
import plotly.graph_objects as go




def volume_plot(scope, fig, chart, chart_df, row_no, col_no):

	# Colour the bars on the chart
	# Close Up 		= Green
	# Close Down 	= Red
	# colors = ['green' if row['open'] - row['close'] >= 0 else 'red' for index, row in chart_df.iterrows()]
	colors = ['seagreen' if row['close'] - row['open'] >= 0 else 'sienna' for index, row in chart_df.iterrows()]
	
	fig.add_trace(	go.Bar(
							x=chart_df['date'],
							y=chart_df['volume'],
							marker_color=colors
							), 
					row=row_no, 
					col=col_no
					)


# candlestick colour = seagreen

# nice Blue = cornflowerblue, deepskyblue, darkturquoise
# nice Red = crimson, maroon, sienna, tomato, red
# better Orance = darkorange
# nice grey = gainsboro
# nice green = lightseagreen, mediumseagreen, springgreen

# aliceblue, antiquewhite, aqua, aquamarine, azure,
# beige, bisque, black, blanchedalmond, blue,
# blueviolet, brown, burlywood, cadetblue,
# chartreuse, chocolate, coral, cornflowerblue,
# cornsilk, crimson, cyan, darkblue, darkcyan,
# darkgoldenrod, darkgray, darkgrey, darkgreen,
# darkkhaki, darkmagenta, darkolivegreen, darkorange,
# darkorchid, darkred, darksalmon, darkseagreen,
# darkslateblue, darkslategray, darkslategrey,
# darkturquoise, darkviolet, deeppink, deepskyblue,

# dimgray, dimgrey, dodgerblue, firebrick,
# floralwhite, forestgreen, fuchsia, gainsboro,

# ghostwhite, gold, goldenrod, gray, grey, green,
# greenyellow, honeydew, hotpink, indianred, indigo,
# ivory, khaki, lavender, lavenderblush, lawngreen,
# lemonchiffon, lightblue, lightcoral, lightcyan,
# lightgoldenrodyellow, lightgray, lightgrey,
# lightgreen, lightpink, lightsalmon, lightseagreen,
# lightskyblue, lightslategray, lightslategrey,
# lightsteelblue, lightyellow, lime, limegreen,
# linen, magenta, maroon, mediumaquamarine,
# mediumblue, mediumorchid, mediumpurple,
# mediumseagreen, mediumslateblue, mediumspringgreen,
# mediumturquoise, mediumvioletred, midnightblue,
# mintcream, mistyrose, moccasin, navajowhite, navy,
# oldlace, olive, olivedrab, orange, orangered,
# orchid, palegoldenrod, palegreen, paleturquoise,
# palevioletred, papayawhip, peachpuff, peru, pink,
# plum, powderblue, purple, red, rosybrown,
# royalblue, rebeccapurple, saddlebrown, salmon,
# sandybrown, seagreen, seashell, sienna, silver,
# skyblue, slateblue, slategray, slategrey, snow,
# springgreen, steelblue, tan, teal, thistle, tomato,
# turquoise, violet, wheat, white, whitesmoke,
# yellow, yellowgreen