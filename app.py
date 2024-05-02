import streamlit as st
from app_predict import run_predict  #다른 파일의 def함수를 가져와서 쓰는방법
from app_view import run_view
from app_compare import run_compare

from PIL import Image #파이썬 이미지 라이브러리 PIL

def main():
    
    menu = ['Home','Viewing stock information','Predicting stock value','Comparing domestic ETF']
    
    choice = st.sidebar.selectbox('메뉴', menu)
    
    if choice == menu[0] :
        
        st.header('Predicting Stock of Korea Project')
        
        if st.button('목차 정보 보기') :
            st.header('1. 주식정보 보기')
            st.subheader(' : Viewing stock information')
            st.subheader('주식을 검색하여 정보를 dataset으로 불러옵니다')
            st.subheader('<2024/04/29 기준 주식정보>')
            st.header('')
            st.header('2. 주식가치 예측')
            st.subheader(' : Predicting stock value')
            st.subheader('2000~2024년 주식데이터를 prophet을 사용하여')
            st.subheader('미래 1년치 주식가치를 예측합니다')
            st.header('')
            st.header('3. 국내 ETF 주식가치비교')
            st.subheader(' : Comparing domestic ETF stock valuations')
            
        img = Image.open('./stock1.png') 
        st.image(img, use_column_width=True) #width=True해주면 자동으로 폭을 맞춰준다
    
    elif choice == menu[1]: 
        run_view()          #다른 파일의 def함수를 가져와서 쓰는방법
    elif choice == menu[2]:
        run_predict()
    elif choice == menu[3]:
        run_compare() 

if __name__ == '__main__':
    main()