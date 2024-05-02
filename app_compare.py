from PIL import Image #파이썬 이미지 라이브러리 PIL
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def run_compare() :

    img = Image.open('./ETF.png') #저장되어있는 이미지 파일을 화면에 표시하는 방법
    st.image(img, use_column_width=True) #width=True해주면 자동으로 폭을 맞춰준다
    
    df1 = pd.read_csv('./KRETF.csv')
    
    
    
    column_list = df1['Category'].unique()
  
    choice_list = st.multiselect('etf 카테고리를 선택하세요', column_list)
    
    if df1[choice_list == df1['Category']] :

        st.line_chart(df1)