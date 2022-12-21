import streamlit as st
import webbrowser

dumgal = "https://eaccess.dumgal.gov.uk/online-applications/search.do?action=advanced&searchType=Application"
highland = "https://wam.highland.gov.uk/wam/search.do?action=advanced"
argbute = "https://publicaccess.argyll-bute.gov.uk/online-applications/search.do?action=advanced"
choice = st.selectbox("Local Authority",["Dumfries and Galloway","Highland","Argyll and Bute"])

if choice == "Dumfries and Galloway":
    st.markdown("[LAPP](%s)" % dumgal)
elif choice == "Highland":
    st.markdown("[LAPP](%s)" % highland)