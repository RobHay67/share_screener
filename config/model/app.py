import time  





def scope_app(scope):
	# Application Fixex Variables
	scope.project_description = 'DDT - Data Driven Trading'
	scope.project_start_time = time.time()


	# System Wide Variables
	scope.share_market = 'ASX'						# Set Initial Default Share Market - we gotta start somewhere
	scope.dropdown_lists_need_updating = False		# Intially set to false, the loading or refreshing of the 
													# share index file has resposibility to modify this, but can
													# only do this after loading the share index file
	
	scope.st_button = None






