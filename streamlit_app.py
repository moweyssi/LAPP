import streamlit as st
import webbrowser

dumgal = "https://eaccess.dumgal.gov.uk/online-applications/search.do?action=advanced&searchType=Application"
highland = "https://wam.highland.gov.uk/wam/search.do?action=advanced"
argbute = "https://publicaccess.argyll-bute.gov.uk/online-applications/search.do?action=advanced"
st.selectbox("Local Authority",["Dumfries and Galloway","Highland","Argyll and Bute"])

st.markdown(f'''
<a href={dumgal}><button style="background-color:GreenYellow;">Stackoverflow</button></a>
''',
unsafe_allow_html=True)