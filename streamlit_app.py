import streamlit as st

pkinross = "https://planningapps.pkc.gov.uk/online-applications/search.do?action=advanced&searchType=Application"
slanarkshire = "https://publicaccess.southlanarkshire.gov.uk/online-applications/search.do?action=advanced"
dumgal = "https://eaccess.dumgal.gov.uk/online-applications/search.do?action=advanced&searchType=Application"
highland = "https://wam.highland.gov.uk/wam/search.do?action=advanced"
argbute = "https://publicaccess.argyll-bute.gov.uk/online-applications/search.do?action=advanced"
renfrewshire = "https://pl-bs.renfrewshire.gov.uk/online-applications/search.do?action=advanced"
fife = "https://planning.fife.gov.uk/online/search.do?action=advanced"
borders = "https://eplanning.scotborders.gov.uk/online-applications/search.do?action=advanced"
angus = "https://planning.angus.gov.uk/online-applications/search.do?action=advanced"
tayside = "https://idoxwam.dundeecity.gov.uk/idoxpa-web/search.do?action=advanced"
strathclyde = "https://publicaccess.glasgow.gov.uk/online-applications/search.do?action=advanced"
grampian = "https://publicaccess.aberdeencity.gov.uk/online-applications/search.do?action=advanced"
westlothian = "https://planning.westlothian.gov.uk/publicaccess/search.do?action=advanced"
midlothian = "https://planning-applications.midlothian.gov.uk/OnlinePlanning/search.do?action=advanced"
eastlothian = "https://pa.eastlothian.gov.uk/online-applications/search.do?action=advanced"
shetland = "https://pa.shetland.gov.uk/online-applications/search.do?action=advanced"
marine = "https://marine.gov.scot/marine-licence-applications"

authorities = [
    #"Perth and Kinross",
    "South Lanarkshire",
    "Dumfries and Galloway",
    "Highland",
    "Argyll and Bute",  
    "Renfrewshire",   
    "Fife",
    "Borders",
    "Angus",
    "Tayside/Dundee",
    "Strathclyde/Glasgow",
    "Grampian/Aberdeen",
    "West Lothian",
    "Midlothian",
    "East Lothian",
    "Shetland",
    "Marine"
    ]
links = [
    #pkinross,
    slanarkshire,
    dumgal,
    highland,
    argbute,
    renfrewshire,
    fife,
    borders,
    angus,
    tayside,
    strathclyde,
    grampian,
    westlothian,
    midlothian,
    eastlothian,
    shetland,
    marine
    ]
choice = st.selectbox("Local Authority",authorities)

for i in range(len(links)):
    if choice==authorities[i]:
        #st.write("[LAPP](%s)" % links[i]) 

        st.write('''
            <a target="_blank" href={}>
                <button>
                    Local Authority Planning Portal
                </button>
            </a>
            '''.format(links[i]),
            unsafe_allow_html=True
        )

companyhouse = "https://find-and-update.company-information.service.gov.uk/"

st.write(f'''
    <a target="_blank" href="https://find-and-update.company-information.service.gov.uk/">
        <button>
            Companies House
        </button>
    </a>
    ''',
    unsafe_allow_html=True
)