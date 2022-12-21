import streamlit as st
import streamlit.components.v1 as components
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("https://eaccess.dumgal.gov.uk/online-applications/search.do?action=advanced&searchType=Application")
# follow second link with element text matching regular expression
br.select_form('searchCriteriaForm')
br['searchCriteria.reference'] = "18/1706/FUL"
br.submit()
soup = BeautifulSoup(br.response().read())
components.html(html=soup,height=600)
