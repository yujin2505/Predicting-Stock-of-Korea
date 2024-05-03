import streamlit as st
import pandas as pd
df = pd.read_csv('./data.csv')

from PIL import Image #파이썬 이미지 라이브러리 PIL

def run_view() :
    
    st.title('주식정보 보기')
    st.header(' : Viewing stock information')
    st.subheader('')
    st.text('주식을 검색하여 정보를 dataset으로 불러옵니다')
    st.text('기업의 Code는 주식 예측 도구에서 사용하므로 주식가치 예측을 원하면 Code를 복사해주세요')
    
    st.header('')
    
    if st.button(label='전체 데이터보기') :
        st.dataframe(df.iloc[:,1:], width=2000, height=550)
    
    st.header('')
    st.subheader('컬럼(columns)에 대한 설명입니다')
    img = Image.open('./view_column.png') 
    st.image(img, use_column_width=True) #width=True해주면 자동으로 폭을 맞춰준다
    
    st.header('')

    new_data = st.text_input('주식의 Name을 입력해주세요 ex)삼성, 현대')
    st.dataframe(df.iloc[:,1:][df['Name'].str.contains(new_data)], width=2000, height=450)
    
    