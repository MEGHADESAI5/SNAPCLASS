import streamlit as st

def style_background_home():

    st.markdown(""" 
        <style>

                .stApp{
                    background: #5865F2  !important;
                }   
                
                
                
                """
                ,unsafe_allow_html=True)

def style_background_dashboard():

    st.markdown(""" 
        <style>

                .stApp{
                    background: #E0E3FF  !important;
                }   
                
                
                
                """
                ,unsafe_allow_html=True)
    
def style_base_layout():

    st.markdown(""" 
        <style>
                @import url('https://fonts.googleapis.com/css2?family=PT+Serif:ital,wght@0,400;0,700;1,400;1,700&family=Public+Sans:ital,wght@0,100..900;1,100..900&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=PT+Serif:ital,wght@0,400;0,700;1,400;1,700&family=Public+Sans:ital,wght@0,100..900;1,100..900&display=swap');
        /* Hide top bar */
            # MainMenu , footer , header {
                visibility: hidden;
            }
                
            .block-container{
                padding-top:1.5rem !important;
            }
                
            
                
                
        </style>     
                
                """
                ,unsafe_allow_html=True)