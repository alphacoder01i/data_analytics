import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load Data
df = pd.read_csv('country_vaccinations.csv')
df_manuf = pd.read_csv('country_vaccinations_by_manufacturer.csv')

# App Initialization
app = dash.Dash(__name__)
app.title = 'COVID Vaccination Dashboard'

# Layout
app.layout = html.Div([
    html.H1("🌍 COVID-19 Vaccination Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Select Country:"),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': c, 'value': c} for c in sorted(df['country'].unique())],
            value='India',
            clearable=False
        ),
    ], style={'width': '40%', 'margin': 'auto'}),

    html.Br(),

    dcc.Tabs([
        dcc.Tab(label='📈 Vaccination Trends', children=[
            dcc.Graph(id='total-vaccinations-line'),
            dcc.Graph(id='daily-vaccinations-bar'),
        ]),

        dcc.Tab(label='🏭 Manufacturer Comparison', children=[
            dcc.Graph(id='manufacturer-line'),
        ])
    ])
])

# Callbacks
@app.callback(
    Output('total-vaccinations-line', 'figure'),
    Output('daily-vaccinations-bar', 'figure'),
    Output('manufacturer-line', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graphs(selected_country):
    country_df = df[df['country'] == selected_country]
    manuf_df = df_manuf[df_manuf['location'] == selected_country]

    # Line chart: Total vaccinations
    fig1 = px.line(
        country_df, x='date', y='total_vaccinations',
        title=f'Total Vaccinations in {selected_country}',
        labels={'date': 'Date', 'total_vaccinations': 'Total Vaccinations'}
    )

    # Bar chart: Daily vaccinations
    fig2 = px.bar(
        country_df, x='date', y='daily_vaccinations',
        title=f'Daily Vaccinations in {selected_country}',
        labels={'date': 'Date', 'daily_vaccinations': 'Daily Vaccinations'}
    )

    # Line chart: Manufacturer
    fig3 = px.line(
        manuf_df, x='date', y='total_vaccinations', color='vaccine',
        title=f'Vaccines by Manufacturer in {selected_country}',
        labels={'date': 'Date', 'total_vaccinations': 'Total by Manufacturer'}
    )

    return fig1, fig2, fig3

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
