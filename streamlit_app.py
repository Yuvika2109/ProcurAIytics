import streamlit as st
def login():
  
    st.markdown(
    """
     <h1 style="text-align: center;">Welcome to ProcurAlytics🤖</h1>
     <h6 style="text-align: center;">A generative AI application</h6>
      <h4 style="text-align: center;">LOGIN</h4>
    """,
    unsafe_allow_html=True,
)
   
    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")


    if st.button("Login"):
        if username == "tsdpl" and password == "1234":
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
   
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {visibility: hidden; width: 0;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    login()
else:

    st.set_page_config(layout="wide")
    with st.sidebar:
        st.text("A Generative AI Application")
        if st.button("Logout"):
            st.session_state.logged_in = False  

    
      
    about = st.Page(
        page="views/about.py",
        title="About the project",
        icon=":material/account_circle:",
        default=True,
    )
    project_1_page = st.Page(
        page="views/spend.py",
        title="Visualization of Spend Categorization",
        icon=":material/bar_chart:",
    )
    project_2_page = st.Page(
        page="views/chatbot.py",
        title="Chatbot",
        icon=":material/smart_toy:",
    )

    pg = st.navigation(
        {
            "Info": [about],
            "Projects": [project_1_page, project_2_page],
        }
    )
    pg.run()