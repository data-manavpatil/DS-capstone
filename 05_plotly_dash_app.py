import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Load data
df = pd.read_csv("C:/Users/manav/Desktop/cleaned_data.csv")

# Initialize app
app = Dash(__name__)
app.title = "SpaceX Booster Reuse Dashboard"

# Layout
app.layout = html.Div([
    html.H1("🚀 SpaceX Booster Analysis", style={"textAlign": "center"}),
    
    html.Label("Select Landing Pad:"),
    dcc.Dropdown(
        id='pad-dropdown',
        options=[{'label': pad, 'value': pad} for pad in df['landingpad'].unique()],
        value=df['landingpad'].unique()[0]
    ),
    
    dcc.Graph(id='reuse-pie'),
    dcc.Graph(id='reused-histogram'),
])

# Callbacks
@app.callback(
    [Output('reuse-pie', 'figure'),
     Output('reused-histogram', 'figure')],
    [Input('pad-dropdown', 'value')]
)
def update_graphs(selected_pad):
    filtered_df = df[df['landingpad'] == selected_pad]

    # Pie chart: reused vs not
    pie_fig = px.pie(
        filtered_df, names='reused', title='Reused vs Not Reused',
        color_discrete_sequence=['red', 'green']
    )

    # Histogram: reused count distribution
    hist_fig = px.histogram(
        filtered_df, x='reusedcount', nbins=10,
        title='Distribution of Reused Counts',
        color='reused'
    )

    return pie_fig, hist_fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
