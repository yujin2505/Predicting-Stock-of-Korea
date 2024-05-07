import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from prophet import Prophet
import streamlit as st


def run_predict() :
    
    col1, col2, col3 = st.columns([1, 2.5, 1])
    
    with col2 :
        df = fdr.StockListing("KRX")
        df.reset_index(inplace=True, drop=True)
        
        st.title('Ⅱ. 주식가치 예측')
        st.subheader(' : Predicting stock value')
        st.text('기업 코드를 입력하여 한 기업의 과거 주식데이터를 prophet을 사용하여 미래 1년치')
        st.text('주식가치를 예측합니다.  Code를 모른다면 Viewing stock information를 참조하세요')
        st.header('')
        st.subheader('예측하고자 하는 기업의 Code입력하기')
        code = st.text_input('기업 Code를 입력하세요 ex)005930')

        if len(code) !=0 :
            
            st.text('검색한 기업의 주식 정보를 불러옵니다')
            st.dataframe(df.iloc[:,1:][code == df['Code']])
            
            df2 = fdr.DataReader(symbol=code) # 2000~2024년 4월까지의 데이터를 불러온다
            df2.reset_index(inplace=True)
            
            df2 = df2.iloc[ : , [0, 3+1]]
            
            df2.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)  #ds와 y로 바꾼다
            
            st.text('Prophet에 적용하기 위해 컬럼명을 ds와 y로 변경하였습니다.')
            st.dataframe(df2)
            
            # 1. 라이브러리를 변수로 만들고
            prophet = Prophet()
            
            # 2. 데이터로 학습시킨다
            prophet.fit(df2)

            # 3. 예측하고자 하는 기간을 정해서, 비어있는 데이터프레임을 만든다
            future = prophet.make_future_dataframe(periods=365, freq='D')  #365일

            # 4. 예측을 한다
            forecast = prophet.predict(future)
            
            st.text('현재시각 기준으로 1년치 데이터를 예측합니다.')
            st.dataframe(forecast)
            
            st.subheader('현재 시각 기준 데이터와 1년치 예상 주가에 대한 그래프입니다')
            fig1 = prophet.plot(forecast)
            st.pyplot(fig1)
            
            st.subheader('')
            
            st.subheader('기업의 연,월,주간 주가에 대한 예측치 그래프입니다')
            fig2 = prophet.plot_components(forecast)
            st.pyplot(fig2)