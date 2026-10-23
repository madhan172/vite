import streamlit as st

st.title("Student Performance Predictor")

hours = st.slider("Study Hours", 1, 12, 5)
attendance = st.slider("Attendance %", 0, 100, 75)

if st.button("Predict"):

    if hours >= 5 and attendance >= 60:
        st.success("Pass")
    else:
        st.error("Fail")

st.caption("Educational ML Demo Application")
