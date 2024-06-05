import streamlit as st

from streamlit_option_menu import option_menu



import LibGuide_Route,about_book,research


st.set_page_config(page_title="SaiScholar",page_icon="book",layout="wide")



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Main Menu',
                options=["LibGuide Route",'Know about your Book','Research'],
                icons=['chat-fill','book','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='cast',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'#89CFF0'},
        "icon": {"color": "black", "font-size": "15px"}, 
        "nav-link": {"color":"black","font-size": "15px", "text-align": "left", "margin":"-1px", "--hover-color": "#FFFCE4"},
        "nav-link-selected": {"background-color": "#E0F7FE"},}
                
                )

        
        if app == "LibGuide Route":
            LibGuide_Route.guide()
        if app == "Know about your Book":
            about_book.abtbook()
        if app=="Research":
            research.re()
          
             
          
             
    run()            
         