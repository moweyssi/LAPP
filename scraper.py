#import re
#import mechanize
#from bs4 import BeautifulSoup
#
#br = mechanize.Browser()
#br.set_handle_robots(False)
#br.addheaders = [('user-agent', '  Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
#br.open("https://eaccess.dumgal.gov.uk/online-applications/search.do?action=advanced&searchType=Application")
## follow second link with element text matching regular expression
#br.select_form('searchCriteriaForm')
#br['searchCriteria.reference'] = "18/1706/FUL"
#br.submit()


#soup = BeautifulSoup(br.response().read())

import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
#browser.open("https://eaccess.dumgal.gov.uk/online-applications/search.do?action=advanced&searchType=Application")
#browser.select_form()
#browser['searchCriteria.reference'] = "18/1706/FUL"
#browser.submit_selected()

