import streamlit as st
from pages.config.three_cols import three_cols


def view_users(scope):

	st.subheader('User Configuration')
	three_cols( 'User Configuration stored in', {}, 'scope.users', widget_type='string' )
	
	st.divider()
	three_cols( 'User Logged in ?', scope.users['logged_in'], "scope.users['logged_in']" )
	three_cols( 'Which User is logged in (name)', scope.users['login_name'], "scope.users['login_name']" )
	
	st.divider()
	three_cols( 'List of Valid Users', scope.users['user_list'], "scope.users['user_list']" )
	
	st.divider()
	three_cols( 'Raw Json File', scope.users['json'], "scope.users['json']" )





