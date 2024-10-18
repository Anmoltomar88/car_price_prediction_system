import streamlit as st
from modules import homepage, predict, contact_us

st.set_page_config(page_title="Car Price Prediction", layout="wide")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.markdown("<h2>📚 Navigation</h2>", unsafe_allow_html=True)

if 'current_page' not in st.session_state:
    st.session_state.current_page = '🏠 Home'

if st.sidebar.button("🏠 Home"):
    st.session_state.current_page = '🏠 Home'
if st.sidebar.button("🚗 Predict"):
    st.session_state.current_page = '🚗 Predict'
if st.sidebar.button("✉️ Contact Us"):
    st.session_state.current_page = '✉️ Contact Us'

if st.session_state.current_page == "🏠 Home":
    homepage.show()
elif st.session_state.current_page == "🚗 Predict":
    predict.show()
elif st.session_state.current_page == "✉️ Contact Us":
    contact_us.show()

# st.markdown(
#     """
#     <div class="footer">
#         <p>© 2024 Car Price Prediction App. All rights reserved. Developed by Anmol.</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
