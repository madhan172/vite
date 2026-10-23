import streamlit as st

st.title("Student Performance Predictor")

hours = st.slider("Study Hours", 1, 12, 5)
attendance = st.slider("Attendance %", 0, 100, 75)

if st.button("Predict"):

    if hours >= 5 and attendance >= 60:
        st.success("Pass")
    else:
        st.error("Fail")

st.caption("Educational ML Demo Application")if hours >= 5 and attendance >= 60:
    st.success("Student is likely to PASS")
    st.metric("Success Rate", "85%")
else:
    st.error("Student is likely to FAIL")
    st.metric("Success Rate", "35%")
st.caption(
    "This is an educational machine learning demonstration project."
)
