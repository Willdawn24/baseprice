import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot 

def plot(feedcode: str):
    df = pd.DataFrame([1,2,3,4,5], columns=['col'])
    layout = {'title': feedcode}
    fig = plot({'data': [go.Scatter(x = df.index, y = df['col'], name = "series")],
                'layout': layout}, output_type = 'div')
    return fig