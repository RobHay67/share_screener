
import streamlit as st



def general(info):
	st.markdown('##### General meta_data Info') 
	st.markdown('** Market **: ' + info['market'])
	st.markdown('** Exchange **: ' + info['exchange'])
	st.markdown('** Quote Type **: ' + info['quoteType'])