from PIL import Image #파이썬 이미지 라이브러리 PIL
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sb

#그래프 한글화하기
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')


def run_compare() :

    col1, col2, col3 = st.columns([1, 2.5, 1])
    
    with col2 :
        st.title('Ⅲ. 국내 ETF 주식가치비교')
        st.header(' : Comparing domestic ETF stock valuations')
        st.text('ETF데이터는 2024/4/29 기준 데이터입니다.')
        st.text('ETF는 하나의 주식으로 거래되지만 여러 자산에 대한 소유권을 가질 수 있게 해줍니다.')
        st.text('쉽게 말하면 여러 채권과 주식, 자산을 담고있는 하나의 상자로 표현됩니다.')
        st.text('주식은 분산투자하는 경우, risk가 서로 상쇄되어 안전성이 높아지기 때문에')
        st.text('그 자체로 분산투자가 가능한 ETF는 원금상실위험이 적은 안전한 투자대상으로 평가됩니다')
        
        etf_list = pd.read_csv('./KRETF.csv')

        st.header('')
        st.subheader('이자율(EarningRate) 높은 순서로 보기')
        st.text('이자율(EarningRate)은 일정 기간 동안 얻는 수입이나 수익의 속도를 나타내는 지표입니다.')
        
        # etf_list DataFrame에서 'EarningRate' 열을 내림차순으로 정렬
        etf_list = etf_list.sort_values(by='EarningRate', ascending=False)

        # 정렬된 DataFrame을 streamlit의 st.dataframe()에 전달
        etf_list = etf_list.iloc[:,[2,3,4,6,7,9]]
        st.dataframe(etf_list)
        
        st.header('')
        st.header('# ETF 카테고리별 이자율 보기')
        st.header('')
        
        etf_list2 = etf_list.groupby('Category')['EarningRate'].mean().reset_index()
        etf_list2.dropna(inplace=True)
        
        etf_list2.loc[etf_list2['Category'] == 1, 'Category_Name'] = '국내시장지수 ETF'
        etf_list2.loc[etf_list2['Category'] == 2, 'Category_Name'] = '국내업종/테마 ETF'
        etf_list2.loc[etf_list2['Category'] == 3, 'Category_Name'] = '국내파생'
        etf_list2.loc[etf_list2['Category'] == 4, 'Category_Name'] = '해외주식'
        etf_list2.loc[etf_list2['Category'] == 5, 'Category_Name'] = '원자재'
        etf_list2.loc[etf_list2['Category'] == 6, 'Category_Name'] = '채권'
        etf_list2.loc[etf_list2['Category'] == 7, 'Category_Name'] = '기타'

        etf_list2 = etf_list2[['Category','Category_Name','EarningRate']]
        
        st.subheader('1. 국내시장지수 ETF')
        st.text('국내시장지수 ETF는 우리나라 증시를 추종하는 ETF입니다')
        st.subheader('2. 국내업종/테마 ETF')
        st.text('TIGER 2차전지테마, KODEX삼성그룹과 같은 특정 테마에 투자하는 ETF들이 상장되어 있습니다')
        st.subheader('3. 국내파생')
        st.text('국내파생ETF상품은 레버리지, 인버스 ETF들을 말합니다')
        st.text('레버리지 ETF는 추종지수의 2배수로 수익률을 낼 수 있는 상품입니다')
        st.text('반대로 지수가 1% 하락하면 ETF는 2% 손실을 보게 됩니다')
        st.subheader('4. 해외주식')
        st.text('미국의 S&P500지수 또는 나스닥지수를 추종하는 ETF 등 해외주식을 추종하는 ETF들이 있습니다.')
        st.subheader('5. 원자재')
        st.text('원자재 ETF는 원유, 금선물 등의 시세를 추종하는 ETF 입니다 특징은 롤오버비용, 괴리율이 크게 발생하여')
        st.text('추종지수를 잘 따라가지 못하는 경우가 많아 투자시에 주의가 필요하다는 것입니다.')
        st.subheader('6. 채권')
        st.text('채권형 ETF는 국채 등의 지수에 투자하는 상품입니다')
        st.subheader('7. 기타')
        st.text('KODEX달러선물 ETF, TIGER일본엔선물 ETF 등이 있습니다')
        st.text('달러가격 상승 또는 일본엔화의 상승을 예상한다면 투자할 수 있는 상품들입니다')
        st.header('')
        
        choice = st.selectbox('카테고리를 선택하세요', etf_list2['Category_Name'])
        
        if choice == '국내시장지수 ETF' :
            st.dataframe(etf_list.loc[etf_list['Category']==1], width=2000, height=350)
        elif choice == '국내업종/테마 ETF' :
            st.dataframe(etf_list.loc[etf_list['Category']==2], width=2000, height=350)
        elif choice == '국내파생' :
            st.dataframe(etf_list.loc[etf_list['Category']==3], width=2000, height=350)
        elif choice == '해외주식' :
            st.dataframe(etf_list.loc[etf_list['Category']==4], width=2000, height=350)
        elif choice == '원자재' :
            st.dataframe(etf_list.loc[etf_list['Category']==5], width=2000, height=350)
        elif choice == '채권' :
            st.dataframe(etf_list.loc[etf_list['Category']==6], width=2000, height=350)
        else :
            st.dataframe(etf_list.loc[etf_list['Category']==7], width=2000, height=350)
        
        
        st.header('')
        st.header('')
        st.subheader('Category별 최저, 최대 이자율')
        st.header('')
        st.text('최저, 최대 이자율을 알 수 있습니다. 이자율이 마이너스인 경우, 원금보장이 어렵습니다')


        etf_list3 = etf_list.groupby('Category')['EarningRate'].max().reset_index()
        etf_list3['Category_Name'] = etf_list2['Category_Name']
        etf_list3 = etf_list3.sort_values('EarningRate',ascending=False)
        etf_list3 = etf_list3[['Category','Category_Name','EarningRate']]
        st.dataframe(etf_list3)
        
        etf_list4 = etf_list.groupby('Category')['EarningRate'].min().reset_index()
        etf_list4['Category_Name'] = etf_list2['Category_Name']
        etf_list4 = etf_list4.sort_values('EarningRate')
        etf_list4 = etf_list4[['Category','Category_Name','EarningRate']]
        st.dataframe(etf_list4)
        
        fig1 = plt.figure(figsize=(6,6))
        plt.grid(True)
        plt.bar(data=etf_list ,x='Category',height='EarningRate', width=0.6, color='pink')
        plt.axhline(y=0, color='black')  # y축 진하게
        plt.xticks([2,4,5,3,1,7,6],['국내업종/테마 ETF','해외주식','원자재','국내파생','국내시장지수 ETF','기타','채권'],rotation=45)
        plt.title('카테고리별 최저,최대 이자율 그래프')
        plt.ylabel('이자율')
        st.pyplot(fig1)

        
        st.header('')
        st.header('')
        st.subheader('Category별 EarningRate의 평균')
        st.dataframe(etf_list2.sort_values(by='EarningRate',ascending=False))
        
        
        etf_list2 = etf_list2.sort_values('EarningRate',ascending=False)
        
        st.header('')
        st.text('카테고리별 이자율 평균을 높은 순서대로 정렬하였습니다')
        fig = plt.figure(figsize=(6,6))

        X = [1, 3, 5, 7, 9, 11, 13]

        plt.bar(X, etf_list2['EarningRate'], width=1.25, color='orange')
        plt.axhline(y=0, color='black')  # y축 진하게
        plt.title('카테고리별 이자율 평균 그래프')
        plt.ylabel('이자율 평균')
        plt.grid(True)
        
        ticklabel = ['국내시장지수 ETF', '국내업종/테마 ETF', '해외주식', '원자재', '기타', '국내파생', '채권']
        plt.xticks(X, ticklabel, rotation=45)

        st.pyplot(fig)

