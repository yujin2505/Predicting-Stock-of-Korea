from PIL import Image #파이썬 이미지 라이브러리 PIL
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


def run_compare() :

    st.header('국내 ETF 주식가치비교')
    st.subheader(' : Comparing domestic ETF stock valuations')
    st.text('ETF는 하나의 주식으로 거래되지만 여러 자산에 대한 소유권을 가질 수 있게 해줍니다.')
    st.text('ETF는 여러 채권과 주식, 자산을 담고있는 하나의 상자로 표현됩니다.')
    st.text('주식은 분산투자하는 경우, risk가 서로 상쇄되어 안전성이 높아집니다')
    st.text('그 자체로 분산투자가 가능한 ETF는 원금상실위험이 적은 안전한 투자대상으로 평가됩니다')
    
    etf_list = pd.read_csv('./KRETF.csv')

    st.header('')
    st.subheader('EarningRate가 높은 순서로 보기')
    
    # etf_list DataFrame에서 'EarningRate' 열을 내림차순으로 정렬
    sorted_etf_list = etf_list.sort_values(by='EarningRate', ascending=False)

    # 정렬된 DataFrame을 streamlit의 st.dataframe()에 전달
    st.dataframe(sorted_etf_list.iloc[:,1:])
    
    st.subheader('Category별로 보기')
    img = Image.open('./ETF.png') #저장되어있는 이미지 파일을 화면에 표시하는 방법
    st.image(img, use_column_width=True) #width=True해주면 자동으로 폭을 맞춰준다
    
    choice = st.selectbox('그룹을 선택하세요', np.arange(1,7+1))
            
    st.dataframe(etf_list[ etf_list['Category']==choice , ])
    
    st.subheader('Category별 EarningRate의 평균')
    chart = etf_list.groupby('Category')['EarningRate'].mean()

    fig = px.bar(chart)
    st.plotly_chart(fig)
    
    st.dataframe(chart)