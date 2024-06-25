# import streamlit as st

# st.title*("my first app")

# """
# stremlits files runs below like this
# go to the folder 
# them stremlit appname.py

import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)