# Interactive visualizations with Plotly
# This works in JupyterLab without any extensions

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Set renderer for JupyterLab compatibility
import plotly.io as pio
pio.renderers.default = "notebook"

# Create sample data
df = pd.DataFrame({
    'column1': np.random.randn(100),
    'column2': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100),
    'size': np.random.randint(10, 100, 100)
})

# Interactive scatter plot
fig = px.scatter(
    df, 
    x='column1', 
    y='column2', 
    color='category',
    size='size',
    title='Interactive Scatter Plot',
    hover_data=['category', 'size']
)
fig.show()

# Interactive line plot with multiple traces
dates = pd.date_range('2024-01-01', periods=100)
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=dates, y=np.random.randn(100).cumsum(), name='Series 1'))
fig2.add_trace(go.Scatter(x=dates, y=np.random.randn(100).cumsum(), name='Series 2'))
fig2.update_layout(title='Time Series Plot', xaxis_title='Date', yaxis_title='Value')
fig2.show()

# 3D scatter plot
fig3 = px.scatter_3d(
    df, 
    x='column1', 
    y='column2', 
    z='size',
    color='category',
    title='3D Scatter Plot'
)
fig3.show()
