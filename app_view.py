import streamlit as st
import pandas as pd
df = pd.read_csv('./data.csv')


def run_view() :

    new_data = st.text_input('어떤 주식이 궁금하세요?')
    
    if st.button(label='전체 데이터보기') :
        st.dataframe(df)
