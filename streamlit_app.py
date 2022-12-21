import streamlit as st

dumgal = "https://eaccess.dumgal.gov.uk/online-applications/search.do?action=advanced&searchType=Application"
highland = "https://wam.highland.gov.uk/wam/search.do?action=advanced"
argbute = "https://publicaccess.argyll-bute.gov.uk/online-applications/search.do?action=advanced"
renfrewshire = "https://pl-bs.renfrewshire.gov.uk/online-applications/search.do?action=advanced"
fife = "https://planning.fife.gov.uk/online/search.do?action=advanced"

authorities = ["Dumfries and Galloway","Highland","Argyll and Bute","Renfrewshire","Fife"]
links = [dumgal,highland,argbute,renfrewshire,fife]
choice = st.selectbox("Local Authority",authorities)

#if choice == authorities[0]:
#    st.markdown("[LAPP](%s)" % links[0])
#elif choice == authorities[1]:
#    st.markdown("[LAPP](%s)" % links[1])
#elif choice == authorities[2]:
#    st.markdown("[LAPP](%s)" % links[3])
for i in range(len(links)):
    if choice==authorities[i]:
        st.write("[LAPP](%s)" % links[i])  