import plotly.express as px
import pandas as pd

# Read in master OPRAmachine dataset
df = pd.read_csv('https://raw.githubusercontent.com/gavinrozzi/opra-data/master/opramachine_requests.csv', encoding= 'unicode_escape', parse_dates=['request_created_at','request_updated_at','date_initial_request_last_sent_at','date_response_required_by','date_very_overdue_after','last_public_response_at'])

# Summarize counts of requests by public authority and by user
authority_summary = df.groupby('requested_from').size().sort_values(ascending=False)
user_summary = df.groupby('requested_by').size().sort_values(ascending=True)

# Save summaries to CSV for later usage
df_users.to_csv('user_summary.csv')
df_authority.to_csv('authority_summary.csv')

# Convert to dataframe
df_users = pd.DataFrame({'user':user_summary.index, 'request_count':user_summary.values})
df_authority = pd.DataFrame({'authority':authority_summary.index, 'request_count':authority_summary.values})

# Get top 100 authorities and plot them
top100 = authority_summary.head(100)
df_top100 = pd.DataFrame({'authority':top100.index, 'request_count':top100.values})
fig3 = px.bar(df_top100, x='authority', y= 'request_count',title='Top 100 Authorities', color = 'request_count', color_continuous_scale=px.colors.sequential.Viridis)

# Create some plots of the summarized data
fig1 = px.bar(df_authority, x='authority', y= 'request_count',title='OPRA Requests by Authority', color = 'request_count', color_continuous_scale=px.colors.sequential.Viridis)
fig2 = px.bar(df_users, x='user', y= 'request_count',title='OPRA Requests by User', color = 'request_count', color_continuous_scale=px.colors.sequential.Viridis)

# Show the plots
fig1.show()
fig2.show()
fig3.show()