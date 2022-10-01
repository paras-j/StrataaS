import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

    
    


st.title("Get financials from SEC Edgar")

import pandas as pd
import numpy as np
import requests
import plotly.graph_objects as go

option = st.sidebar.selectbox("Which company?", ('CIK0000320193','CIK0000789019','CIK0001652044','CIK0001326801','CIK0001739104','CIK0001090727','CIK0001318605'), 3)

#response = requests.get(f"https://data.sec.gov/api/xbrl/companyfacts/{option}.json", headers=headers)
response = requests.get("https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json")

#data = pd.json_normalize(response.json())
data = response.json()
st.write(data)

# for message in data['messages']:
#     st.image(message['user']['avatar_url'])
#     st.write(message['user']['username'])
#     st.write(message['created_at'])
#     st.write(message['body'])
