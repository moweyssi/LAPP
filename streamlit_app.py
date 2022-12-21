import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
#components.iframe("https://eaccess.dumgal.gov.uk/")
components.html(html="""<!DOCTYPE html>
      <html>
        <head>
          <title> Title of the document<title>
        </head>
          <body>
    <center>
        <h1 style="color:green">Talkers code</h1>
        <!-- this is only for educational purposes -->
        <p>Alternative of iframe tag</p>
        <embed src="https://www.talkerscode.com" width="1000" height="500" style="border: 1px solid white; box-shadow: 0 0 5px black;" />
    </center>
   </body>
</html>""",height=600)