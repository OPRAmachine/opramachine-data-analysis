import pandas as pd 

# Read CSV of OPRA request data to Pandas dataframe
opra_requests = pd.read_csv("opramachine_requests.csv")

# Convert date time columns to proper type
opra_requests['request_created_at'] = opra_requests['request_created_at'].astype('datetime64[ns]') 
opra_requests['request_updated_at'] = opra_requests['request_updated_at'].astype('datetime64[ns]') 
opra_requests['date_initial_request_last_sent_at'] = opra_requests['date_initial_request_last_sent_at'].astype('datetime64[ns]') 
opra_requests['date_response_required_by'] = opra_requests['date_response_required_by'].astype('datetime64[ns]') 
opra_requests['date_very_overdue_after'] = opra_requests['date_very_overdue_after'].astype('datetime64[ns]') 
opra_requests['last_public_response_at'] = opra_requests['last_public_response_at'].astype('datetime64[ns]') 

# Calculate difference in time
opra_requests['days_until_response'] = opra_requests['last_public_response_at'] - opra_requests['date_initial_request_last_sent_at']