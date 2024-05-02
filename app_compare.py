from PIL import Image #파이썬 이미지 라이브러리 PIL
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


def run_compare() :

    st.header('국내 ETF 주식가치비교')
    st.subheader(' : Comparing domestic ETF stock valuations')
    
    etf_list = pd.read_csv('./KRETF.csv')
    
    st.subheader('EarningRate가 높은 순서로 보기')
    
    # etf_list DataFrame에서 'EarningRate' 열을 내림차순으로 정렬
    sorted_etf_list = etf_list.sort_values(by='EarningRate', ascending=False)

    # 정렬된 DataFrame을 streamlit의 st.dataframe()에 전달
    st.dataframe(sorted_etf_list)
    
    st.subheader('Category별로 보기')
    img = Image.open('./ETF.png') #저장되어있는 이미지 파일을 화면에 표시하는 방법
    st.image(img, use_column_width=True) #width=True해주면 자동으로 폭을 맞춰준다
    
    choice = st.selectbox('그룹을 선택하세요', np.arange(1,7+1))
            
    st.dataframe(etf_list.loc[ etf_list['Category']==choice , ])
    
    
    st.subheader('Category별 EarningRate의 평균')
    chart = etf_list.groupby('Category')['EarningRate'].mean()

    fig = px.bar(chart)
    st.plotly_chart(fig)
    
    st.dataframe(chart)