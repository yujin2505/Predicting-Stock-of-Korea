import streamlit as st
from PIL import Image #파이썬 이미지 라이브러리 PIL

def run_home() :
    
    # 화면을 2분할 하여 스크롤을 내리지 않고 함께 출력하게 할 것이다
    col1, col2= st.columns([2.3, 2])  
    
    with col1 :
        
        # 전체 프로젝트에 대한 설명
        
        st.title('Predicting Stock of Korea')
        st.subheader(' ')
        st.link_button('데이터 출처 바로가기','https://github.com/FinanceData/FinanceDataReader')
        st.text('데이터 출처 : FinanceDataReader라이브러리')
        st.text('데이터는 라이브러리에서 실시간으로 반영됩니다!')
        st.subheader(' ')
        st.text('국내 주식을 검색하면 보여주고, 기업코드를 입력하면 기업의 미래 1년치 주식가치를 ')
        st.text('프로펫(prophet)기법을 사용하여 예측하고 년,월,주간의 주가 흐름을 그래프로 나타내었습니다')
        st.text('비교적 안정적인 리턴(return)을 가져오는 국내 ETF 주식을 ')
        st.text('이자율(EarningRate)을 중심으로 비교하였습니다')        
        st.subheader(' ')
        
        # 메인 화면에 넣을 사진
        img = Image.open('./stock1.png')  
        st.image(img, width=650)
            
            
    with col2 :
        
        # 목차
        
        st.header(' ')
        st.header(' ')
        st.header(' ')
        st.header('- 목차 -')
        st.subheader('')
        
        st.subheader('Ⅰ. 주식정보 보기')
        st.subheader(' : Viewing stock information')
        st.text('기업 Name을 입력받아 기업 주식에 대한 정보를 dataset으로 불러옵니다')
        st.subheader('')
        
        st.subheader('Ⅱ. 주식가치 예측')
        st.subheader(' : Predicting stock value')
        st.text('주식데이터를 prophet(프로펫) 기법을 사용하여')
        st.text('미래 1년치 주식가치를 예측합니다')
        st.subheader('')
        
        st.subheader('Ⅲ. 국내 ETF 주식가치비교')
        st.subheader(' : Comparing domestic ETF stock valuations')
        st.text('안정적인 return을 가져오는 국내 ETF주식을 종목별(카테고리별)로 비교합니다')
            