import plotly.express as px
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/gavinrozzi/opra-data/master/opramachine_requests.csv', encoding= 'unicode_escape', parse_dates=['request_created_at','request_updated_at','date_initial_request_last_sent_at','date_response_required_by','date_very_overdue_after','last_public_response_at'])

# Summarize counts of requests by public authority and by user
authority_summary = df.groupby('requested_from').size().sort_values(ascending=True)
user_summary = df.groupby('requested_by').size().sort_values(ascending=True)

# Convert to dataframe
df_users = pd.DataFrame({'user':user_summary.index, 'request_count':user_summary.values})
df_authority = pd.DataFrame({'authority':authority_summary.index, 'request_count':authority_summary.values})

# Save summaries to CSV
df_users.to_csv('user_summary.csv')
df_authority.to_csv('authority_summary.csv')

# Create some plots of the summarized data
fig1 = px.bar(df_authority, x='authority', y= 'request_count',title='OPRA Requests by Authority', color = 'request_count', color_continuous_scale=px.colors.sequential.Viridis)
fig2 = px.bar(df_users, x='user', y= 'request_count',title='OPRA Requests by User', color = 'request_count', color_continuous_scale=px.colors.sequential.Viridis)

fig1.show()
fig2.show()