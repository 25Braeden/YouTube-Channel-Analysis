import pandas as pd
import plotly.express as px

# CHANGE THIS TO YOUR FILE PATH
file_path = 'Global YouTube Statistics.csv'

# If error with this line remove encoding='latin-1'
df = pd.read_csv(file_path, encoding='latin-1')

# Making the plot
fig = px.scatter(df, x='subscribers', y='highest_yearly_earnings',
                 labels={'subscribers': 'Subscriber Count', 'highest_yearly_earnings': 'Highest Yearly Earnings'},
                 title='Relationship between Subscriber Count and Highest Yearly Earnings')

# Hover text
fig.update_traces(textposition='top center',
                  hovertemplate='%{text} <br>Subscribers: %{x} <br>Highest Yearly Earnings: %{y}', text=df['Youtuber'])

# Show dotted lines making it cool
fig.update_xaxes(type='linear', showspikes=True)
fig.update_yaxes(type='linear', showspikes=True)

# Show the plot
fig.show()
