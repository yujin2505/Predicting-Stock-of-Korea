import streamlit as st
import pandas as pd

df = pd.read_csv('./data.csv')

name = df['Name']
code = df['Code']


def run_predict() :
    
    st.title('주식가치 1년치 예측하기')
    st.subheader('2000~2024년 데이터를 통해 미래 1년치 주식가치를 예측합니다')
    
    if new_data.isdigit():
        df[new_data == code]
        st.text(f"'{code}'을(를) 입력하셨습니다")
    
    
    else :
        new_data = new_data.strip()
        df[new_data == name]
        st.text(f"'{name}'을(를) 입력하셨습니다")