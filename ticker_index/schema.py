import pandas as pd


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Index file Schema
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Changes require a reboot

schema = {
		'share_code'		:{'dtype':'str'				, 'default':None,							'allow_edits':False},
		'company_name'		:{'dtype':'str'				, 'default':'zz_missing_company_name',		'allow_edits':True},
		'industry_group'	:{'dtype':'str'				, 'default':'zz_missing_industry_group',	'allow_edits':True},
		'listing_date'		:{'dtype':'datetime64[ns]'	, 'default':pd.to_datetime('2000-01-01'),	'allow_edits':False},
		'market_cap'		:{'dtype':'float64'			, 'default':0.0,							'allow_edits':False},
		'opening_time'		:{'dtype':'str'				, 'default':None,							'allow_edits':False},
		'minutes_per_day'	:{'dtype':'float64'			, 'default':None,							'allow_edits':False},
		'blue_chip'			:{'dtype':'str'				, 'default':'zz_not_yet_tagged',			'allow_edits':True},
		'yahoo_status'		:{'dtype':'str'				, 'default':None,							'allow_edits':False},
		'missing_dates'		:{'dtype':'object'			, 'default':None,							'allow_edits':False},
		'delisted_date'		:{'dtype':'datetime64[ns]'	, 'default':None,							'allow_edits':False},
		'trading_halt_dates':{'dtype':'object'			, 'default':None,							'allow_edits':False},
	}



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Index file Schema - Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


def editable_columns(scope):
	schema = scope.ticker_index['schema']
	editable_cols={}
	for i, key in enumerate(schema):
		if schema[key]['allow_edits'] == True:
			editable_cols[i]=key
	return editable_cols

def data_types(scope):
	schema = scope.ticker_index['schema']
	dtypes={}
	for field, schema in schema.items():
		dtypes[field] = schema['dtype']
	return dtypes

def default_values(scope):
	schema = scope.ticker_index['schema']
	default_values={}
	for field, schema in schema.items():
		default_values[field] = schema['default']
	return default_values

def csv_dtypes(scope):
	schema = scope.ticker_index['schema']
	dtypes={}
	for field, schema in schema.items():
		if schema['dtype'] != 'datetime64[ns]': 
			dtypes[field] = schema['dtype']
	return dtypes

def csv_dates(scope):
	schema = scope.ticker_index['schema']
	dates_to_parse = []
	for field, schema in schema.items():
		if schema['dtype'] == 'datetime64[ns]': 
			dates_to_parse.append(field)
	return dates_to_parse

