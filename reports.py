import time
import datetime
import re 								# for the strip colours functions
import streamlit as st
import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# -----------------------------------------------------------------------------------------------------------------------------------
# Colours
# -----------------------------------------------------------------------------------------------------------------------------------
red         = '\033[91m'
green       = '\033[92m'
yellow      = '\033[93m'
blue        = '\033[94m'
purple      = '\033[95m'
cyan        = '\033[96m'
white 		= '\033[0m'


# -----------------------------------------------------------------------------------------------------------------------------------
# Share Index Reports
# -----------------------------------------------------------------------------------------------------------------------------------

def print_share_index_industries(params):
	terminal_heading( params, 'Share Index File contains the following Industries', line_filler='-', colour=cyan )
	print ( cyan, end='' )
	print ( params.share_index_file['industry_group'].value_counts() )
	print ( cyan + '-'*params.terminal_width + white)
	terminal_blank_line(5)

def print_missing_dates(params):
	terminal_heading( params, 'Missing Dates for each ticker just assessed', line_filler='-', colour=yellow )
	print ( yellow, end='' )
	for ticker in params.share_data['files']:
		missing_dates_string = str(params.share_index['file'].at[ticker, 'missing_dates'])
		if missing_dates_string != 'None':
			qty = str(missing_dates_string.count(' ')+1)
			leader = ticker + white + ' (' + qty + ') ' + yellow
			if len(missing_dates_string) <= params.terminal['width'] - 20:
				print ( leader + missing_dates_string )
			else:
				for chunk in chunkstring(missing_dates_string, (11*16)):
					print ( leader + chunk )
	print ( yellow + '-'*params.terminal['width'] + white)

def chunkstring(string, length):
	return (string[0+i:length+i] for i in range(0, len(string), length))

# -----------------------------------------------------------------------------------------------------------------------------------
# Params Report - Helpers
# -----------------------------------------------------------------------------------------------------------------------------------

def terminal_blank_line( number_of_new_lines ):
	for i in range(0,number_of_new_lines): print ('')

def terminal_heading( params, message, colour=white, line_filler='-' ):
	print ( colour + (line_filler*params.terminal_width) + white)
	print ( colour + message + white )       
	print ( colour + (line_filler*params.terminal_width) + white)

def report_progress(params, message, message2=None, colour=white, colour2=yellow, line_filler=None, leading_spaces=None, wait=None, prefix=True):
	if params.terminal_audit:
		line_prefix = 'report - ' if prefix == True else ''

		message = line_prefix + str(message)

		if message2 != None: message2=str(message2)

		if leading_spaces != None: terminal_blank_line(2)      # add this many returns before printing
		
		if message2 != None:
			message = message.ljust(tab1)           # we have a second message so add a space between them
		else: 
			message2 = ''

		if line_filler != None:
			spare_spaces = params.terminal['width'] - len( str(message) ) - len( str(message2) ) - 1
			line_filler = line_filler * spare_spaces
		else:
			line_filler = ''

		complete_message = colour + message + colour2 + message2 + white + line_filler

		if wait != None:
			# print ( red +'adding wait'+white, end=' ')
			print ( complete_message, end=' ' + white )  # the user wants us to wait a bit
		else:
			print ( complete_message          + white )


# -----------------------------------------------------------------------------------------------------------------------------------
# Project Heading & Footer
# -----------------------------------------------------------------------------------------------------------------------------------
def print_project_completion(params):
	current_time    = time.time()
	start_time      = params.project['start_time']
	
	time_difference_seconds = round( ( ( current_time - start_time )      ), 2 ) 
	time_difference_minutes = round( ( ( current_time - start_time ) / 60 ), 2 ) 

	for i in range(0,5): print ('')
	
	print ( cyan + ('='*params.terminal['width']) + white)
	terminal_heading( params, ('Processing complete - ' + params.project['description']), line_filler='=', colour=cyan )
	print ( cyan + ('='*params.terminal['width']) + white)
	for i in range(0,2): print ('')

	# print( purple + params.project_description + green + ' processing complete' + white )
	print( cyan + ' - completed runtime          @ ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + white)
	print( cyan + ' - total load time in seconds = ', str( time_difference_seconds ) + white)
	print( cyan + ' - total load time in minutes = ', str( time_difference_minutes ) + white)
	for i in range(0,2): print ('')
	print ( cyan + '='*params.terminal['width'] + white )



# -----------------------------------------------------------------------------------------------------------------------------------
# Output Ticker Iteration to terminal
# -----------------------------------------------------------------------------------------------------------------------------------
def output_results_to_browser(scope, output=None, result=None, final_print=False, passed='', passed_2='', failed='' ):
	# I think what we do here is just build 3 list and save them

	if output == None:
		# this is the initial run so set all the defails
		# width_of_next_output = 0
		scope.result_passed=passed
		scope.result_passed_2=passed_2
		scope.result_failed=failed
		scope.result_passed_count = 0
		scope.result_passed_2_count = 0
		scope.result_failed_count = 0

	# Store the results
	if result=='passed':
		scope.result_passed = scope.result_passed + str(output) + ' '
		scope.result_passed_count +=1
	elif result=='passed_2':
		scope.result_passed_2 = scope.result_passed_2 + str(output) + ' '
		scope.result_passed_2_count +=1
	elif result=='failed':
		scope.result_failed = scope.result_failed + str(output) + ' '
		scope.result_failed_count +=1

	# print (scope.result_passed)
	if final_print: 
		scope.result_passed = scope.result_passed + ' < ( ' + str(scope.result_passed_count) + ' )'
		scope.result_passed_2 = scope.result_passed_2 + ' < ( ' + str(scope.result_passed_2_count) + ' )'
		scope.result_failed = scope.result_failed + ' < ( ' + str(scope.result_failed_count) + ' )'

		if scope.result_passed_count > 0: st.info(scope.result_passed)
		if scope.result_passed_2_count > 0: st.warning(scope.result_passed_2)

		# if len(scope.result_failed) != 0:
		if scope.result_failed_count > 0: st.error(scope.result_failed)



def output_result_to_terminal(params, output=None, result=None, final_print=False):
	# On the initial run, provide the output_width of the variable, 
	# then just call the function when you want it incremented, 
	# and finally provide the final output sting to finsih off the function

	if output != None:
		width_of_next_output = len(strip_colours(output)) + 1
		params.terminal_print_width += width_of_next_output
	else:
		# this is the initial run so set all the defails
		width_of_next_output = 0
		params.terminal_print_width=0
		params.terminal_count_passed=0
		params.terminal_count_passed_2=0
		params.terminal_count_failed=0
	
	# Print the results
	if result=='passed':
		print( cyan + output + white, end=' ' )
		# st.info(output)
		params.terminal_count_passed +=1
	elif result=='passed_2':
		print( yellow + output + white, end=' ' )
		# st.st.warning(output)
		params.terminal_count_passed_2 +=1
	elif result=='failed':
		print( purple + output + white, end=' ' )
		# st.error(output)
		params.terminal_count_failed +=1
	
	# check if we expect to exceeded the terminal output on the next print and do a carriage return so this does not happen
	if (params.terminal_print_width) > params.terminal_width-5 : 
		print ('')
		params.terminal_print_width=0
	
	if final_print: print ( output )


def strip_colours( variable ):
	ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
	stripped_variable = ansi_escape.sub('', variable)
	return stripped_variable

