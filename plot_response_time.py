# Script to create plots of OPRA response times from OPRAmachine dataset

import plotly.express as px
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/gavinrozzi/opra-data/master/opramachine_requests.csv', encoding= 'unicode_escape', parse_dates=['request_created_at','request_updated_at','date_initial_request_last_sent_at','date_response_required_by','date_very_overdue_after','last_public_response_at'])

# Create a column of the number of days until a response, calculated from last_public_response_at and date_initial_request_last_sent_at columns
df['days_until_response'] = df['last_public_response_at'] - df['date_initial_request_last_sent_at']
df['days'] = df['days_until_response'].dt.days

# Remove cases where the time difference column is negative
# TODO: Find out why some of the time deltas are coming out negative. Maybe the data needs cleaning?
df = df[df.days.ge(0)]

# Plot the data

# All requests
fig = px.scatter(df, x='request_created_at', y='days',color="described_state",hover_name="title")

# TODO: Get the requests for just 2019

# Subset just the succesful requests and plot them
successful = df[df.described_state.eq('successful')]
fig = px.scatter(successful, x='request_created_at', y='days',color="described_state",hover_name="title")

# Subset just the succesful requests and plot them
rejected = df[df.described_state.eq('rejected')]
fig = px.scatter(rejected, x='request_created_at', y='days',color="described_state",hover_name="title")

# Plot just the requests that took longer than 7 days use date response required by column

fig.show()