import pandas as pd
import plotly.express as px

df=pd.read_csv('covid.csv')
fig=px.scatter(df,x='date',y='cases',color='country',title='NUMBER OF COVID CASES')
fig.show()