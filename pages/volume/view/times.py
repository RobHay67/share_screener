
import streamlit as st



def view_local_vs_market_time(local_time, market_time): # DONE
	col1,col2,col3 = st.columns([1,1,1])
	with col1:st.write('Local Time')
	with col2:st.write(str(local_time.strftime('%H:%M:%S %p')))
	with col3:st.write(str(local_time.strftime('%Y-%m-%d')))

	with col1:st.write('Market Time')
	with col2:st.subheader(str(market_time.strftime('%H:%M:%S %p')))
	with col3:st.write(str(market_time.strftime('%Y-%m-%d')))

	st.markdown("""---""")



