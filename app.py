import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

st.header("_Streamlit_ is :blue[cool] :sunglasses:")

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)
