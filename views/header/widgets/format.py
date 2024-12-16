
import streamlit as st


def md_for_header(string, bold=False):

	formatted_string = str(string)
	if bold:formatted_string = "<b>"+formatted_string+"</b>"

	align		="text-align: Right;"
	color		="color:grey;"
	font_size	="font-size:.85em;"

	md_string 	= f"""
						<div style=
									"
									{align}
									{color}
									{font_size}
									"
						>
						{formatted_string}
						</div>
						"""
	
	st.markdown(md_string, unsafe_allow_html=True)






			


	# st.markdown("""
	# 			<div style="text-align: Right;color:grey;font-size:.85em;">Ticker Files (loaded)</div>
	# 			"""
	#        		, unsafe_allow_html=True)




# formatted_string = f"""
# # 					<div style="text-align: {align};">{formatted_string}</div>
# # 							"""



# def format_md_string(string, align=None, bold=False, colour='Black' ):

# 	formatted_string = str(string)

# 	if bold:formatted_string = "<b>"+formatted_string+"</b>"
	
# 	if align != None:
# 		formatted_string = f"""
# 							<div style="text-align: Right;">Ticker Files (loaded)</div>
# 							"""
# 				st.markdown("""
# 							<div style="text-align: Right;color:grey;font-size:.85em;">Ticker Files (loaded)</div>
# 						"""
# 	       				, unsafe_allow_html=True)
# 	return formatted_string