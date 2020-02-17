import pandas as pd 

# Read CSV of OPRA request data to Pandas dataframe, parse dates

opra_requests = pd.read_csv('https://raw.githubusercontent.com/gavinrozzi/opra-data/master/opramachine_requests.csv', encoding= 'unicode_escape', parse_dates=['request_created_at','request_updated_at','date_initial_request_last_sent_at','date_response_required_by','date_very_overdue_after','last_public_response_at'])

# Calculate difference in time
opra_requests['days_until_response'] = opra_requests['last_public_response_at'] - opra_requests['date_initial_request_last_sent_at']

