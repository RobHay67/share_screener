import streamlit as st
from pages.config.three_cols import three_cols


def view_users(scope):

	st.subheader('User Configuration')
	three_cols( 'User Configuration stored in', {}, 'scope.users', widget_type='string' )

	st.subheader('User Configuration')
	three_cols( 'User Logged in ?', scope.user_logged_in, "scope.user_logged_in" )
	three_cols( 'Logged in Name', scope.users['login_name'], "scope.users['login_name']" )
	three_cols( 'List of Valid Users', scope.users['user_list'], "scope.users['user_list']" )
	three_cols( 'Raw Json File', scope.users['json'], "scope.users['json']" )





