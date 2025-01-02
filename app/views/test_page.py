import streamlit as st

from app.views.header.controller import show_page_header



# Page Configuration
page = 'testing'
page_title = 'test Page - try out new config'
page_icon = '🔬'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page


show_page_header(scope, page_title, page_icon)

# @st.dialog("No Tickers have been selected!")
# st.dialog('this is a dialog ????', width="wide")

# with st.popover('open popover'):
# 	st.write("what the hell")

# Pop Up Model with iterations (and the @st.dialog results in the model only being executied one time)
# @st.dialog("Cast your vote")
# def vote(item):
#     st.write(f"Why is {item} your favorite?")
#     reason = st.text_input("Because...")
#     if st.button("Submit Button"):
#         st.session_state.vote = {"item": item, "reason": reason}
#         st.rerun()

# if "vote" not in st.session_state:
#     st.write("Vote for your favorite")
#     if st.button("A"):
#         vote("A")
#     if st.button("B"):
#         vote("B")
# else:
#     f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
    

# import yfinance as yf

# ticker = "MSFT"
# ticker = "cba.ax"


	# yf_download = yf.download( 
	# 								tickers=scope.yf['batch_ticker_string'], 
	# 								# period='3mo',
	# 								period=scope.pages['download_days'], 
	# 								interval='1d', 
	# 								progress=True, 
	# 								# show_errors=False
	# 								)	

# dat = yf.download(tickers='CBA.AX', period='5d', interval='1d')

# st.header(ticker)
# st.write(dat)
# print(dat)



# dat = yf.Ticker(ticker)
# st.header(ticker)
# st.write(dat)
# st.write(dat.info)
# st.subheader('Dividends')
# st.write(dat.dividends)
# st.write(dat.calendar)
# st.write(dat.analyst_price_targets)
# st.write(dat.quarterly_income_stmt)
# st.subheader('this is dat.history')
# st.write(dat.history(period='1mo'))
# st.write(dat.option_chain(dat.options[0]).calls)


# scope.pages['download_days'] = '5d'
# print(scope.pages['download_days'])