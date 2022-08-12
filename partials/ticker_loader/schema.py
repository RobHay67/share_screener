

import streamlit as st



def column_layout_schema(scope):


	# ....x....1....x....2....x....3....x....4....x....5....x....6....x....7....x....8....x....9....x....0....x....1....x....2
	# -------------------------------------------------------------------------------------------------------------------------------------
	# Col1				  col2						        col3			col4				col5				col6
	# -------------------------------------------------------------------------------------------------------------------------------------

	# Multi Screen
	# ....x....1....x....2....x....3....x....4....x....5....x....6....x....7....x....8....x....9....x....0....x....1....x....2
	# | select ticker(s) |  select industry(s)             ||              |  ticker_files     |           Messages          |
	# | Search           |  select a Market                ||              |  trial dfs        |           Messages          |
	# |                  |                                 ||              |  chart dfs        |           Messages          |

	# Single Ticker Screens
	# ....x....1....x....2....x....3....x....4....x....5....x....6....x....7....x....8....x....9....x....0....x....1....x....2
	# | select a ticker  | select a ticker   |              |              |  ticker_files     |           Messages          |
	# |                  | Search            |              |              |  trial dfs        |           Messages          |
	# |                  |                   |              |              |  chart dfs        |           Messages          |



	app = scope.apps['display_app']


	if app != 'screener':
		# Single, Intrad-Day, Volume, Research
		col1,col2,col3,col4,col5,col6 = st.columns([2.0, 3.4, 0.1, 1.5, 2.0, 3.0])
		
	else:
		# == 'Screeener'
		col1,col2,col3,col4,col5,col6 = st.columns([2.0, 3.4, 0.1, 1.5, 2.0, 3.0])
	
	scope.col1 = col1
	scope.col2 = col2
	scope.col3 = col3
	scope.col4 = col4
	scope.col5 = col5
	scope.col6 = col6



