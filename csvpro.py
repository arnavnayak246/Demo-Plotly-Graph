import pandas as pd
import plotly.express as px
df = pd.read_csv("line_chart.csv")
fig = px.line(df,x="Year",y="Avg. Covid Cases Per Year",color="Country",title="International Covid Graph")

fig.show()