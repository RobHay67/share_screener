import streamlit as st


def save_index(scope):
	
	saving_df = scope.ticker_index['df'].copy()
	
	# ensure that the index is saved as a normal column
	saving_df.reset_index(inplace=True)      	 
	
	saving_df.to_csv( scope.files['paths']['ticker_index'], index=False )

	st.toast('Saved the Ticker Index File', icon='💾')
	print ( '\033[92m' + 'Saving the Ticker Index file Now ' + '>'*50 + '\033[0m')	




