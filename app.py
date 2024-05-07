import streamlit as st
from app_home import run_home
from app_predict import run_predict  #다른 파일의 def함수를 가져와서 쓰는방법
from app_view import run_view
from app_compare import run_compare
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

def main():
        
    menu = ['Project Description','Viewing Stock Information','Predicting Stock Value','Comparing Domestic ETF']
    
    with st.sidebar :
        choice = option_menu(' ',menu,
                             icons=["house",'bi bi-search',"bi bi-graph-up-arrow","bi bi-file-earmark-bar-graph"] , menu_icon="bi bi-buildings", default_index=0,
                            )
    
    if choice == menu[0] :
        run_home()
    elif choice == menu[1]: 
        run_view()          #다른 파일의 def함수를 가져와서 쓰는방법
    elif choice == menu[2]:
        run_predict()
    elif choice == menu[3]:
        run_compare() 


if __name__ == '__main__':
    main()