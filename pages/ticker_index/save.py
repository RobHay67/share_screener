import streamlit as st
from ticker_index.save import save_index
from ticker_index.schema import editable_columns




def save_ticker_index_button(scope):

	widget_key = 'widget_save_ticker_index'
	
	button = st.button(
						label='Save Changes to Ticker Index', 
						use_container_width=True, 
						type='secondary',
						key=widget_key,
						on_click=save_changes_to_ticker_index,
						args=(scope,)
						)
	
	return button



def save_changes_to_ticker_index(scope):
	# TODO st.data_editor
	# Note this solution is refering to the old_df to get the keys.
	# it should be referring to the new editable df
	# this will probable break if we allow add rows
	
	editable_cols = editable_columns(scope)
	save_required = False

	ticker_index_df = scope.ticker_index['df']

	# determine if we have edited records
	edited_records = st.session_state["widget_ticker_index_df"]["edited_cells"]

	# for key in sorted(st.session_state["widget_ticker_index_df"]):print(key)

	if len(edited_records)>0:
		non_editable_cols = []
		for position, new_value in edited_records.items():
			print('Coordinates  = ', position)
			print('New Value    = ', new_value)

			co_ordinates = position.split(':')
			row_no = int(co_ordinates[0])
			col_no = int(co_ordinates[1])
			print('Row Number   = ', row_no)
			print('Col Number   = ', col_no)

			# Check if we are allowed to edit this column
			if col_no in editable_cols.keys():

				col_name = editable_cols[col_no]
				print('Col Name     = ', col_name)
				
				print('Determine the index for the specified row > ', row_no)
				index_name = ticker_index_df.iloc[[row_no]].index.values.tolist()
				ticker = index_name[0]
				print('Ticker       = ', ticker)

				print('Lets Update the Original df')
				# scope.ticker_index['df'].at[ticker, 'company_name'] = new_value
				ticker_index_df.at[ticker, col_name] = new_value

				save_required = True
			else:
				
				non_editable_cols.append(col_no)
		
		if save_required:save_index(scope)
	
		if len(non_editable_cols) > 0:
			st.toast('Cannot edit these column numbers >'+str(non_editable_cols))

