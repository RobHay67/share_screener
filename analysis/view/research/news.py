
import streamlit as st
import pandas as pd
from datetime import datetime

# Unfortunately YFinance is no good for news - we need to find another source TODO






def news(metadata):
	st.markdown('** news from YFinance is NOT Reliable - will try scraping from ASX - BeautifulSoup **')


	# news = pd.DataFrame(metadata.news)
	# if not news.empty:
	# 	my_expander = st.expander(label='News', expanded=False)
	# 	my_expander.dataframe(news, 2000, 2000)
	# else:
	# 	st.markdown('** No News **')



