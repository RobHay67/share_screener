# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Data file Schema
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
ticker_file_schema =  {
					1 : { 'col_name' : 'date'   , 'index_col' : True  , 'data_type' : 'datetime64[ns]'  },
					2 : { 'col_name' : 'open'   , 'index_col' : False , 'data_type' : 'float64'         },
					3 : { 'col_name' : 'high'   , 'index_col' : False , 'data_type' : 'float64'         },
					4 : { 'col_name' : 'low'    , 'index_col' : False , 'data_type' : 'float64'         },
					5 : { 'col_name' : 'close'  , 'index_col' : False , 'data_type' : 'float64'         },
					6 : { 'col_name' : 'volume' , 'index_col' : False , 'data_type' : 'int64'           }, 
					0 : { 'col_name' : 'ticker' , 'index_col' : False , 'data_type' : None              },   # will not be added to the column dictionary
					# 0 : { 'col_name' : 'unused' , 'index_col' : False , 'data_type' : None              },
					}



ticker_file_usecols 	= ['date', 'open', 'high', 'low', 'close', 'volume']
ticker_file_dtypes 		= {'open': 'float64', 'high': 'float64', 'low': 'float64', 'close': 'float64', 'volume': 'int64'}
ticker_file_dates 		= ['date']




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# We really should be using code to generate the ticker_file lists
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def data_types(schema):
# 	dtypes={}
# 	for field, schema in schema.items():
# 		dtypes[field] = schema['dtype']
# 	return dtypes

# def default_values(schema):
# 	default_values={}
# 	for field, schema in schema.items():
# 		default_values[field] = schema['default']
# 	return default_values

# def csv_dtypes(schema):
# 	dtypes={}
# 	for field, schema in schema.items():
# 		if schema['dtype'] != 'datetime64[ns]': 
# 			dtypes[field] = schema['dtype']
# 	return dtypes

# def csv_dates(schema):
# 	dates_to_parse = []
# 	for field, schema in schema.items():
# 		if schema['dtype'] == 'datetime64[ns]': 
# 			dates_to_parse.append(field)
# 	return dates_to_parse