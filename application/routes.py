from application import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

@app.route('/')
def index():
    # Graph One
    df = px.data.medals_wide()
    fig1 = px.bar(df, x='nation', y=['gold','silver','bronze'], title='Wide=Form Input')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Graph Two
    df2 = px.data.iris()
    fig2 = px.scatter_3d(df2, x='sepal_length', y="sepal_width", z="petal_width", color="species", title="Iris Dataset")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', title='Index', graph1JSON=graph1JSON, graph2JSON=graph2JSON)