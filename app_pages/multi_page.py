
import streamlit as st


class MultiPage:
    """ Class to generate multiple Streamlit pages using an object
    oriented approach
    """

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="💻"
        )

    def app_page(self, title, func) -> None:
        """ use this method to add the pages to the object
        and appends title"""
        self.pages.append({"title": title, "function": func})

    def run(self):
        """Set title on each pages and menu names"""
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages,
                                format_func=lambda page: page['title'])
                                #  radio button for  each of the pages in the application. 
        page['function']()