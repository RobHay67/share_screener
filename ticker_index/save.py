
from partials.messages.ticker_index import message_save




def save_index( scope ): # DONE
	# st.subheader('Save Ticker Index File')
	
	saving_df = scope.ticker_index.copy()
	
	saving_df.reset_index(inplace=True)      	 # ensure that the index is saved as a normal column
	
	saving_df.to_csv( scope.files['paths']['ticker_index'], index=False )
	
	print ( '\033[92mSaved Ticker Index \033[0m')

	message_save()



