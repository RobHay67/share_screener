
def scope_app(scope):
	# System Wide Variables
	scope.share_market = 'ASX'						# Set Initial Default Share Market - we gotta start somewhere
	scope.dropdown_lists_need_updating = False		# Intially set to false, the loading or refreshing of the 
													# share index file has resposibility to set this, but can
													# only do this after loading the share index file
	scope.st_button = None

