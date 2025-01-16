

def determine_tab_names(no_of_verdicts, tab_group_size):

	no_of_tabs = int(no_of_verdicts / tab_group_size)		
	if (no_of_verdicts % tab_group_size) > 0:no_of_tabs+=1
		
	list_of_tab_names = []
	for tab_no in range(no_of_tabs):
		list_of_tab_names.append(str(tab_no+1))
	
	return list_of_tab_names

