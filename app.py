import streamlit as st

st.title("Force Open Google in a New Tab")

if st.button("Open Google"):
    # Inject JavaScript to open a new tab when the button is pressed
    st.markdown("""
        <script>
        window.open('https://www.google.com', '_blank');
        </script>
        """, unsafe_allow_html=True)