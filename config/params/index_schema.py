import pandas as pd


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Index file Schema
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
schema = {
		'share_code'		:{'dtype':'str'				, 'default':None},
		'company_name'		:{'dtype':'str'				, 'default':'zz_missing_company_name'},
		'industry_group'	:{'dtype':'str'				, 'default':'zz_missing_industry_group'},
		'listing_date'		:{'dtype':'datetime64[ns]'	, 'default':pd.to_datetime('2000-01-01')},
		'market_cap'		:{'dtype':'float64'			, 'default':0.0},
		'opening_time'		:{'dtype':'str'				, 'default':None},
		'minutes_per_day'	:{'dtype':'float64'			, 'default':None},
		'blue_chip'			:{'dtype':'str'				, 'default':'zz_not_yet_tagged'},
		'yahoo_status'		:{'dtype':'str'				, 'default':None},
		'missing_dates'		:{'dtype':'object'			, 'default':None},
		'delisted_date'		:{'dtype':'datetime64[ns]'	, 'default':None},
		'trading_halt_dates':{'dtype':'object'			, 'default':None},
	}



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Index file Schema - Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def data_types(schema):
	dtypes={}
	for field, schema in schema.items():
		dtypes[field] = schema['dtype']
	return dtypes

def default_values(schema):
	default_values={}
	for field, schema in schema.items():
		default_values[field] = schema['default']
	return default_values

def csv_dtypes(schema):
	dtypes={}
	for field, schema in schema.items():
		if schema['dtype'] != 'datetime64[ns]': 
			dtypes[field] = schema['dtype']
	return dtypes

def csv_dates(schema):
	dates_to_parse = []
	for field, schema in schema.items():
		if schema['dtype'] == 'datetime64[ns]': 
			dates_to_parse.append(field)
	return dates_to_parse

