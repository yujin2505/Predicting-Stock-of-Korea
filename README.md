# Predicting Stock of Korea
데이터는 라이브러리에서 실시간으로 반영됩니다

### 기획의도
주식투자를 잘 하기 위해서는 현재 기업의 상황에 대한 정보수집이 가장 중요하지만,
그에 뒷받침되어 주가가 움직이는 흐름을 예측한다면 주식투자에 도움이 될 것이라고 생각하여 주가예측 모델을 만드는 것을 기획하였습니다. 

### 설계
1) 기업 Name을 입력받아 기업 주식에 대한 정보를 dataset으로 불러옵니다.
2) 기업코드를 입력하면 기업의 미래 1년치 주식가치를 프로펫(prophet)라이브러리를 사용하여 예측하고 년,월,주간의 주가 흐름을 그래프로 나타내었습니다.
3) 비교적 안정적인 리턴(return)을 가져오는 국내 ETF 주식을 이자율(EarningRate)을 중심으로 비교하였습니다.

### 개발(과정)
https://codebunny99.tistory.com/category/Project
블로그에 작성하였습니다.

### 핵심기술
prophet library

### 데이터출처
FinanceDataReader라이브러리
https://github.com/FinanceData/FinanceDataReader
