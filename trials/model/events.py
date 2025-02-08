

# Exactly which column adders are recalculated or replaced is
# micro controlled by the following event status


# 		scope.tickers[ticker][page]['re_run_functions']


# The following key events cause the ['re_run_functions'] status 
# to be changed which it results in the columns being replaced
# during the page refresh event

from add_cols.events.edit_active import edit_active_event
from add_cols.events.edit_column_adder import edit_column_adder_event
from add_cols.events.new_ticker import new_ticker_data_event_replace_df_true

from add_cols.events.edit_row_limit import edit_row_limit_event




