import streamlit as st

st.title("Student Result Prediction")

hours = st.slider("Study Hours", 1, 12, 5)

if st.button("Predict"):

    if hours >= 5:
        st.success("Pass")
    else:
        st.error("Fail")
