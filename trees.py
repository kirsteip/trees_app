import streamlit as st
import pandas as pd
import plotly.express as px
import requests

from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.title('Trees')
st.write(
    """This app analyzes trees in San Francisco using
    a dataset kindly provided by SF DPW"""
)

trees_df = pd.read_csv('trees.csv')

df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
#st.write(trees_df.head())

st.scatter_chart(df_dbh_grouped)
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

df_dbh_grouped2 = pd.DataFrame(trees_df.groupby(['caretaker']).count()['tree_id'])
st.area_chart(df_dbh_grouped2)
st.data_editor(trees_df)
trees_df.loc[trees_df.index] = trees_df

if st.button("Save data and overwrite"):
    trees_df.to_csv("trees.csv", index=False)
    st.write("Saved!")

profile = ProfileReport(trees_df, explorative=True)
st_profile_report(profile)