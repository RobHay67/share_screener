		
from analysis.view.titles import analysis_titles

from analysis.view.multi_analysis import view_multi_criteria			#TODO fleshing out some ideas



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Mult Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def analysis_multi_page(scope):
	analysis_titles(scope, 'Multiple Ticker Analysis', 'multi')

	view_multi_criteria(scope)

	# TODO we migth be able to jumpt to single stock analysis from any list - that migth be cool!!!


	# if ticker in scope.pages['multi']['chart_df'].keys():	
	# for ticker in scope.pages['multi']['ticker_list']:
		# print (ticker)



