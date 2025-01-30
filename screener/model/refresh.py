


# Column Adders are checked during the page refresh event




# Refresh Columns Adders (process call stack)

# 1 Page Refresh calls
from app.views.header.controller import show_page_header
# 2 Show Ticker Loader and Col Adder Progress Bars
from app.views.header.d_ticker_files.controller import show_ticker_load_and_col_adding
# 3 Check if Columns Need to be replaced (by ticker)
from app.views.header.d_ticker_files.progress_bar_add_cols import progress_bar_for_adding_extra_columns
# 4 Call the add_column function for this dataframe (deletes old columns) 
from add_cols.model.replace_df_cols import replace_page_df_columns

