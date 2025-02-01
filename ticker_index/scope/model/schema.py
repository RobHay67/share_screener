import logging
import pandas as pd

# Changes require a reboot

def scope_ticker_index_schema(scope):
	logging.debug("scope_ticker_index_schema")
	scope.ticker_index['schema'] = schema


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
