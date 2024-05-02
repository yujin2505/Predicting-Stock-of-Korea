import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from prophet import Prophet
import streamlit as st


def run_predict() :
    
    df = pd.read_csv('./data.csv')
    df.reset_index(inplace=True, drop=True)
    
    st.header('주식가치 예측')
    st.subheader(' : Predicting stock value')
    st.text('기업 코드를 입력하여 한 기업의 2000~2024년 주식데이터를 prophet을 사용하여 미래 1년치')
    st.text('주식가치를 예측합니다 Code를 알지 못한다면 Viewing stock information를 참조하세요')
    
    st.header('')
    code = st.text_input('예측을 원하는 기업의 주식의 Code를 입력하세요   ex)005930')

    if len(code) !=0 :
        st.dataframe(df.iloc[:,1:][code == df['Code']])
        
        df2 = fdr.DataReader(symbol=code) # 2000~2024년 4월까지의 데이터를 불러온다
        df2.reset_index(inplace=True)
        
        df2 = df2.iloc[ : , [0, 3+1]]
        
        df2.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)  #ds와 y로 바꾼다
        
        # 1. 라이브러리를 변수로 만들고
        prophet = Prophet()
        
        # 2. 데이터로 학습시킨다
        prophet.fit(df2)

        # 3. 예측하고자 하는 기간을 정해서, 비어있는 데이터프레임을 만든다
        future = prophet.make_future_dataframe(periods=365, freq='D')  #365일

        # 4. 예측을 한다
        forecast = prophet.predict(future)
        
        st.dataframe(forecast)
        
        fig1 = prophet.plot(forecast)
        st.pyplot(fig1)

        fig2 = prophet.plot_components(forecast)
        st.pyplot(fig2)