import streamlit as st
import pandas as pd
from PIL import Image   # 파이썬 이미지 라이브러리 PIL
import FinanceDataReader as fdr

df = fdr.StockListing("KRX")

def run_view() :
    
    col1, col2, col3 = st.columns([1, 2.5, 1])  # 화면의 가운데 정렬을 위해 사용함
    
    with col2 :
        st.title('Ⅰ. 주식정보 보기')
        st.header(' : Viewing stock information')
        st.subheader('')
        st.text('주식을 검색하여 정보를 dataset으로 불러옵니다')
        st.text('기업의 Code는 주식 예측 도구에서 사용하므로 주식가치 예측을 원하면 Code를 복사해주세요')
        st.header('')

        # 전체 데이터보기
        if st.button(label='전체 데이터보기') :
            st.dataframe(df, width=2000, height=550)
        
        st.header('')
        st.subheader('컬럼(columns)에 대한 설명입니다')
        
        # 컬럼 설명에 대한 이미지
        img = Image.open('./view_column.png')  
        st.image(img, width=800) 
        
        st.header('')

    # 데이터 검색하면 데이터프레임 출력하게하기
    new_data = st.text_input('주식의 Name을 입력해주세요 ex)삼성, 현대')
    st.dataframe(df.loc[df['Name'].str.contains(new_data)], width=2000, height=450)
        
    