import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

st.header("_Streamlit_ is :blue[cool] :sunglasses:")

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
