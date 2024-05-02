import streamlit as st
import pandas as pd
df = pd.read_csv('./data.csv')


def run_view() :
    
    st.header('주식정보 보기')
    st.subheader(' : Viewing stock information')
    st.text('주식을 검색하여 정보를 dataset으로 불러옵니다')
    st.text('기업의 Code는 주식 예측 도구에서 사용하므로 주식가치 예측을 원하면 Code를 복사해주세요')
    
    st.header('')
    
    if st.button(label='전체 데이터보기') :
        st.dataframe(df.iloc[:,1:], width=2000, height=550)
    
    st.header('')

    new_data = st.text_input('주식의 Name을 입력해주세요 ex)삼성, 현대')
    st.dataframe(df.iloc[:,1:][df['Name'].str.contains(new_data)], width=2000, height=450)