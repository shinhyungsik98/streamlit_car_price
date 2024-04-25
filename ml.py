import streamlit as st
import joblib
import numpy as np

def run_ml():
    st.subheader('자동차 가격 예측하기')

    #1. 예측하기 위해서, 유저한테 입력을 받습니다
    # Gender age Annual Salary Credit Card Debt New Worth

    st.text('성별을 선택하세요')
    gender = st.radio('성별 선택', ['남자','여자'])
    if gender == '남자' :
        gender = 1
    elif gender == '여자' :
        gender = 0   

    st.text('나이를 입력하세요')
    age = st.number_input('나이 입력',min_value=18,max_value=100,value=24)

    st.text('연봉을 입력하세요')
    salary = st.number_input('연봉 입력',min_value=10000,value=50000,step=1000) 

    st.text('카드빚을 입력하세요')
    debt = st.number_input('카드빚 입력',min_value=0,value=1000,step=1000)

    st.text('자산을 입력하세요')
    worth = st.number_input('자산 입력', min_value=5000, value=20000,step=1000)

    st.subheader('버튼을 누르면 예측합니다')

    if st.button('예측하기') :

        #2.예측한다
        #2-1. 모델이 있어야한다.
        regressor = joblib.load('./model/regressor.pkl')

        #2-2 유저가 입력한 데이터를, 모델에 예측할수 있도록 가공해야 한다.
        # Gender age Annual Salary Credit Card Debt New Worth
        new_data=[gender,age,salary,debt,worth]
        print(new_data)
        #넘파이를 써서 2차원 배열로 바꿔준다
        np.array(new_data).reshape(1,-1)

        new_data = np.array(new_data).reshape(1,-1)

        y_pred = regressor.predict(new_data)

        print(y_pred)

        st.write(y_pred)

        # 위의 데이터로 예측한 자동차 구매 가능 금액은 6,746달러 입니다
        #1.y_pred 에서 숫자만 가져옵니다.
        y_pred=y_pred[0]
        print(y_pred)
        #2.숫자의 소수점 뒤 제거
        y_pred = round(y_pred)
        print(y_pred)
        #3.숫자에 3자리마다 콤마넣기
        y_pred=format(y_pred,',')
        print(y_pred)
        #4. 문자열 조합하기
        st.text(f'위의 데이터로 예측한 자동차 구매 가능 금액은 {y_pred} 달러 입니다.')








    


