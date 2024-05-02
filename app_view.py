import streamlit as st
import pandas as pd
df = pd.read_csv('./data.csv')


def run_view() :
    
    st.header('주식정보 보기')
    st.subheader(' : Viewing stock information')
    st.subheader('주식을 검색하여 정보를 dataset으로 불러옵니다')
    st.subheader('<2024/04/29 기준 주식정보>')
    
    st.header('')
    
    if st.button(label='전체 데이터보기') :
        st.dataframe(df, width=2000, height=550)

    new_data = st.text_input('알고자하는 주식의 Name을 입력하세요 ex)삼성, 현대')
    st.dataframe(df[df['Name'].str.contains(new_data)], width=2000, height=450)