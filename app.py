if hours >= 5 and attendance >= 60:
    st.success("✅ Student is likely to PASS")
    st.metric("Success Rate", "85%")
else:
    st.error("❌ Student is likely to FAIL")
    st.metric("Success Rate", "35%")
