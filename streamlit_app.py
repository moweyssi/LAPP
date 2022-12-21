import streamlit as st
import streamlit.components.v1 as components
import mechanize
from bs4 import BeautifulSoup

#br = mechanize.Browser()
#br.set_handle_robots(False)
#br.addheaders = [('user-agent', '  Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
#br.open("https://eaccess.dumgal.gov.uk/online-applications/search.do?action=advanced&searchType=Application")
## follow second link with element text matching regular expression
#br.select_form('searchCriteriaForm')
#br['searchCriteria.reference'] = "18/1706/FUL"
#br.submit()
#soup = BeautifulSoup(br.response().read())
#print(soup)
#st.markdown(soup,unsafe_allow_html=True)
#components.html(html=soup,height=600)

import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://wam.highland.gov.uk/wam/search.do?action=advanced")
st.markdown(browser.page(),unsafe_allow_html=True)